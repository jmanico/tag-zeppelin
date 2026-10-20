"""Validate threat-model document structure and local specification references.

This checks documentation artifacts only; it does not test application behavior.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGES = ROOT / "threat-model/stages"


def model(path):
    text = path.read_text()
    match = re.search(r"```json\n(.*?)\n```", text, re.S)
    assert match, f"No model JSON: {path}"
    return json.loads(match[1]), match[1]


required = {
    "scope", "evidence", "system", "methods", "threats", "controls",
    "requirements", "risks", "attack_trees", "attack_paths",
    "visualizations", "coverage", "conflicts", "gaps",
}
models = []
for stage in range(11):
    paths = list(STAGES.glob(f"{stage:02}-*.md"))
    assert len(paths) == 1, (stage, paths)
    value, raw = model(paths[0])
    assert required <= value.keys(), paths[0]
    assert set(value["system"]) == {
        "assets", "actors", "data", "zones", "boundaries", "flows", "entry_points"
    }, paths[0]
    models.append(value)

for previous, current in zip(models[8:10], models[9:11]):
    assert {k: v for k, v in previous.items() if k != "visualizations"} == {
        k: v for k, v in current.items() if k != "visualizations"
    }, "A visualization stage changed non-visual model data"
    for record in previous["visualizations"]:
        assert record in current["visualizations"], "Lost visualization record"

report = ROOT / "THREAT_MODEL.md"
report_model, report_raw = model(report)
assert report_raw == model(next(STAGES.glob("10-*.md")))[1], (
    "Appendix A must preserve the downstream JSON text unedited"
)
assert report_model == models[10]
for evidence in report_model["evidence"]:
    if evidence.get("id", "").startswith("POST-E") and evidence.get("sha256"):
        assert hashlib.sha256((ROOT / evidence["source"]).read_bytes()).hexdigest() == evidence["sha256"], (
            "Post-analysis specification evidence is stale", evidence["source"]
        )
threat_ids = [t["id"] for t in report_model["threats"]]
assert len(threat_ids) == len(set(threat_ids))
assert threat_ids == [t["id"] for t in models[8]["threats"]]
for threat_id in threat_ids:
    assert f'id="{threat_id.lower()}"' in report.read_text(), threat_id

# Check local Markdown targets. Historical artifacts may cite baseline locators,
# but their actual Markdown links must still resolve.
link_count = 0
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts or path.name == "REQUIREMENT_TEMPLATE.md":
        continue
    prose = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", prose):
        if "://" in target or target.startswith("mailto:"):
            continue
        location, _, fragment = target.partition("#")
        destination = (path.parent / location).resolve() if location else path
        assert destination.exists(), (path, target)
        if fragment.startswith("t-") and destination == report:
            assert fragment.upper() in threat_ids, (path, fragment)
        link_count += 1

spec_text = "\n".join(
    (ROOT / name).read_text()
    for name in ("REQUIREMENTS.md", "ARCHITECTURE.md", "SECURITY.md", "DESIGN.md")
)
assert "## Open Questions" not in spec_text
assert not re.search(r"\b(?:TO BE DECIDED|UNKNOWN|TBD|BLOCKED)\b", spec_text)
definitions = set(re.findall(r"\*\*((?:FR|NFR)-\d+\.\d+)\*\*", spec_text))
definitions.update(re.findall(r"### (SC-\d+)", spec_text))
definitions.update(re.findall(r"\| ((?:OD|RQ)-\d+) \|", spec_text))
definitions.update(re.findall(r"\*\*(DR-\d+):", spec_text))
for reference in re.findall(r"\b(?:FR-\d+\.\d+|NFR-\d+\.\d+|SC-\d+|OD-\d+|RQ-\d+|DR-\d+)\b", spec_text):
    assert reference in definitions, f"Unresolved specification ID: {reference}"

print(f"PASS: 11 stage models; {len(threat_ids)} stable threats; exact report appendix; "
      f"{link_count} local links; root specification ID references.")
print("Documentation validation only. No application tests exist or ran.")
