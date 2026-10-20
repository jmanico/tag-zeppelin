# Threat-model evidence and pipeline artifacts

The initial analysis uses the four root specifications at Git revision
`e346ef231f549b15ead023bcfbea44ac4e69e59a`. Read those versions when checking
the original evidence after specification hardening.

Pipeline instructions:
`/Users/jmanico/Dropbox/github/aegis/security-utilities-knowledge/content/pipelines/threat-modeling/README.md`.

Stages 00–07 run independently against the same specification bundle. Stage 08
receives all eight fragments; stage 09 receives its unified model; stage 10
receives the diagram artifact; stage 11 receives the visual artifact and writes
the root [THREAT_MODEL.md](../THREAT_MODEL.md).

The numbered artifacts in `stages/` preserve analysis provenance. They are
specification analyses, not implementation tests. Repeated observations from
these shared inputs are not independent confirmation. Stable threat IDs are
assigned at consolidation and retained downstream.

The root specifications own adopted behavior, architecture, controls, and
presentation. The threat report owns findings and evidence limits. Decisions
made after this initial analysis must refresh affected downstream artifacts
without rewriting the historical input evidence or reusing retired IDs.

The maintainer subsequently authorized resolving the policy decisions using
best judgment. Current owning specifications and stages 08–11 carry those
resolutions. Historical fragments retain their original evidence gaps; they
do not constitute a current unanswered-question list.

Reproduce the downstream documents from the preserved fragments and current
specifications, in order:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 threat-model/consolidate.py
PYTHONDONTWRITEBYTECODE=1 python3 threat-model/visualize.py
PYTHONDONTWRITEBYTECODE=1 python3 threat-model/report.py
PYTHONDONTWRITEBYTECODE=1 python3 threat-model/validate.py
git diff --check
```

The validator checks documentation structure, stable threat IDs, model
preservation, current specification hashes, local links, and specification
references. It does not execute application acceptance or security tests.
