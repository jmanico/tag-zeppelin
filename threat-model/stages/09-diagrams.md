# THREAT_MODEL_DIAGRAM

## Model

```json
{
  "scope": {
    "id": "S08-SCOPE",
    "description": "Pre-implementation native music editor and closed recommendation pilot; all eight requested upstream methods completed.",
    "baseline": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
    "upstream_scopes": [
      {
        "id": "S08-SOURCE00",
        "artifact": "threat-model/stages/00-stride.md",
        "scope": {
          "id": "S00-S",
          "description": "Tag a local music collection, review metadata changes, and discover music to buy. Actors are the current user, recommendation-service Admins, and participating users. The release covers local desktop distribution and an operator-run closed recommendation-service pilot.",
          "exclusions": [
            "File renaming, moving, transcoding, and automatic cover art retrieval are outside the first release.",
            "Playback and unspecified viewer functions are outside the first release.",
            "Prices, checkout, payment collection, affiliate tracking, and revenue features are outside the first release.",
            "No web frontend, embedded browser application UI, or mobile application."
          ],
          "evidence_ids": [
            "S00-E1"
          ]
        }
      },
      {
        "id": "S08-SOURCE01",
        "artifact": "threat-model/stages/01-pasta.md",
        "scope": {
          "id": "S01-S",
          "description": "Tag a local music collection, review metadata changes, and discover music to buy. Actors are the current user, recommendation-service Admins, and participating users. The release covers local desktop distribution and an operator-run closed recommendation-service pilot.",
          "exclusions": [
            "File renaming, moving, transcoding, and automatic cover art retrieval are outside the first release.",
            "Playback and unspecified viewer functions are outside the first release.",
            "Prices, checkout, payment collection, affiliate tracking, and revenue features are outside the first release.",
            "No web frontend, embedded browser application UI, or mobile application."
          ],
          "evidence_ids": [
            "S01-E1"
          ]
        }
      },
      {
        "id": "S08-SOURCE02",
        "artifact": "threat-model/stages/02-linddun.md",
        "scope": {
          "id": "S02-S",
          "description": "Tag a local music collection, review metadata changes, and discover music to buy. Actors are the current user, recommendation-service Admins, and participating users. The release covers local desktop distribution and an operator-run closed recommendation-service pilot.",
          "exclusions": [
            "File renaming, moving, transcoding, and automatic cover art retrieval are outside the first release.",
            "Playback and unspecified viewer functions are outside the first release.",
            "Prices, checkout, payment collection, affiliate tracking, and revenue features are outside the first release.",
            "No web frontend, embedded browser application UI, or mobile application."
          ],
          "evidence_ids": [
            "S02-E1"
          ]
        }
      },
      {
        "id": "S08-SOURCE03",
        "artifact": "threat-model/stages/03-attack-trees.md",
        "scope": [
          {
            "id": "S03-SCOPE",
            "description": "Specification-only analysis of native desktop and closed recommendation pilot; all four supplied specifications read independently for this method. No implementation or operational effectiveness claimed.",
            "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a"
          }
        ]
      },
      {
        "id": "S08-SOURCE04",
        "artifact": "threat-model/stages/04-fmea.md",
        "scope": [
          {
            "id": "S04-SCOPE",
            "description": "Specification-only analysis of native desktop and closed recommendation pilot; all four supplied specifications read independently for this method. No implementation or operational effectiveness claimed.",
            "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a"
          }
        ]
      },
      {
        "id": "S08-SOURCE05",
        "artifact": "threat-model/stages/05-ai-ml.md",
        "scope": [
          {
            "id": "S05-SCOPE",
            "description": "All four specifications read for AI/ML applicability. Deterministic overlap/count/tie-break recommendation algorithm is specified; it is not evidence of a trained model.",
            "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a"
          }
        ]
      },
      {
        "id": "S08-SOURCE06",
        "artifact": "threat-model/stages/06-repository.md",
        "scope": {
          "id": "S06-SCOPE",
          "baseline": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
          "status": "Pre-implementation; adopted specifications are plans, not implemented or tested controls",
          "included": [
            "AGENTS.md",
            "ARCHITECTURE.md",
            "DESIGN.md",
            "REQUIREMENTS.md",
            "REQUIREMENT_TEMPLATE.md",
            "SECURITY.md",
            "logo.svg"
          ],
          "excluded": [
            "Git metadata; newly generated pipeline artifacts are analysis outputs, not implementation; logo is a static branding asset, not application code; template placeholders are intentional"
          ]
        }
      },
      {
        "id": "S08-SOURCE07",
        "artifact": "threat-model/stages/07-documents.md",
        "scope": {
          "id": "S07-SCOPE",
          "baseline": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
          "status": "Pre-implementation; adopted specifications are plans, not implemented or tested controls"
        }
      }
    ],
    "identity_aliases": {
      "S01-A1": "S00-A1",
      "S01-A2": "S00-A2",
      "S01-A3": "S00-A3",
      "S01-A4": "S00-A4",
      "S01-U1": "S00-U1",
      "S01-U2": "S00-U2",
      "S01-U3": "S00-U3",
      "S01-U4": "S00-U4",
      "S01-D1": "S00-D1",
      "S01-D2": "S00-D2",
      "S01-D3": "S00-D3",
      "S01-D4": "S00-D4",
      "S01-Z1": "S00-Z1",
      "S01-Z2": "S00-Z2",
      "S01-Z3": "S00-Z3",
      "S01-Z4": "S00-Z4",
      "S01-B1": "S00-B1",
      "S01-B2": "S00-B2",
      "S01-B3": "S00-B3",
      "S01-B4": "S00-B4",
      "S01-F1": "S00-F1",
      "S01-F2": "S00-F2",
      "S01-F3": "S00-F3",
      "S01-F4": "S00-F4",
      "S01-F5": "S00-F5",
      "S01-F6": "S00-F6",
      "S01-P1": "S00-P1",
      "S01-P2": "S00-P2",
      "S01-P3": "S00-P3",
      "S01-P4": "S00-P4",
      "S01-P5": "S00-P5",
      "S02-A1": "S00-A1",
      "S02-A2": "S00-A2",
      "S02-A3": "S00-A3",
      "S02-A4": "S00-A4",
      "S02-U1": "S00-U1",
      "S02-U2": "S00-U2",
      "S02-U3": "S00-U3",
      "S02-U4": "S00-U4",
      "S02-D1": "S00-D1",
      "S02-D2": "S00-D2",
      "S02-D3": "S00-D3",
      "S02-D4": "S00-D4",
      "S02-Z1": "S00-Z1",
      "S02-Z2": "S00-Z2",
      "S02-Z3": "S00-Z3",
      "S02-Z4": "S00-Z4",
      "S02-B1": "S00-B1",
      "S02-B2": "S00-B2",
      "S02-B3": "S00-B3",
      "S02-B4": "S00-B4",
      "S02-F1": "S00-F1",
      "S02-F2": "S00-F2",
      "S02-F3": "S00-F3",
      "S02-F4": "S00-F4",
      "S02-F5": "S00-F5",
      "S02-F6": "S00-F6",
      "S02-P1": "S00-P1",
      "S02-P2": "S00-P2",
      "S02-P3": "S00-P3",
      "S02-P4": "S00-P4",
      "S02-P5": "S00-P5",
      "S03-A1": "S00-A1",
      "S03-A2": "S00-A2",
      "S03-A3": "S00-A3",
      "S03-A4": "S03-A4",
      "S03-A5": "S03-A5",
      "S03-A6": "S03-A6",
      "S04-A1": "S00-A1",
      "S04-A2": "S00-A2",
      "S04-A3": "S00-A3",
      "S04-A4": "S03-A4",
      "S04-A5": "S03-A5",
      "S04-A6": "S03-A6",
      "S05-A1": "S00-A1",
      "S05-A2": "S00-A2",
      "S05-A3": "S00-A3",
      "S05-A4": "S03-A4",
      "S05-A5": "S03-A5",
      "S05-A6": "S03-A6",
      "S07-A01": "S03-A5",
      "S07-A07": "S00-A2",
      "S07-A08": "S00-A1",
      "S07-A09": "S00-A3",
      "S07-ACT01": "S00-U1",
      "S07-ACT02": "S00-U2",
      "S07-ACT03": "S00-U3",
      "S07-ACT04": "S00-U4",
      "S07-Z01": "S00-Z1",
      "S07-Z02": "S00-Z3",
      "S07-Z03": "S00-Z4",
      "S07-B01": "S00-B1",
      "S07-B02": "S00-B3",
      "S07-B03": "S00-B2",
      "S07-EP01": "S00-P1",
      "S07-EP05": "S00-P5",
      "S07-F01": "S00-F1",
      "S07-F02": "S00-F2",
      "S07-F03": "S00-F3",
      "S07-F04": "S00-F4",
      "S07-F05": "S00-F5",
      "S00-C1": "C-SC-001",
      "S00-C2": "C-SC-002",
      "S00-C3": "C-SC-003",
      "S00-C4": "C-SC-004",
      "S00-C5": "C-SC-005",
      "S00-C6": "C-SC-006",
      "S00-C7": "C-SC-007",
      "S00-C8": "C-SC-008",
      "S01-C1": "C-SC-001",
      "S01-C2": "C-SC-002",
      "S01-C3": "C-SC-003",
      "S01-C4": "C-SC-004",
      "S01-C5": "C-SC-005",
      "S01-C6": "C-SC-006",
      "S01-C7": "C-SC-007",
      "S01-C8": "C-SC-008",
      "S02-C1": "C-SC-001",
      "S02-C2": "C-SC-002",
      "S02-C3": "C-SC-003",
      "S02-C4": "C-SC-004",
      "S02-C5": "C-SC-005",
      "S02-C6": "C-SC-006",
      "S02-C7": "C-SC-007",
      "S02-C8": "C-SC-008",
      "S03-C1": "C-SC-001",
      "S03-C2": "C-SC-002",
      "S03-C3": "C-SC-003",
      "S03-C4": "C-SC-004",
      "S03-C5": "C-SC-005",
      "S03-C6": "C-SC-006",
      "S03-C7": "C-SC-007",
      "S03-C8": "C-SC-008",
      "S04-C1": "C-SC-001",
      "S04-C2": "C-SC-002",
      "S04-C3": "C-SC-003",
      "S04-C4": "C-SC-004",
      "S04-C5": "C-SC-005",
      "S04-C6": "C-SC-006",
      "S04-C7": "C-SC-007",
      "S04-C8": "C-SC-008",
      "S05-C1": "C-SC-001",
      "S05-C2": "C-SC-002",
      "S05-C3": "C-SC-003",
      "S05-C4": "C-SC-004",
      "S05-C5": "C-SC-005",
      "S05-C6": "C-SC-006",
      "S05-C7": "C-SC-007",
      "S05-C8": "C-SC-008",
      "S07-C01": "C-SC-001",
      "S07-C02": "C-SC-002",
      "S07-C03": "C-SC-003",
      "S07-C04": "C-SC-004",
      "S07-C05": "C-SC-005",
      "S07-C06": "C-SC-006",
      "S07-C07": "C-SC-007",
      "S07-C08": "C-SC-008",
      "S00-T1": "T-001",
      "S00-T2": "T-002",
      "S00-T3": "T-003",
      "S00-T4": "T-004",
      "S00-T5": "T-005",
      "S00-T6": "T-006",
      "S01-T1": "T-007",
      "S01-T2": "T-008",
      "S01-T3": "T-009",
      "S02-T1": "T-010",
      "S02-T2": "T-011",
      "S02-T3": "T-012",
      "S03-T1": "T-013",
      "S03-T2": "T-014",
      "S03-T3": "T-015",
      "S03-T4": "T-016",
      "S03-T5": "T-017",
      "S03-T6": "T-018",
      "S04-T1": "T-019",
      "S04-T2": "T-020",
      "S04-T3": "T-021",
      "S04-T4": "T-022",
      "S04-T5": "T-023",
      "S04-T6": "T-024",
      "S04-T7": "T-025"
    },
    "risk_method": "No approved common risk method supplied; no unified score computed.",
    "independence": "Methods analyze the same four specifications; repetition is not independent confirmation of runtime behavior.",
    "deployment_plan": {
      "location": "Germany",
      "participants": "EEA residents aged 18 or older admitted by operator invitations; no additional identity-document collection",
      "status": "prospective adopted scope; actual host/eligibility and legal review evidence required before collection",
      "evidence_ids": [
        "POST-E02",
        "POST-E01",
        "POST-E03"
      ]
    },
    "post_analysis_status": "All ten security decisions and five product decisions resolved under maintainer authorization; all fifteen controls adopted ACTIVE, none implemented/verified. No decision deferred. Implementation, workload, privacy review, notice and release evidence remain pending."
  },
  "evidence": [
    {
      "id": "S00-E1",
      "file": "REQUIREMENTS.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-E2",
      "file": "ARCHITECTURE.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-E3",
      "file": "SECURITY.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-E4",
      "file": "DESIGN.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S01-E1",
      "file": "REQUIREMENTS.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-E2",
      "file": "ARCHITECTURE.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-E3",
      "file": "SECURITY.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-E4",
      "file": "DESIGN.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S02-E1",
      "file": "REQUIREMENTS.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-E2",
      "file": "ARCHITECTURE.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-E3",
      "file": "SECURITY.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-E4",
      "file": "DESIGN.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S03-E1",
      "source": "REQUIREMENTS.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-E2",
      "source": "ARCHITECTURE.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-E3",
      "source": "SECURITY.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-E4",
      "source": "DESIGN.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S04-E1",
      "source": "REQUIREMENTS.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-E2",
      "source": "ARCHITECTURE.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-E3",
      "source": "SECURITY.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-E4",
      "source": "DESIGN.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S05-E1",
      "source": "REQUIREMENTS.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-E2",
      "source": "ARCHITECTURE.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-E3",
      "source": "SECURITY.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-E4",
      "source": "DESIGN.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S06-E01",
      "source": "git ls-tree -r --name-only e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "claim": "Exactly seven tracked documentation/static-asset files; no implementation, manifests, build targets, deployment configuration, lockfiles, or tests.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-E02",
      "source": "AGENTS.md:17-21",
      "claim": "No application, harness, formatter or CI; release evidence still required.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-E03",
      "source": "ARCHITECTURE.md:5-18",
      "claim": "Adopted technology versions are plans, not installed dependencies.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-E04",
      "source": "SECURITY.md:3-13",
      "claim": "Controls are adopted, not passing tests; no external corpus pack selected; rejected Fastify pack.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-E05",
      "source": "local find_pack.py and resolve_prompt.py execution during stage06",
      "claim": "Finder executed for planned stack; Node.js24, Fastify5.12, Qt6.8 candidates matched; C++17/ES2022 unmatched with alternatives. All nine returned candidates resolved successfully; none adopted or applied as code findings.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S07-E01",
      "source": "REQUIREMENTS.md",
      "sections": "Entire document read",
      "type": "Product requirements",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-E02",
      "source": "ARCHITECTURE.md",
      "sections": "Entire document read",
      "type": "Adopted architecture",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-E03",
      "source": "SECURITY.md",
      "sections": "Entire document read",
      "type": "Adopted controls",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-E04",
      "source": "DESIGN.md",
      "sections": "Entire document read",
      "type": "Presentation targets",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "POST-E01",
      "source": "REQUIREMENTS.md",
      "locator": "Final adopted threat-driven specification and resolved decisions",
      "sha256": "caf0fd89d3a6dcdefbff4830b9cd481a39ab4d3b3a1faf04b129d95bee55de95",
      "status": "adopted specification under maintainer authorization; no implementation or verification",
      "baseline_preserved": true
    },
    {
      "id": "POST-E02",
      "source": "ARCHITECTURE.md",
      "locator": "Final adopted threat-driven specification and resolved decisions",
      "sha256": "e2778e8138cf48d3b8a1faecf34f723b808c802cc1c6c9ecb17b732d0c01302d",
      "status": "adopted specification under maintainer authorization; no implementation or verification",
      "baseline_preserved": true
    },
    {
      "id": "POST-E03",
      "source": "SECURITY.md",
      "locator": "Final adopted threat-driven specification and resolved decisions",
      "sha256": "813dd3d8749fbdccd91c3f2c50299247ca50c971b7782b8ab0665c57b70c0d26",
      "status": "adopted specification under maintainer authorization; no implementation or verification",
      "baseline_preserved": true
    },
    {
      "id": "POST-E04",
      "source": "DESIGN.md",
      "locator": "Final adopted threat-driven specification and resolved decisions",
      "sha256": "19ebd405746c35f0b9d8cc66528a57d1d933f7100a479ee3627f0afd1e9425ab",
      "status": "adopted specification under maintainer authorization; no implementation or verification",
      "baseline_preserved": true
    }
  ],
  "system": {
    "assets": [
      {
        "id": "S00-A1",
        "name": "Music files and recovery copies",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S03-E1",
          "S03-E2",
          "S03-E4",
          "S04-E1",
          "S04-E2",
          "S04-E4",
          "S05-E1",
          "S05-E2",
          "S05-E4",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-A1",
              "name": "Music files and recovery copies",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-A1",
              "name": "Music files and recovery copies",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-A1",
              "name": "Music files and recovery copies",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 3,
            "record": {
              "id": "S03-A1",
              "name": "Music files and recovery copies",
              "locator": "FR-1.26–FR-1.43",
              "evidence_ids": [
                "S03-E1",
                "S03-E2",
                "S03-E4"
              ]
            }
          },
          {
            "stage": 4,
            "record": {
              "id": "S04-A1",
              "name": "Music files and recovery copies",
              "locator": "FR-1.26–FR-1.43",
              "evidence_ids": [
                "S04-E1",
                "S04-E2",
                "S04-E4"
              ]
            }
          },
          {
            "stage": 5,
            "record": {
              "id": "S05-A1",
              "name": "Music files and recovery copies",
              "locator": "FR-1.26–FR-1.43",
              "evidence_ids": [
                "S05-E1",
                "S05-E2",
                "S05-E4"
              ]
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-A08",
              "name": "Music files and recovery storage",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          3,
          4,
          5,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-A2",
        "name": "Local catalog, proposals, approvals and operation state",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S03-E1",
          "S03-E2",
          "S03-E4",
          "S04-E1",
          "S04-E2",
          "S04-E4",
          "S05-E1",
          "S05-E2",
          "S05-E4",
          "S07-E02",
          "POST-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-A2",
              "name": "Local catalog, proposals, approvals and operation state",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-A2",
              "name": "Local catalog, proposals, approvals and operation state",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-A2",
              "name": "Local catalog, proposals, approvals and operation state",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 3,
            "record": {
              "id": "S03-A2",
              "name": "Local review and catalog state",
              "locator": "Interfaces and persistence",
              "evidence_ids": [
                "S03-E1",
                "S03-E2",
                "S03-E4"
              ]
            }
          },
          {
            "stage": 4,
            "record": {
              "id": "S04-A2",
              "name": "Local review and catalog state",
              "locator": "Interfaces and persistence",
              "evidence_ids": [
                "S04-E1",
                "S04-E2",
                "S04-E4"
              ]
            }
          },
          {
            "stage": 5,
            "record": {
              "id": "S05-A2",
              "name": "Local review and catalog state",
              "locator": "Interfaces and persistence",
              "evidence_ids": [
                "S05-E1",
                "S05-E2",
                "S05-E4"
              ]
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-A07",
              "name": "Local SQLite catalog",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          3,
          4,
          5,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "technology": "SQLite 3.x local catalog"
      },
      {
        "id": "S00-A3",
        "name": "Service accounts, sessions and release memberships",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S03-E1",
          "S03-E2",
          "S03-E4",
          "S04-E1",
          "S04-E2",
          "S04-E4",
          "S05-E1",
          "S05-E2",
          "S05-E4",
          "S07-E02",
          "POST-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-A3",
              "name": "Service accounts, sessions and release memberships",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-A3",
              "name": "Service accounts, sessions and release memberships",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-A3",
              "name": "Service accounts, sessions and release memberships",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 3,
            "record": {
              "id": "S03-A3",
              "name": "Accounts, sessions and memberships",
              "locator": "FR-4.1–FR-4.27",
              "evidence_ids": [
                "S03-E1",
                "S03-E2",
                "S03-E4"
              ]
            }
          },
          {
            "stage": 4,
            "record": {
              "id": "S04-A3",
              "name": "Accounts, sessions and memberships",
              "locator": "FR-4.1–FR-4.27",
              "evidence_ids": [
                "S04-E1",
                "S04-E2",
                "S04-E4"
              ]
            }
          },
          {
            "stage": 5,
            "record": {
              "id": "S05-A3",
              "name": "Accounts, sessions and memberships",
              "locator": "FR-4.1–FR-4.27",
              "evidence_ids": [
                "S05-E1",
                "S05-E2",
                "S05-E4"
              ]
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-A09",
              "name": "Service SQLite store",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          3,
          4,
          5,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "technology": "SQLite 3.x service store"
      },
      {
        "id": "S00-A4",
        "name": "Native desktop and recommendation API availability",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-A4",
              "name": "Native desktop and recommendation API availability",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-A4",
              "name": "Native desktop and recommendation API availability",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-A4",
              "name": "Native desktop and recommendation API availability",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S03-A4",
        "name": "Recommendation results",
        "locator": "FR-3.2–FR-3.16",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4",
          "S04-E1",
          "S04-E2",
          "S04-E4",
          "S05-E1",
          "S05-E2",
          "S05-E4"
        ],
        "source_records": [
          {
            "stage": 3,
            "record": {
              "id": "S03-A4",
              "name": "Recommendation results",
              "locator": "FR-3.2–FR-3.16",
              "evidence_ids": [
                "S03-E1",
                "S03-E2",
                "S03-E4"
              ]
            }
          },
          {
            "stage": 4,
            "record": {
              "id": "S04-A4",
              "name": "Recommendation results",
              "locator": "FR-3.2–FR-3.16",
              "evidence_ids": [
                "S04-E1",
                "S04-E2",
                "S04-E4"
              ]
            }
          },
          {
            "stage": 5,
            "record": {
              "id": "S05-A4",
              "name": "Recommendation results",
              "locator": "FR-3.2–FR-3.16",
              "evidence_ids": [
                "S05-E1",
                "S05-E2",
                "S05-E4"
              ]
            }
          }
        ],
        "source_stages": [
          3,
          4,
          5
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S03-A5",
        "name": "Desktop presentation",
        "locator": "Components",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4",
          "S04-E1",
          "S04-E2",
          "S04-E4",
          "S05-E1",
          "S05-E2",
          "S05-E4",
          "S07-E02",
          "POST-E02"
        ],
        "source_records": [
          {
            "stage": 3,
            "record": {
              "id": "S03-A5",
              "name": "Desktop presentation",
              "locator": "Components",
              "evidence_ids": [
                "S03-E1",
                "S03-E2",
                "S03-E4"
              ]
            }
          },
          {
            "stage": 4,
            "record": {
              "id": "S04-A5",
              "name": "Desktop presentation",
              "locator": "Components",
              "evidence_ids": [
                "S04-E1",
                "S04-E2",
                "S04-E4"
              ]
            }
          },
          {
            "stage": 5,
            "record": {
              "id": "S05-A5",
              "name": "Desktop presentation",
              "locator": "Components",
              "evidence_ids": [
                "S05-E1",
                "S05-E2",
                "S05-E4"
              ]
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-A01",
              "name": "Native desktop presentation",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          3,
          4,
          5,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "technology": "Qt 6.8 Widgets, C++17"
      },
      {
        "id": "S03-A6",
        "name": "Service availability",
        "locator": "NFR-3.1",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4",
          "S04-E1",
          "S04-E2",
          "S04-E4",
          "S05-E1",
          "S05-E2",
          "S05-E4"
        ],
        "source_records": [
          {
            "stage": 3,
            "record": {
              "id": "S03-A6",
              "name": "Service availability",
              "locator": "NFR-3.1",
              "evidence_ids": [
                "S03-E1",
                "S03-E2",
                "S03-E4"
              ]
            }
          },
          {
            "stage": 4,
            "record": {
              "id": "S04-A6",
              "name": "Service availability",
              "locator": "NFR-3.1",
              "evidence_ids": [
                "S04-E1",
                "S04-E2",
                "S04-E4"
              ]
            }
          },
          {
            "stage": 5,
            "record": {
              "id": "S05-A6",
              "name": "Service availability",
              "locator": "NFR-3.1",
              "evidence_ids": [
                "S05-E1",
                "S05-E2",
                "S05-E4"
              ]
            }
          }
        ],
        "source_stages": [
          3,
          4,
          5
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S07-A02",
        "name": "Local application/domain services",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A02",
              "name": "Local application/domain services",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-A03",
        "name": "Persistence/media adapters",
        "evidence_ids": [
          "S07-E02",
          "POST-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A03",
              "name": "Persistence/media adapters",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ],
        "technology": "TagLib 2.x adapter with restricted media helper; filesystem and SQLite adapters"
      },
      {
        "id": "S07-A04",
        "name": "Desktop discovery/sharing adapters",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A04",
              "name": "Desktop discovery/sharing adapters",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-A05",
        "name": "Service account/sharing domain",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A05",
              "name": "Service account/sharing domain",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-A06",
        "name": "Recommendation calculation",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A06",
              "name": "Recommendation calculation",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-A10",
        "name": "MusicBrainz",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A10",
              "name": "MusicBrainz",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-A11",
        "name": "OS browser/Bandcamp",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A11",
              "name": "OS browser/Bandcamp",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-A12",
        "name": "Fastify API",
        "evidence_ids": [
          "S07-E02",
          "POST-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-A12",
              "name": "Fastify API",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ],
        "technology": "Node.js 24 LTS, Fastify 5, JavaScript ES2022"
      },
      {
        "id": "POST-A01",
        "name": "Restricted local media helper",
        "technology": "Child process behind media adapter; TagLib 2.x media parsing/transformation",
        "threat_ids": [
          "T-003",
          "T-005",
          "T-021"
        ],
        "control_ids": [
          "C-SC-002",
          "C-SC-003",
          "C-SC-011"
        ],
        "authority": "Local domain retains approval, recovery and final replacement; helper has no service credentials or catalog-wide access",
        "status": "adopted post-analysis design; unimplemented",
        "evidence_ids": [
          "POST-E02"
        ]
      }
    ],
    "actors": [
      {
        "id": "S00-U1",
        "name": "Current desktop user",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E01"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-U1",
              "name": "Current desktop user",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-U1",
              "name": "Current desktop user",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-U1",
              "name": "Current desktop user",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-ACT01",
              "name": "Current local user",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-U2",
        "name": "Participating service user",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E01"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-U2",
              "name": "Participating service user",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-U2",
              "name": "Participating service user",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-U2",
              "name": "Participating service user",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-ACT02",
              "name": "Participating service user",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-U3",
        "name": "Recommendation-service Admin",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E01"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-U3",
              "name": "Recommendation-service Admin",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-U3",
              "name": "Recommendation-service Admin",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-U3",
              "name": "Recommendation-service Admin",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-ACT03",
              "name": "Recommendation-service Admin",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-U4",
        "name": "Operator",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E03"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-U4",
              "name": "Operator",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-U4",
              "name": "Operator",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-U4",
              "name": "Operator",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-ACT04",
              "name": "Operator",
              "evidence_ids": [
                "S07-E03"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S07-ACT05",
        "name": "Project maintainer",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-ACT05",
              "name": "Project maintainer",
              "evidence_ids": [
                "S07-E03"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      }
    ],
    "data": [
      {
        "id": "S00-D1",
        "name": "Audio, editable metadata, identifiers, paths and images",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-D1",
              "name": "Audio, editable metadata, identifiers, paths and images",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-D1",
              "name": "Audio, editable metadata, identifiers, paths and images",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-D1",
              "name": "Audio, editable metadata, identifiers, paths and images",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-D2",
        "name": "Username, password and session secret",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-D2",
              "name": "Username, password and session secret",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-D2",
              "name": "Username, password and session secret",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-D2",
              "name": "Username, password and session secret",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-D3",
        "name": "Shared release identifiers and account memberships",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-D3",
              "name": "Shared release identifiers and account memberships",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-D3",
              "name": "Shared release identifiers and account memberships",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-D3",
              "name": "Shared release identifiers and account memberships",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-D4",
        "name": "Operation type, result, time and correlation ID security logs",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-D4",
              "name": "Operation type, result, time and correlation ID security logs",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-D4",
              "name": "Operation type, result, time and correlation ID security logs",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-D4",
              "name": "Operation type, result, time and correlation ID security logs",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S07-D01",
        "name": "Audio, saved metadata and file paths",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-D01",
              "name": "Audio, saved metadata and file paths",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-D02",
        "name": "Pending proposals, approvals and recovery references",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-D02",
              "name": "Pending proposals, approvals and recovery references",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-D03",
        "name": "Account identifiers, release memberships and security logs: personal data",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-D03",
              "name": "Account identifiers, release memberships and security logs: personal data",
              "evidence_ids": [
                "S07-E03"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-D04",
        "name": "Password hashes and opaque-session digests; client credential-store token",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-D04",
              "name": "Password hashes and opaque-session digests; client credential-store token",
              "evidence_ids": [
                "S07-E03"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-D05",
        "name": "Previewed release identifier set",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-D05",
              "name": "Previewed release identifier set",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "POST-D01",
        "name": "Registration invitation token; stored digest and expiry/consumption state",
        "control_ids": [
          "C-SC-010"
        ],
        "threat_ids": [
          "T-009",
          "T-017"
        ],
        "sensitivity": "Invitation secret must not be logged or put in URLs",
        "status": "adopted post-analysis design; unimplemented",
        "evidence_ids": [
          "POST-E02"
        ]
      }
    ],
    "zones": [
      {
        "id": "S00-Z1",
        "name": "Native desktop process",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-Z1",
              "name": "Native desktop process",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-Z1",
              "name": "Native desktop process",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-Z1",
              "name": "Native desktop process",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-Z01",
              "name": "User desktop",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-Z2",
        "name": "User filesystem",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-Z2",
              "name": "User filesystem",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-Z2",
              "name": "User filesystem",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-Z2",
              "name": "User filesystem",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-Z3",
        "name": "Recommendation service host",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-Z3",
              "name": "Recommendation service host",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-Z3",
              "name": "Recommendation service host",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-Z3",
              "name": "Recommendation service host",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-Z02",
              "name": "Recommendation service",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-Z4",
        "name": "External MusicBrainz and browser Bandcamp services",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-Z4",
              "name": "External MusicBrainz and browser Bandcamp services",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-Z4",
              "name": "External MusicBrainz and browser Bandcamp services",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-Z4",
              "name": "External MusicBrainz and browser Bandcamp services",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-Z03",
              "name": "External MusicBrainz and OS browser/Bandcamp",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      }
    ],
    "boundaries": [
      {
        "id": "S00-B1",
        "name": "Filesystem to desktop media adapter",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-B1",
              "name": "Filesystem to desktop media adapter",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-B1",
              "name": "Filesystem to desktop media adapter",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-B1",
              "name": "Filesystem to desktop media adapter",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-B01",
              "name": "Desktop filesystem input and write boundary",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "control_ids": [
          "C-SC-002",
          "C-SC-003"
        ],
        "control_evidence_status": "adopted plan; no implemented/verified control evidence"
      },
      {
        "id": "S00-B2",
        "name": "Desktop to external services",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-B2",
              "name": "Desktop to external services",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-B2",
              "name": "Desktop to external services",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-B2",
              "name": "Desktop to external services",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-B03",
              "name": "Desktop to external network services",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "control_ids": [
          "C-SC-002",
          "C-SC-005"
        ],
        "control_evidence_status": "adopted plan; no implemented/verified control evidence"
      },
      {
        "id": "S00-B3",
        "name": "Desktop to authenticated recommendation API",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-B3",
              "name": "Desktop to authenticated recommendation API",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-B3",
              "name": "Desktop to authenticated recommendation API",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-B3",
              "name": "Desktop to authenticated recommendation API",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-B02",
              "name": "Desktop to recommendation API",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "control_ids": [
          "C-SC-001",
          "C-SC-004",
          "C-SC-005"
        ],
        "control_evidence_status": "adopted plan; no implemented/verified control evidence"
      },
      {
        "id": "S00-B4",
        "name": "API handler to service domain authorization",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-B4",
              "name": "API handler to service domain authorization",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-B4",
              "name": "API handler to service domain authorization",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-B4",
              "name": "API handler to service domain authorization",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "control_ids": [
          "C-SC-006"
        ],
        "control_evidence_status": "adopted plan; no implemented/verified control evidence"
      },
      {
        "id": "POST-B01",
        "name": "Desktop media adapter to restricted helper process",
        "control_ids": [
          "C-SC-002",
          "C-SC-003",
          "C-SC-011"
        ],
        "control_evidence_status": "ACTIVE adopted limits and isolation, not verified",
        "threat_ids": [
          "T-003",
          "T-005",
          "T-021"
        ],
        "status": "adopted post-analysis design; unimplemented",
        "evidence_ids": [
          "POST-E02"
        ]
      }
    ],
    "flows": [
      {
        "id": "S00-F1",
        "name": "Import/query: presentation to local services to media/catalog and results",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-F1",
              "name": "Import/query: presentation to local services to media/catalog and results",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-F1",
              "name": "Import/query: presentation to local services to media/catalog and results",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-F1",
              "name": "Import/query: presentation to local services to media/catalog and results",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-F01",
              "name": "Presentation to local services to media/catalog and results",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-F2",
        "name": "Review/save/restore: local domain to filesystem and catalog",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-F2",
              "name": "Review/save/restore: local domain to filesystem and catalog",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-F2",
              "name": "Review/save/restore: local domain to filesystem and catalog",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-F2",
              "name": "Review/save/restore: local domain to filesystem and catalog",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-F02",
              "name": "Reviewed save/restore through local domain to filesystem/catalog",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-F3",
        "name": "Discovery: catalog to adapter to MusicBrainz to local domain/presentation",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-F3",
              "name": "Discovery: catalog to adapter to MusicBrainz to local domain/presentation",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-F3",
              "name": "Discovery: catalog to adapter to MusicBrainz to local domain/presentation",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-F3",
              "name": "Discovery: catalog to adapter to MusicBrainz to local domain/presentation",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-F03",
              "name": "Catalog to integration adapter to MusicBrainz to presentation",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-F4",
        "name": "Sharing/recommendations: desktop to API to domain to service store and results",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-F4",
              "name": "Sharing/recommendations: desktop to API to domain to service store and results",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-F4",
              "name": "Sharing/recommendations: desktop to API to domain to service store and results",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-F4",
              "name": "Sharing/recommendations: desktop to API to domain to service store and results",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-F04",
              "name": "Desktop to HTTPS JSON API to service domain/store and results",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "historical_description": "Sharing/recommendations: desktop to API to domain to service store and results",
        "current_output": "Ranked qualifying release identifiers only; no numerical contributor counts, identities, individual libraries, cohort sizes or suppressed releases; internal exact ranking counts retained.",
        "post_analysis_evidence_ids": [
          "POST-E01",
          "POST-E02"
        ]
      },
      {
        "id": "S00-F5",
        "name": "Purchase search: desktop adapter to OS browser and Bandcamp",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E02"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-F5",
              "name": "Purchase search: desktop adapter to OS browser and Bandcamp",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-F5",
              "name": "Purchase search: desktop adapter to OS browser and Bandcamp",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-F5",
              "name": "Purchase search: desktop adapter to OS browser and Bandcamp",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-F05",
              "name": "Generated purchase search URL to OS browser",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-F6",
        "name": "API operations to operator security logs",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-F6",
              "name": "API operations to operator security logs",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-F6",
              "name": "API operations to operator security logs",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-F6",
              "name": "API operations to operator security logs",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S05-F1",
        "description": "Confirmed release memberships → service deterministic overlap/count ranking → paginated IDs/counts → desktop local exclusion and MusicBrainz label lookup.",
        "evidence_ids": [
          "S05-E1",
          "S05-E2"
        ],
        "source_records": [
          {
            "stage": 5,
            "record": {
              "id": "S05-F1",
              "description": "Confirmed release memberships → service deterministic overlap/count ranking → paginated IDs/counts → desktop local exclusion and MusicBrainz label lookup.",
              "evidence_ids": [
                "S05-E1",
                "S05-E2"
              ]
            }
          }
        ],
        "source_stages": [
          5
        ],
        "historical_description": "Confirmed release memberships → service deterministic overlap/count ranking → paginated IDs/counts → desktop local exclusion and MusicBrainz label lookup.",
        "current_output": "Ranked qualifying release identifiers only; no numerical contributor counts, identities, individual libraries, cohort sizes or suppressed releases; internal exact ranking counts retained.",
        "post_analysis_evidence_ids": [
          "POST-E01",
          "POST-E02"
        ]
      },
      {
        "id": "POST-F01",
        "name": "Bounded media adapter to restricted helper: selected input/staged file and operation data, then validated result",
        "source_id": "S07-A03",
        "destination_id": "POST-A01",
        "boundary_ids": [
          "POST-B01"
        ],
        "threat_ids": [
          "T-003",
          "T-005",
          "T-021"
        ],
        "status": "adopted post-analysis design; unimplemented",
        "evidence_ids": [
          "POST-E02"
        ]
      },
      {
        "id": "POST-F02",
        "name": "Local operator provisioning path to service account domain: issue invitations",
        "source_id": "S00-U4",
        "destination_id": "S07-A05",
        "threat_ids": [
          "T-001",
          "T-009",
          "T-017"
        ],
        "protocol": "Local command; concrete invocation format not specified",
        "status": "adopted post-analysis design; unimplemented",
        "evidence_ids": [
          "POST-E02"
        ]
      }
    ],
    "entry_points": [
      {
        "id": "S00-P1",
        "name": "Selected media, folders and JPEG/PNG cover art",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E01"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-P1",
              "name": "Selected media, folders and JPEG/PNG cover art",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-P1",
              "name": "Selected media, folders and JPEG/PNG cover art",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-P1",
              "name": "Selected media, folders and JPEG/PNG cover art",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-EP01",
              "name": "Selected files/folders and JPEG/PNG artwork",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-P2",
        "name": "MusicBrainz responses and native metadata rendering",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-P2",
              "name": "MusicBrainz responses and native metadata rendering",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-P2",
              "name": "MusicBrainz responses and native metadata rendering",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-P2",
              "name": "MusicBrainz responses and native metadata rendering",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-P3",
        "name": "Public registration and sign-in HTTPS JSON",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-P3",
              "name": "Public registration and sign-in HTTPS JSON",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-P3",
              "name": "Public registration and sign-in HTTPS JSON",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-P3",
              "name": "Public registration and sign-in HTTPS JSON",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
        "current_contract": "Registration requires invitation token, canonical ASCII username and password; invitation/admission validation precedes hashing under SC-010/SC-012.",
        "post_analysis_evidence_ids": [
          "POST-E01",
          "POST-E03"
        ]
      },
      {
        "id": "S00-P4",
        "name": "Protected account, library and recommendation HTTPS JSON",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-P4",
              "name": "Protected account, library and recommendation HTTPS JSON",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-P4",
              "name": "Protected account, library and recommendation HTTPS JSON",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-P4",
              "name": "Protected account, library and recommendation HTTPS JSON",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S00-P5",
        "name": "Local operator initial Admin command",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3",
          "S01-E1",
          "S01-E2",
          "S01-E3",
          "S02-E1",
          "S02-E2",
          "S02-E3",
          "S07-E03"
        ],
        "status": "specified",
        "source_records": [
          {
            "stage": 0,
            "record": {
              "id": "S00-P5",
              "name": "Local operator initial Admin command",
              "evidence_ids": [
                "S00-E1",
                "S00-E2",
                "S00-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 1,
            "record": {
              "id": "S01-P5",
              "name": "Local operator initial Admin command",
              "evidence_ids": [
                "S01-E1",
                "S01-E2",
                "S01-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 2,
            "record": {
              "id": "S02-P5",
              "name": "Local operator initial Admin command",
              "evidence_ids": [
                "S02-E1",
                "S02-E2",
                "S02-E3"
              ],
              "status": "specified"
            }
          },
          {
            "stage": 7,
            "record": {
              "id": "S07-EP05",
              "name": "Local operator initial-Admin provisioning command",
              "evidence_ids": [
                "S07-E03"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          0,
          1,
          2,
          7
        ],
        "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records."
      },
      {
        "id": "S07-EP02",
        "name": "Metadata manual entry and match selection",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-EP02",
              "name": "Metadata manual entry and match selection",
              "evidence_ids": [
                "S07-E01"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "S07-EP03",
        "name": "HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-EP03",
              "name": "HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ],
        "current_contract": "Registration requires invitation token, canonical ASCII username and password; invitation/admission validation precedes hashing under SC-010/SC-012.",
        "post_analysis_evidence_ids": [
          "POST-E01",
          "POST-E03"
        ]
      },
      {
        "id": "S07-EP04",
        "name": "MusicBrainz response ingress",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned",
        "source_records": [
          {
            "stage": 7,
            "record": {
              "id": "S07-EP04",
              "name": "MusicBrainz response ingress",
              "evidence_ids": [
                "S07-E02"
              ],
              "status": "planned"
            }
          }
        ],
        "source_stages": [
          7
        ]
      },
      {
        "id": "POST-EP01",
        "name": "Local operator invitation issue command",
        "threat_ids": [
          "T-001",
          "T-009",
          "T-017"
        ],
        "control_ids": [
          "C-SC-010"
        ],
        "status": "adopted post-analysis design; unimplemented",
        "evidence_ids": [
          "POST-E02"
        ]
      }
    ]
  },
  "methods": [
    {
      "id": "S00-M",
      "name": "STRIDE",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S01-M",
      "name": "PASTA",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S02-M",
      "name": "LINDDUN",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S03-M1",
      "name": "Attack trees",
      "rating_method": "Not supplied; scenarios unranked; no likelihood, severity, cost, owner, deadline or residual-risk score inferred.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S04-M1",
      "name": "FMEA",
      "rating_method": "Not supplied; scenarios unranked; no likelihood, severity, cost, owner, deadline or residual-risk score inferred.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S05-M1",
      "name": "MITRE ATLAS",
      "edition": "2026.09; format 6.0.0; modified 2026-09-15",
      "source": "https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/v6/ATLAS-2026.09.yaml",
      "verification": "Release metadata opened; individual technique enumeration not performed because no applicable AI lifecycle exists. No technique IDs emitted. Latest-release status not independently established.",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-M2",
      "name": "OWASP Machine Learning Security Top Ten",
      "edition": "Unnumbered current draft project page accessed 2026-10-20",
      "source": "https://owasp.org/projects/machine-learning-security-top-ten",
      "verification": "Draft status verified. Page did not expose an exact draft revision or category list; checklist identifiers unverified and omitted.",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-M3",
      "name": "OWASP GenAI LLM Top 10",
      "edition": "Not applicable; not opened",
      "verification": "No evidenced LLM, agent, retrieval-augmented generation, or model tool use.",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S06-METHOD",
      "name": "automated repository analysis",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S07-METHOD",
      "name": "document analysis",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    }
  ],
  "threats": [
    {
      "id": "T-001",
      "title": "Unauthorized account or Admin operation",
      "category": "Spoofing",
      "scenario": "Recommendation operations accept bearer sessions and account roles; a stolen or invalid session or client-selected ownership could act as another account unless authentication, revocation and domain authorization requirements hold.",
      "affected_ids": [
        "S00-A3",
        "S00-D2",
        "S00-B3",
        "S00-B4",
        "S00-F4",
        "S00-P3",
        "S00-P4",
        "S00-P5"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "FR-4.3, FR-4.11–FR-4.26",
        "SC-001, SC-005, SC-006"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-005",
        "C-SC-006"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S00-T1",
      "source_stage": 0,
      "method_id": "S00-M",
      "source_artifact": "threat-model/stages/00-stride.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-014"
      ],
      "relationship_basis": [
        "Account authorization: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-012",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-015"
          ],
          "action": "Consistent account-name identity",
          "exact_treatment": "Consistent account-name identity — ACTIVE\n\nApply FR-4.30's accepted spelling and lowercase canonical identity consistently to registration uniqueness, sign-in lookup and the normalized-username throttle required by SC-001. Enforce canonical uniqueness transactionally. Reject invalid spellings rather than silently removing characters. Verify case variants cannot obtain separate throttle identities or ambiguous account ownership, including concurrent registration. This policy does not normalize, truncate or restrict passwords beyond FR-4.17. Threats: [T-001](THREAT_MODEL.md#t-001), [T-009](THREAT_MODEL.md#t-009).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.30",
          "acceptance_ids": [
            "AC-FR-4.30-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Usernames MUST contain 3–32 ASCII letters, digits, or underscores. The service MUST use ASCII lowercase as the canonical account identity for uniqueness, sign-in and throttling. FR-4.17 password handling is unchanged.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-002",
      "title": "Unreviewed or destructive media mutation",
      "category": "Tampering",
      "scenario": "A source can change between review and write; replaced paths, interrupted replacement, or restoring a different copy can alter unapproved content unless approval binding and reconciliation are enforced.",
      "affected_ids": [
        "S00-A1",
        "S00-A2",
        "S00-B1",
        "S00-F2",
        "S00-P1"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "FR-1.27–FR-1.42",
        "SC-002–SC-003"
      ],
      "control_ids": [
        "C-SC-002",
        "C-SC-003"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S00-T2",
      "source_stage": 0,
      "method_id": "S00-M",
      "source_artifact": "threat-model/stages/00-stride.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-007",
        "T-013",
        "T-019",
        "T-020"
      ],
      "relationship_basis": [
        "File/recovery integrity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence task",
          "action": "Document and verify applicable race-resistant replacement/coordination, cursor binding and interrupted deletion-cleanup recovery; guarantees remain mandatory.",
          "evidence_ids": [
            "POST-E02"
          ]
        }
      ]
    },
    {
      "id": "T-003",
      "title": "Untrusted native input interpretation",
      "category": "Elevation of Privilege",
      "scenario": "Imported media, embedded cover images, external labels and metadata enter native parsing/rendering and browser handoff. Malformed input or interpretation as commands can cross that boundary if validation and plain-text handling fail.",
      "affected_ids": [
        "S00-A1",
        "S00-A4",
        "S00-D1",
        "S00-B1",
        "S00-B2",
        "S00-F1",
        "S00-F3",
        "S00-F5",
        "S00-P1",
        "S00-P2"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "FR-1.19–FR-1.22, FR-3.17",
        "SC-002",
        "DESIGN.md Components: Rendering"
      ],
      "control_ids": [
        "C-SC-002"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S00-T3",
      "source_stage": 0,
      "method_id": "S00-M",
      "source_artifact": "threat-model/stages/00-stride.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-018",
        "T-021"
      ],
      "relationship_basis": [
        "Native interpretation/resource safety: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-002",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Native input and rendering",
          "exact_treatment": "Native input and rendering\n\n- Treat imported files, metadata, cover images, and network responses as untrusted. Prevent interpretation of metadata as HTML, scripts, shell fragments, or format strings; presentation follows the rendering convention in [DESIGN.md](DESIGN.md).\n- Validate numbers, dates, image type, decoded dimensions, and allocation sizes in the local domain before use; field validity is defined in FR-1.20–FR-1.22 in [REQUIREMENTS.md](REQUIREMENTS.md). Limit cover inputs to 20 MiB encoded and 40 million decoded pixels; observable rejection is defined in FR-1.39 in [REQUIREMENTS.md](REQUIREMENTS.md). Use checked arithmetic and RAII; fuzz media adapters and run address/undefined-behavior sanitizers in supported test builds.\n- Import only selected regular files or regular files beneath selected directories; do not recursively follow symlinks, junctions, or reparse points. Check identity again before write; observable link and source-change behavior is defined in FR-1.37–FR-1.40 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Generate only HTTPS Bandcamp search URLs with encoded artist/title parameters and an allowlisted host. Hand them to the OS URL opener without a shell. Do not execute URLs or commands supplied by metadata.\n- Apply the existing cover byte/pixel limits to embedded artwork as well as separately selected images, before unbounded decoding or allocation. Verify remote response structure before domain use. Additional resource budgets depend on SC-011. Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).\n- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, and the keyboard/scaling acceptance targets in [DESIGN.md](DESIGN.md) on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-011",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-013",
            "DEC-OD-014"
          ],
          "action": "Complete resource budgets",
          "exact_treatment": "Complete resource budgets — ACTIVE\n\n- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.\n- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.\n- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.\n- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.\n- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-1.45",
          "acceptance_ids": [
            "AC-FR-1.45-4"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST reject a file whose metadata processing exceeds the limits in SC-011 in [SECURITY.md](SECURITY.md), leave the source unchanged, show a per-file error, and continue processing other files without silently truncating metadata.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted isolation; enforcement evidence pending",
          "action": "Use the restricted media helper and SC-011 process/memory budgets; keep final replacement authority in the local domain.",
          "asset_ids": [
            "POST-A01"
          ],
          "flow_ids": [
            "POST-F01"
          ],
          "evidence_ids": [
            "POST-E02"
          ]
        }
      ]
    },
    {
      "id": "T-004",
      "title": "Cross-user membership inference",
      "category": "Information Disclosure",
      "scenario": "The service exposes exact ranked release identifiers/counts for libraries sharing at least one release. In a small or distinctive overlap cohort those outputs may reveal another participant’s memberships despite omission of identities and whole-library fields.",
      "affected_ids": [
        "S00-A3",
        "S00-D3",
        "S00-B3",
        "S00-F4",
        "S00-P4"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "FR-3.2–FR-3.3, FR-3.11–FR-3.14, FR-4.10",
        "ARCHITECTURE.md Interfaces and persistence"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-004",
        "C-SC-008"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S00-T4",
      "source_stage": 0,
      "method_id": "S00-M",
      "source_artifact": "threat-model/stages/00-stride.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-008",
        "T-010"
      ],
      "relationship_basis": [
        "Membership inference: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-009",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-010"
          ],
          "action": "Recommendation inference protection",
          "exact_treatment": "Recommendation inference protection — ACTIVE\n\n- Enforce FR-3.20–FR-3.23 in the service domain before pagination. Compute exact ranking only over qualifying releases; prevent identity, candidate-support count and cohort-size disclosure in response bodies, cursor contents and errors. Present only the required generic aggregate reason. Existing SC-001/SC-004/SC-008 and FR-4.10 remain mandatory.\n- Limit each account to two admitted library replacements in any rolling 24 hours and five admitted recommendation queries in any rolling hour. Count admission atomically before calculation or mutation; rejected validation/authentication attempts remain subject to SC-001. Each cursor chain belongs to one admitted query; its page requests do not consume further query admissions, but all page requests remain subject to SC-001's authenticated-request limit. A fresh query after revision invalidation consumes a new admission. Preserve withdrawal and account deletion access; they are not library replacements. Rate-limit failure and explicit-retry behavior follow FR-4.24–FR-4.25 and FR-4.32 in REQUIREMENTS.md.\n- Do not claim that cohort thresholds, omitted counts or invitations provide anonymity or eliminate inference. Prior knowledge, collusion and comparisons over time remain residual threats. Release requires adversarial tests for fewer-than-required cohorts/contributors, contributor removal at thresholds, repeated replacements, colluding invited accounts, cross-page revision changes, and differential outputs. Verify that the specified minimums, output restrictions and limits hold and that tested recommendation functions do not disclose identities or complete libraries contrary to FR-4.10. A demonstrated violation blocks service release; record test limitations and remaining inference risk in release evidence.\n- Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.2",
          "acceptance_ids": [
            "AC-FR-3.2-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST show new-release recommendations from other participating users whose shared libraries have at least one release in common with the current user's shared library, subject to the privacy eligibility rules FR-3.20–FR-3.23.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.20",
          "acceptance_ids": [
            "AC-FR-3.20-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST return shared-library recommendations only when at least five other eligible submitted libraries overlap the requester's submitted library. Withdrawn, suspended and requester-owned libraries MUST NOT count toward this minimum.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.21",
          "acceptance_ids": [
            "AC-FR-3.21-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "A recommended release MUST occur in at least three of those eligible other libraries. The system MUST apply this privacy eligibility rule before ranking qualifying releases exactly as FR-3.3 requires; FR-3.12–FR-3.13 still apply.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.22",
          "acceptance_ids": [
            "AC-FR-3.22-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The API and desktop MUST NOT expose numerical contributor counts, contributing identities, or individual libraries with recommendations. The desktop MUST use a generic aggregate reason, such as Recommended from shared libraries. Internal counts remain necessary for FR-3.3.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.23",
          "acceptance_ids": [
            "AC-FR-3.23-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "When privacy eligibility leaves no recommendations, the system MUST explain that there is insufficient shared information to show recommendations while protecting participants, without revealing cohort sizes or suppressed releases.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.28",
          "acceptance_ids": [
            "AC-FR-4.28-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST disclose before sharing that recommendations can reveal patterns about shared music despite privacy safeguards; it MUST NOT promise anonymity or protection from every inference. FR-4.10 remains required and service release requires SC-009 verification.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ],
      "current_scenario_disposition": "Baseline exact-count exposure is historical and superseded by FR-3.20–FR-3.23. Original scenario preserved for audit; current identifier-only output, thresholds and access limits do not prove absence of inference.",
      "residual_uncertainty": "Prior knowledge, colluding invited accounts and differential outputs over time remain inference concerns. No anonymity or complete inference resistance claimed. SC-009 adversarial verification and FR-4.10 release gate remain outstanding; risk remains unrated."
    },
    {
      "id": "T-005",
      "title": "Resource exhaustion at API and parser boundaries",
      "category": "Denial of Service",
      "scenario": "The bounded host receives registration, password hashing, library replacement and recommendation work; the desktop parses user-selected media and remote responses. Saturated resources can deny service unless resource limits cover work admitted before authentication as well as parsing and response consumption.",
      "affected_ids": [
        "S00-A4",
        "S00-B1",
        "S00-B2",
        "S00-B3",
        "S00-F1",
        "S00-F3",
        "S00-F4",
        "S00-P1",
        "S00-P2",
        "S00-P3",
        "S00-P4"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "NFR-3.1",
        "SC-001–SC-002, SC-005"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-002",
        "C-SC-005",
        "C-SC-007"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S00-T5",
      "source_stage": 0,
      "method_id": "S00-M",
      "source_artifact": "threat-model/stages/00-stride.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-009",
        "T-017",
        "T-025"
      ],
      "relationship_basis": [
        "Resource admission/service capacity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-002",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Native input and rendering",
          "exact_treatment": "Native input and rendering\n\n- Treat imported files, metadata, cover images, and network responses as untrusted. Prevent interpretation of metadata as HTML, scripts, shell fragments, or format strings; presentation follows the rendering convention in [DESIGN.md](DESIGN.md).\n- Validate numbers, dates, image type, decoded dimensions, and allocation sizes in the local domain before use; field validity is defined in FR-1.20–FR-1.22 in [REQUIREMENTS.md](REQUIREMENTS.md). Limit cover inputs to 20 MiB encoded and 40 million decoded pixels; observable rejection is defined in FR-1.39 in [REQUIREMENTS.md](REQUIREMENTS.md). Use checked arithmetic and RAII; fuzz media adapters and run address/undefined-behavior sanitizers in supported test builds.\n- Import only selected regular files or regular files beneath selected directories; do not recursively follow symlinks, junctions, or reparse points. Check identity again before write; observable link and source-change behavior is defined in FR-1.37–FR-1.40 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Generate only HTTPS Bandcamp search URLs with encoded artist/title parameters and an allowlisted host. Hand them to the OS URL opener without a shell. Do not execute URLs or commands supplied by metadata.\n- Apply the existing cover byte/pixel limits to embedded artwork as well as separately selected images, before unbounded decoding or allocation. Verify remote response structure before domain use. Additional resource budgets depend on SC-011. Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).\n- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, and the keyboard/scaling acceptance targets in [DESIGN.md](DESIGN.md) on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-010",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-011",
            "DEC-OD-012"
          ],
          "action": "Pilot enrollment and registration admission",
          "exact_treatment": "Pilot enrollment and registration admission — ACTIVE\n\n- Implement FR-4.29 through the local operator provisioning path described in ARCHITECTURE.md. Generate invitation secrets from 32 cryptographically random bytes, store only their SHA-256 digests, and expire unused invitations seven days after generation. Do not log secrets or place them in URLs. No service Admin invitation API is introduced.\n- Validate invitation validity and registration admission before password hashing. Limit registration attempts to three per rolling hour per source IP and 30 per rolling hour service-wide, counting failed invitations as attempts. Enforce both counters atomically. Return generic invalid-invitation rejection without indicating whether a secret was used, expired or unknown; use existing FR-4.24 responses for rate/capacity rejection.\n- Recheck invitation validity, account capacity and canonical name uniqueness when committing account creation; consume the invitation in the same transaction. Failed creation must not leave a partial account or consume the invitation. Preserve the 100-account cap and existing sign-in/authenticated limits.\n- Rate counters used by SC-001, SC-009 and SC-010 MUST remain effective across service restarts, retain only the minimum enforcement identity/key, count and window state, and expire when their limiting windows end. Account-deletion cleanup under SC-008 remains required. Verify restart behavior and expiry as well as atomic admission.\n- Verify invalid, expired and replayed invitations, concurrent redemption, capacity and counter boundaries, transaction rollback, and rejection before hashing. Threats: [T-005](THREAT_MODEL.md#t-005), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-011",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-013",
            "DEC-OD-014"
          ],
          "action": "Complete resource budgets",
          "exact_treatment": "Complete resource budgets — ACTIVE\n\n- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.\n- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.\n- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.\n- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.\n- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-1.45",
          "acceptance_ids": [
            "AC-FR-1.45-4"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST reject a file whose metadata processing exceeds the limits in SC-011 in [SECURITY.md](SECURITY.md), leave the source unchanged, show a per-file error, and continue processing other files without silently truncating metadata.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.24",
          "acceptance_ids": [
            "AC-FR-3.24-4"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST reject an external response that exceeds SC-011 limits, show request-failure feedback with an explicit retry action, and never present truncated data as a complete result.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.32",
          "acceptance_ids": [
            "AC-FR-4.32-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST report endpoint-specific admission and privacy rate limits using FR-4.24 and require an explicit user retry after rate limiting, including recommendation queries; no automatic rate-limit retry is permitted. FR-4.25 continues to govern all mutations. Numeric limits are owned by SC-009–SC-011 in [SECURITY.md](SECURITY.md).",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted isolation; enforcement evidence pending",
          "action": "Use the restricted media helper and SC-011 process/memory budgets; keep final replacement authority in the local domain.",
          "asset_ids": [
            "POST-A01"
          ],
          "flow_ids": [
            "POST-F01"
          ],
          "evidence_ids": [
            "POST-E02"
          ]
        }
      ]
    },
    {
      "id": "T-006",
      "title": "Stale sharing or deletion results",
      "category": "Tampering",
      "scenario": "Concurrent withdrawal, suspension or replacement can invalidate recommendation pages; interrupted deletion cleanup may otherwise be reported as complete. Revision checks, transaction boundaries and pending-deletion results must remain consistent.",
      "affected_ids": [
        "S00-A3",
        "S00-D3",
        "S00-F4",
        "S00-P4"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "FR-3.16, FR-4.8–FR-4.9, FR-4.22–FR-4.27",
        "SC-004, SC-008"
      ],
      "control_ids": [
        "C-SC-004",
        "C-SC-005",
        "C-SC-008"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S00-T6",
      "source_stage": 0,
      "method_id": "S00-M",
      "source_artifact": "threat-model/stages/00-stride.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-012",
        "T-015",
        "T-022",
        "T-023"
      ],
      "relationship_basis": [
        "Deletion/eligibility freshness: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-004",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Sharing and deletion",
          "exact_treatment": "Sharing and deletion\n\n- Construct an immutable previewed identifier set bound to the confirmation required by FR-4.4–FR-4.6 in [REQUIREMENTS.md](REQUIREMENTS.md). Allow only release identifiers in the shared-library payload, separate from authentication/protocol context; reject extra fields. No import, save, refresh, retry loop, or background task may silently submit a changed library.\n- Library replacement, withdrawal, and account deletion MUST be transactional. Completion behavior is defined in FR-4.22 and FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md). Session revocation is defined in SC-005; recommendation eligibility is defined in FR-4.13 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Do not cache recommendations or persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.\n- Treat pagination cursors as untrusted input; validate their binding to the authenticated requester and membership revision on every page. The desktop must discard an invalidated accumulation under FR-3.19 in [REQUIREMENTS.md](REQUIREMENTS.md). Verify requester substitution and revision changes without treating a cursor as authorization. Threats: [T-006](THREAT_MODEL.md#t-006), [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023).\n- Verification: exact preview/submission equality, extra-field rejection, transaction rollback, concurrent withdrawal/suspension during pagination, and immediate session revocation. Trace: FR-4.4–FR-4.9, FR-4.13–FR-4.14, DR-6.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "status": "implementation evidence task",
          "action": "Document and verify applicable race-resistant replacement/coordination, cursor binding and interrupted deletion-cleanup recovery; guarantees remain mandatory.",
          "evidence_ids": [
            "POST-E02"
          ]
        }
      ]
    },
    {
      "id": "T-007",
      "title": "Approved edits can lose integrity during interrupted file operations",
      "category": "Tampering",
      "scenario": "Review, recovery creation, atomic replacement and catalog reconciliation cross independent persistence operations. A changed source or interruption threatens preservation and accurate saved-state reporting unless the specified sequence holds.",
      "affected_ids": [
        "S00-A1",
        "S00-A2",
        "S00-F2",
        "S00-B1"
      ],
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "FR-1.5, FR-1.27–FR-1.42",
        "ARCHITECTURE.md Interfaces and persistence; DR-3",
        "SC-003"
      ],
      "control_ids": [
        "C-SC-002",
        "C-SC-003"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S01-T1",
      "source_stage": 1,
      "method_id": "S01-M",
      "source_artifact": "threat-model/stages/01-pasta.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-002",
        "T-013",
        "T-019",
        "T-020"
      ],
      "relationship_basis": [
        "File/recovery integrity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence pending",
          "action": "Implement and verify existing adopted controls; no further unanswered policy choice is identified."
        }
      ]
    },
    {
      "id": "T-008",
      "title": "Recommendation output can disclose participant memberships",
      "category": "Information Disclosure",
      "scenario": "Exact overlap-based ranking and counts may expose memberships of a small or distinctive eligible set, conflicting with the intended privacy outcome if that outcome includes inference resistance.",
      "affected_ids": [
        "S00-A3",
        "S00-D3",
        "S00-F4",
        "S00-P4"
      ],
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "FR-3.2–FR-3.3, FR-4.10",
        "ARCHITECTURE.md Interfaces and persistence"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-004",
        "C-SC-008"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S01-T2",
      "source_stage": 1,
      "method_id": "S01-M",
      "source_artifact": "threat-model/stages/01-pasta.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-004",
        "T-010"
      ],
      "relationship_basis": [
        "Membership inference: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-009",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-010"
          ],
          "action": "Recommendation inference protection",
          "exact_treatment": "Recommendation inference protection — ACTIVE\n\n- Enforce FR-3.20–FR-3.23 in the service domain before pagination. Compute exact ranking only over qualifying releases; prevent identity, candidate-support count and cohort-size disclosure in response bodies, cursor contents and errors. Present only the required generic aggregate reason. Existing SC-001/SC-004/SC-008 and FR-4.10 remain mandatory.\n- Limit each account to two admitted library replacements in any rolling 24 hours and five admitted recommendation queries in any rolling hour. Count admission atomically before calculation or mutation; rejected validation/authentication attempts remain subject to SC-001. Each cursor chain belongs to one admitted query; its page requests do not consume further query admissions, but all page requests remain subject to SC-001's authenticated-request limit. A fresh query after revision invalidation consumes a new admission. Preserve withdrawal and account deletion access; they are not library replacements. Rate-limit failure and explicit-retry behavior follow FR-4.24–FR-4.25 and FR-4.32 in REQUIREMENTS.md.\n- Do not claim that cohort thresholds, omitted counts or invitations provide anonymity or eliminate inference. Prior knowledge, collusion and comparisons over time remain residual threats. Release requires adversarial tests for fewer-than-required cohorts/contributors, contributor removal at thresholds, repeated replacements, colluding invited accounts, cross-page revision changes, and differential outputs. Verify that the specified minimums, output restrictions and limits hold and that tested recommendation functions do not disclose identities or complete libraries contrary to FR-4.10. A demonstrated violation blocks service release; record test limitations and remaining inference risk in release evidence.\n- Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.2",
          "acceptance_ids": [
            "AC-FR-3.2-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST show new-release recommendations from other participating users whose shared libraries have at least one release in common with the current user's shared library, subject to the privacy eligibility rules FR-3.20–FR-3.23.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.20",
          "acceptance_ids": [
            "AC-FR-3.20-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST return shared-library recommendations only when at least five other eligible submitted libraries overlap the requester's submitted library. Withdrawn, suspended and requester-owned libraries MUST NOT count toward this minimum.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.21",
          "acceptance_ids": [
            "AC-FR-3.21-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "A recommended release MUST occur in at least three of those eligible other libraries. The system MUST apply this privacy eligibility rule before ranking qualifying releases exactly as FR-3.3 requires; FR-3.12–FR-3.13 still apply.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.22",
          "acceptance_ids": [
            "AC-FR-3.22-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The API and desktop MUST NOT expose numerical contributor counts, contributing identities, or individual libraries with recommendations. The desktop MUST use a generic aggregate reason, such as Recommended from shared libraries. Internal counts remain necessary for FR-3.3.",
          "evidence_ids": [
            "POST-E01"
          ]
        }
      ],
      "current_scenario_disposition": "Baseline exact-count exposure is historical and superseded by FR-3.20–FR-3.23. Original scenario preserved for audit; current identifier-only output, thresholds and access limits do not prove absence of inference.",
      "residual_uncertainty": "Prior knowledge, colluding invited accounts and differential outputs over time remain inference concerns. No anonymity or complete inference resistance claimed. SC-009 adversarial verification and FR-4.10 release gate remain outstanding; risk remains unrated."
    },
    {
      "id": "T-009",
      "title": "Unauthenticated work can consume bounded pilot capacity",
      "category": "Denial of Service",
      "scenario": "Registration and password sign-in precede authenticated account limits and consume a 100-account pilot and hashing/host resources. Their admission policy needs to preserve the closed-pilot and bounded-work objectives.",
      "affected_ids": [
        "S00-A3",
        "S00-A4",
        "S00-P3",
        "S00-B3"
      ],
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "REQUIREMENTS.md release scope; FR-4.2, FR-4.16, NFR-3.1",
        "SC-001, SC-005"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-005",
        "C-SC-007"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "original_id": "S01-T3",
      "source_stage": 1,
      "method_id": "S01-M",
      "source_artifact": "threat-model/stages/01-pasta.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-005",
        "T-017",
        "T-025"
      ],
      "relationship_basis": [
        "Resource admission/service capacity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-008",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Privacy and operational evidence",
          "exact_treatment": "Privacy and operational evidence\n\n- Treat account identifiers, release memberships, and security logs as personal data. Shared-library content restrictions are defined in FR-4.7 in [REQUIREMENTS.md](REQUIREMENTS.md). Local catalog and recovery files use owner-only permissions.\n- Log operation type, result, time, and correlation ID; exclude passwords, bearer tokens, invitation secrets, payload bodies, local paths, and complete libraries. Retain service security logs for 30 days and restrict access to operators. Alert on repeated authentication throttling (20 events in 5 minutes), failed deletion transactions, or certificate renewal failures through operator monitoring. Invitation-secret exclusion traces to [T-009](THREAT_MODEL.md#t-009).\n- The closed pilot uses no persistent service database backups (recommendation snapshot restrictions are defined in SC-004), so committed account/library deletion leaves no application-managed backup copy. Enable SQLite secure deletion and checkpoint/truncate WAL after deletion before reporting success; on checkpoint failure retry cleanup; user-visible status is defined in FR-4.22 in [REQUIREMENTS.md](REQUIREMENTS.md). This is logical application deletion, not a promise of forensic erasure on storage hardware. Do not enable provider snapshots without an adopted deletion/retention design. Local recovery retention is defined in FR-1.31 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Before public launch, the maintainer MUST record deployment jurisdiction, processing basis, user notice, retention/deletion handling, and dependency-license obligations in the release evidence. This gate does not assert a legal determination or waive obligations during the pilot.\n- Verification: payload/log inspection, timed retention cleanup, account/library deletion including WAL cleanup, local recovery retention, and a completed release review. Trace: [REQUIREMENTS.md](REQUIREMENTS.md) release scope, FR-1.31, FR-4.7–FR-4.9, FR-4.14.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-010",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-011",
            "DEC-OD-012"
          ],
          "action": "Pilot enrollment and registration admission",
          "exact_treatment": "Pilot enrollment and registration admission — ACTIVE\n\n- Implement FR-4.29 through the local operator provisioning path described in ARCHITECTURE.md. Generate invitation secrets from 32 cryptographically random bytes, store only their SHA-256 digests, and expire unused invitations seven days after generation. Do not log secrets or place them in URLs. No service Admin invitation API is introduced.\n- Validate invitation validity and registration admission before password hashing. Limit registration attempts to three per rolling hour per source IP and 30 per rolling hour service-wide, counting failed invitations as attempts. Enforce both counters atomically. Return generic invalid-invitation rejection without indicating whether a secret was used, expired or unknown; use existing FR-4.24 responses for rate/capacity rejection.\n- Recheck invitation validity, account capacity and canonical name uniqueness when committing account creation; consume the invitation in the same transaction. Failed creation must not leave a partial account or consume the invitation. Preserve the 100-account cap and existing sign-in/authenticated limits.\n- Rate counters used by SC-001, SC-009 and SC-010 MUST remain effective across service restarts, retain only the minimum enforcement identity/key, count and window state, and expire when their limiting windows end. Account-deletion cleanup under SC-008 remains required. Verify restart behavior and expiry as well as atomic admission.\n- Verify invalid, expired and replayed invitations, concurrent redemption, capacity and counter boundaries, transaction rollback, and rejection before hashing. Threats: [T-005](THREAT_MODEL.md#t-005), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-012",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-015"
          ],
          "action": "Consistent account-name identity",
          "exact_treatment": "Consistent account-name identity — ACTIVE\n\nApply FR-4.30's accepted spelling and lowercase canonical identity consistently to registration uniqueness, sign-in lookup and the normalized-username throttle required by SC-001. Enforce canonical uniqueness transactionally. Reject invalid spellings rather than silently removing characters. Verify case variants cannot obtain separate throttle identities or ambiguous account ownership, including concurrent registration. This policy does not normalize, truncate or restrict passwords beyond FR-4.17. Threats: [T-001](THREAT_MODEL.md#t-001), [T-009](THREAT_MODEL.md#t-009).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.29",
          "acceptance_ids": [
            "AC-FR-4.29-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Account registration MUST require a valid, unused, unexpired invitation token provisioned by the pilot operator. The service MUST consume it atomically with account creation; invalid invitations MUST receive generic rejection without creating an account.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.30",
          "acceptance_ids": [
            "AC-FR-4.30-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Usernames MUST contain 3–32 ASCII letters, digits, or underscores. The service MUST use ASCII lowercase as the canonical account identity for uniqueness, sign-in and throttling. FR-4.17 password handling is unchanged.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.32",
          "acceptance_ids": [
            "AC-FR-4.32-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST report endpoint-specific admission and privacy rate limits using FR-4.24 and require an explicit user retry after rate limiting, including recommendation queries; no automatic rate-limit retry is permitted. FR-4.25 continues to govern all mutations. Numeric limits are owned by SC-009–SC-011 in [SECURITY.md](SECURITY.md).",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.34",
          "acceptance_ids": [
            "AC-FR-4.34-9"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The closed pilot MUST admit only participants aged 18 or older and resident in the EEA through operator-controlled invitations. The operator MUST determine eligibility before issuing invitations; the application MUST NOT introduce additional identity-document collection. This is the adopted pilot scope, not a statement that any participant has been verified.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-010",
      "title": "Linking or detecting memberships through overlap output",
      "category": "Linking",
      "scenario": "Shared memberships are personal data under SC-008. Exact overlap selection and ranked identifiers/counts can link a distinctive submitted set to inferred peer memberships, even though responses omit user identities.",
      "affected_ids": [
        "S00-D3",
        "S00-A3",
        "S00-F4",
        "S00-P4"
      ],
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "FR-3.2–FR-3.3, FR-3.11–FR-3.14, FR-4.10",
        "SC-008",
        "ARCHITECTURE.md Interfaces and persistence"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-004",
        "C-SC-008"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "additional_types": [
        "Detecting",
        "Data disclosure"
      ],
      "implicated_interests": [
        "Avoid disclosure of other users’ identities or complete libraries through recommendation functions (FR-4.10)."
      ],
      "original_id": "S02-T1",
      "source_stage": 2,
      "method_id": "S02-M",
      "source_artifact": "threat-model/stages/02-linddun.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-004",
        "T-008"
      ],
      "relationship_basis": [
        "Membership inference: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-009",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-010"
          ],
          "action": "Recommendation inference protection",
          "exact_treatment": "Recommendation inference protection — ACTIVE\n\n- Enforce FR-3.20–FR-3.23 in the service domain before pagination. Compute exact ranking only over qualifying releases; prevent identity, candidate-support count and cohort-size disclosure in response bodies, cursor contents and errors. Present only the required generic aggregate reason. Existing SC-001/SC-004/SC-008 and FR-4.10 remain mandatory.\n- Limit each account to two admitted library replacements in any rolling 24 hours and five admitted recommendation queries in any rolling hour. Count admission atomically before calculation or mutation; rejected validation/authentication attempts remain subject to SC-001. Each cursor chain belongs to one admitted query; its page requests do not consume further query admissions, but all page requests remain subject to SC-001's authenticated-request limit. A fresh query after revision invalidation consumes a new admission. Preserve withdrawal and account deletion access; they are not library replacements. Rate-limit failure and explicit-retry behavior follow FR-4.24–FR-4.25 and FR-4.32 in REQUIREMENTS.md.\n- Do not claim that cohort thresholds, omitted counts or invitations provide anonymity or eliminate inference. Prior knowledge, collusion and comparisons over time remain residual threats. Release requires adversarial tests for fewer-than-required cohorts/contributors, contributor removal at thresholds, repeated replacements, colluding invited accounts, cross-page revision changes, and differential outputs. Verify that the specified minimums, output restrictions and limits hold and that tested recommendation functions do not disclose identities or complete libraries contrary to FR-4.10. A demonstrated violation blocks service release; record test limitations and remaining inference risk in release evidence.\n- Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-015",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-018",
            "DEC-OD-019"
          ],
          "action": "Privacy release-context evidence",
          "exact_treatment": "Privacy release-context evidence — ACTIVE\n\n- Verify the prospective pilot hosting location defined in ARCHITECTURE.md and the participant eligibility defined in FR-4.34 before pilot collection. Record the actual deployment and eligibility evidence; the adopted scope is not proof that a host or participants already exist. The operator's invitation workflow must confirm eligibility without collecting identity-document copies or adding service profile fields.\n- Adopt a processing plan of consent for voluntary library sharing, contractual necessity for account/service operation, and legitimate interests for the limited security logging in SC-008. These are intended bases for review, not established legal conclusions. Before any pilot personal-data collection, the maintainer must record the applicable review and evidence substantiating each operation's basis, scope, necessity, and applicable safeguards; record the logging interest/balancing assessment and consent/withdrawal design. If the review does not substantiate the plan, collection and pilot release must not begin; a reviewed specification amendment is required before using another plan.\n- Before enrollment, publish a notice with the actual operator identity/contact, processing purposes and data categories, intended bases, recipients/external services, account/library deletion, 30-day security-log retention, no persistent service backups, recommendation inference risks, applicable rights/contact route and withdrawal process. Explain that sharing withdrawal ends sharing, account deletion ends account operation, and the disclosed security-log retention is governed separately under the reviewed logging basis. Show external lookup disclosure under FR-3.18. The actual notice and review records are release evidence, not invented contents in this specification.\n- Verify notice delivery and the specified consent, withdrawal, deletion and retention behavior before pilot release. Preserve SC-008's broader public-launch review, including dependency-license obligations. Required evidence is outstanding; no compliance, anonymity or implemented-control claim follows from this ACTIVE rule. Threats: [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.2",
          "acceptance_ids": [
            "AC-FR-3.2-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST show new-release recommendations from other participating users whose shared libraries have at least one release in common with the current user's shared library, subject to the privacy eligibility rules FR-3.20–FR-3.23.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.20",
          "acceptance_ids": [
            "AC-FR-3.20-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST return shared-library recommendations only when at least five other eligible submitted libraries overlap the requester's submitted library. Withdrawn, suspended and requester-owned libraries MUST NOT count toward this minimum.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.21",
          "acceptance_ids": [
            "AC-FR-3.21-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "A recommended release MUST occur in at least three of those eligible other libraries. The system MUST apply this privacy eligibility rule before ranking qualifying releases exactly as FR-3.3 requires; FR-3.12–FR-3.13 still apply.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.22",
          "acceptance_ids": [
            "AC-FR-3.22-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The API and desktop MUST NOT expose numerical contributor counts, contributing identities, or individual libraries with recommendations. The desktop MUST use a generic aggregate reason, such as Recommended from shared libraries. Internal counts remain necessary for FR-3.3.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.23",
          "acceptance_ids": [
            "AC-FR-3.23-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "When privacy eligibility leaves no recommendations, the system MUST explain that there is insufficient shared information to show recommendations while protecting participants, without revealing cohort sizes or suppressed releases.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.28",
          "acceptance_ids": [
            "AC-FR-4.28-6"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST disclose before sharing that recommendations can reveal patterns about shared music despite privacy safeguards; it MUST NOT promise anonymity or protection from every inference. FR-4.10 remains required and service release requires SC-009 verification.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.33",
          "acceptance_ids": [
            "AC-FR-4.33-9"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Before registration and before enabling sharing, the system MUST present the service notice required by SC-015 in [SECURITY.md](SECURITY.md). Sharing consent MUST remain separate, explicit and disabled by default.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.34",
          "acceptance_ids": [
            "AC-FR-4.34-9"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The closed pilot MUST admit only participants aged 18 or older and resident in the EEA through operator-controlled invitations. The operator MUST determine eligibility before issuing invitations; the application MUST NOT introduce additional identity-document collection. This is the adopted pilot scope, not a statement that any participant has been verified.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ],
      "current_scenario_disposition": "Baseline exact-count exposure is historical and superseded by FR-3.20–FR-3.23. Original scenario preserved for audit; current identifier-only output, thresholds and access limits do not prove absence of inference.",
      "residual_uncertainty": "Prior knowledge, colluding invited accounts and differential outputs over time remain inference concerns. No anonymity or complete inference resistance claimed. SC-009 adversarial verification and FR-4.10 release gate remain outstanding; risk remains unrated."
    },
    {
      "id": "T-011",
      "title": "External lookup disclosure can be mistaken for sharing being disabled",
      "category": "Unawareness and unintervenability",
      "scenario": "MusicBrainz searches send artist/title terms without an account, independently of recommendation sharing; browser handoff sends a purchase query to Bandcamp. A sharing-disabled indicator alone does not communicate these separate data movements.",
      "affected_ids": [
        "S00-D1",
        "S00-F3",
        "S00-F5",
        "S00-B2",
        "S00-P2"
      ],
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "FR-1.13, FR-3.5, FR-3.17, FR-4.1; MusicBrainz lookup paragraph",
        "DESIGN.md Match selection, Discovery, Accounts and sharing"
      ],
      "control_ids": [
        "C-SC-002",
        "C-SC-005",
        "C-SC-008"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "implicated_interests": [
        "Awareness of search-term disclosure beyond the local collection."
      ],
      "original_id": "S02-T2",
      "source_stage": 2,
      "method_id": "S02-M",
      "source_artifact": "threat-model/stages/02-linddun.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-015",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-018",
            "DEC-OD-019"
          ],
          "action": "Privacy release-context evidence",
          "exact_treatment": "Privacy release-context evidence — ACTIVE\n\n- Verify the prospective pilot hosting location defined in ARCHITECTURE.md and the participant eligibility defined in FR-4.34 before pilot collection. Record the actual deployment and eligibility evidence; the adopted scope is not proof that a host or participants already exist. The operator's invitation workflow must confirm eligibility without collecting identity-document copies or adding service profile fields.\n- Adopt a processing plan of consent for voluntary library sharing, contractual necessity for account/service operation, and legitimate interests for the limited security logging in SC-008. These are intended bases for review, not established legal conclusions. Before any pilot personal-data collection, the maintainer must record the applicable review and evidence substantiating each operation's basis, scope, necessity, and applicable safeguards; record the logging interest/balancing assessment and consent/withdrawal design. If the review does not substantiate the plan, collection and pilot release must not begin; a reviewed specification amendment is required before using another plan.\n- Before enrollment, publish a notice with the actual operator identity/contact, processing purposes and data categories, intended bases, recipients/external services, account/library deletion, 30-day security-log retention, no persistent service backups, recommendation inference risks, applicable rights/contact route and withdrawal process. Explain that sharing withdrawal ends sharing, account deletion ends account operation, and the disclosed security-log retention is governed separately under the reviewed logging basis. Show external lookup disclosure under FR-3.18. The actual notice and review records are release evidence, not invented contents in this specification.\n- Verify notice delivery and the specified consent, withdrawal, deletion and retention behavior before pilot release. Preserve SC-008's broader public-launch review, including dependency-license obligations. Required evidence is outstanding; no compliance, anonymity or implemented-control claim follows from this ACTIVE rule. Threats: [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.18",
          "acceptance_ids": [
            "AC-FR-3.18-2"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Before an external lookup or purchase-search action sends data, the system MUST identify the receiving service and the search terms or release identifiers being sent, and explain that recommendation sharing being disabled does not disable these user-requested disclosures. This is informational context for the initiating workflow, not an additional confirmation gate for each lookup request.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.33",
          "acceptance_ids": [
            "AC-FR-4.33-9"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Before registration and before enabling sharing, the system MUST present the service notice required by SC-015 in [SECURITY.md](SECURITY.md). Sharing consent MUST remain separate, explicit and disabled by default.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-012",
      "title": "Deletion or withdrawal can leave stale membership exposure",
      "category": "Data disclosure",
      "scenario": "Withdrawal and deletion must remove membership eligibility and complete specified WAL cleanup before success; stale pagination or misleading pending-deletion presentation could continue exposing withdrawn membership results.",
      "affected_ids": [
        "S00-D3",
        "S00-A3",
        "S00-F4",
        "S00-P4"
      ],
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "FR-3.16, FR-4.8–FR-4.9, FR-4.22",
        "SC-004, SC-008",
        "DESIGN.md Accounts and sharing"
      ],
      "control_ids": [
        "C-SC-004",
        "C-SC-005",
        "C-SC-008"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability",
      "implicated_interests": [
        "Withdrawal and deletion as specified by FR-4.8–FR-4.14, FR-4.22."
      ],
      "original_id": "S02-T3",
      "source_stage": 2,
      "method_id": "S02-M",
      "source_artifact": "threat-model/stages/02-linddun.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-006",
        "T-015",
        "T-022",
        "T-023"
      ],
      "relationship_basis": [
        "Deletion/eligibility freshness: same documented adverse event; complementary methods, not independent verification."
      ],
      "clarification": "Stale cursors can expose memberships; misleading pending-deletion presentation misstates completion and does not itself cause data disclosure. Original source scenario is preserved, with these causal effects distinguished.",
      "post_analysis_actions": [
        {
          "control_id": "C-SC-015",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-018",
            "DEC-OD-019"
          ],
          "action": "Privacy release-context evidence",
          "exact_treatment": "Privacy release-context evidence — ACTIVE\n\n- Verify the prospective pilot hosting location defined in ARCHITECTURE.md and the participant eligibility defined in FR-4.34 before pilot collection. Record the actual deployment and eligibility evidence; the adopted scope is not proof that a host or participants already exist. The operator's invitation workflow must confirm eligibility without collecting identity-document copies or adding service profile fields.\n- Adopt a processing plan of consent for voluntary library sharing, contractual necessity for account/service operation, and legitimate interests for the limited security logging in SC-008. These are intended bases for review, not established legal conclusions. Before any pilot personal-data collection, the maintainer must record the applicable review and evidence substantiating each operation's basis, scope, necessity, and applicable safeguards; record the logging interest/balancing assessment and consent/withdrawal design. If the review does not substantiate the plan, collection and pilot release must not begin; a reviewed specification amendment is required before using another plan.\n- Before enrollment, publish a notice with the actual operator identity/contact, processing purposes and data categories, intended bases, recipients/external services, account/library deletion, 30-day security-log retention, no persistent service backups, recommendation inference risks, applicable rights/contact route and withdrawal process. Explain that sharing withdrawal ends sharing, account deletion ends account operation, and the disclosed security-log retention is governed separately under the reviewed logging basis. Show external lookup disclosure under FR-3.18. The actual notice and review records are release evidence, not invented contents in this specification.\n- Verify notice delivery and the specified consent, withdrawal, deletion and retention behavior before pilot release. Preserve SC-008's broader public-launch review, including dependency-license obligations. Required evidence is outstanding; no compliance, anonymity or implemented-control claim follows from this ACTIVE rule. Threats: [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.33",
          "acceptance_ids": [
            "AC-FR-4.33-9"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Before registration and before enabling sharing, the system MUST present the service notice required by SC-015 in [SECURITY.md](SECURITY.md). Sharing consent MUST remain separate, explicit and disabled by default.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-013",
      "title": "Unauthorized music-file change",
      "tree_id": "S03-AT1",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-1.5, FR-1.23–FR-1.43; SC-002–SC-003",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "C-SC-002",
        "C-SC-003"
      ],
      "original_id": "S03-T1",
      "source_stage": 3,
      "method_id": "S03-M1",
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-002",
        "T-007",
        "T-019",
        "T-020"
      ],
      "relationship_basis": [
        "File/recovery integrity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence pending",
          "action": "Implement and verify existing adopted controls; no further unanswered policy choice is identified."
        }
      ]
    },
    {
      "id": "T-014",
      "title": "Unauthorized account or shared-library change",
      "tree_id": "S03-AT2",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-4.3, FR-4.11–FR-4.26; DR-5; SC-001, SC-005–SC-006",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "C-SC-001",
        "C-SC-005",
        "C-SC-006"
      ],
      "original_id": "S03-T2",
      "source_stage": 3,
      "method_id": "S03-M1",
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-001"
      ],
      "relationship_basis": [
        "Account authorization: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence pending",
          "action": "Implement and verify existing adopted controls; no further unanswered policy choice is identified."
        }
      ]
    },
    {
      "id": "T-015",
      "title": "Disclosure of a withdrawn or suspended library through a stale result",
      "tree_id": "S03-AT3",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-3.16, FR-4.9, FR-4.13; SC-004",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "C-SC-004",
        "C-SC-005"
      ],
      "original_id": "S03-T3",
      "source_stage": 3,
      "method_id": "S03-M1",
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-006",
        "T-012",
        "T-022",
        "T-023"
      ],
      "relationship_basis": [
        "Deletion/eligibility freshness: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-004",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Sharing and deletion",
          "exact_treatment": "Sharing and deletion\n\n- Construct an immutable previewed identifier set bound to the confirmation required by FR-4.4–FR-4.6 in [REQUIREMENTS.md](REQUIREMENTS.md). Allow only release identifiers in the shared-library payload, separate from authentication/protocol context; reject extra fields. No import, save, refresh, retry loop, or background task may silently submit a changed library.\n- Library replacement, withdrawal, and account deletion MUST be transactional. Completion behavior is defined in FR-4.22 and FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md). Session revocation is defined in SC-005; recommendation eligibility is defined in FR-4.13 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Do not cache recommendations or persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.\n- Treat pagination cursors as untrusted input; validate their binding to the authenticated requester and membership revision on every page. The desktop must discard an invalidated accumulation under FR-3.19 in [REQUIREMENTS.md](REQUIREMENTS.md). Verify requester substitution and revision changes without treating a cursor as authorization. Threats: [T-006](THREAT_MODEL.md#t-006), [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023).\n- Verification: exact preview/submission equality, extra-field rejection, transaction rollback, concurrent withdrawal/suspension during pagination, and immediate session revocation. Trace: FR-4.4–FR-4.9, FR-4.13–FR-4.14, DR-6.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.19",
          "acceptance_ids": [
            "AC-FR-3.19-3"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST discard an incomplete recommendation result when its membership revision is invalidated and require the fresh query in FR-3.16 before displaying a completed ranking.",
          "evidence_ids": [
            "POST-E01"
          ]
        }
      ]
    },
    {
      "id": "T-016",
      "title": "Unconfirmed library disclosure",
      "tree_id": "S03-AT4",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-4.4–FR-4.7; SC-004; DESIGN.md Accounts and sharing",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "C-SC-004"
      ],
      "original_id": "S03-T4",
      "source_stage": 3,
      "method_id": "S03-M1",
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [],
      "post_analysis_actions": [
        {
          "status": "implementation evidence pending",
          "action": "Implement and verify existing adopted controls; no further unanswered policy choice is identified."
        }
      ]
    },
    {
      "id": "T-017",
      "title": "Service exhaustion prevents recommendation access",
      "tree_id": "S03-AT5",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-4.2, FR-4.23–FR-4.24; NFR-3.1; SC-001",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "C-SC-001",
        "C-SC-007"
      ],
      "original_id": "S03-T5",
      "source_stage": 3,
      "method_id": "S03-M1",
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-005",
        "T-009",
        "T-025"
      ],
      "relationship_basis": [
        "Resource admission/service capacity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-010",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-011",
            "DEC-OD-012"
          ],
          "action": "Pilot enrollment and registration admission",
          "exact_treatment": "Pilot enrollment and registration admission — ACTIVE\n\n- Implement FR-4.29 through the local operator provisioning path described in ARCHITECTURE.md. Generate invitation secrets from 32 cryptographically random bytes, store only their SHA-256 digests, and expire unused invitations seven days after generation. Do not log secrets or place them in URLs. No service Admin invitation API is introduced.\n- Validate invitation validity and registration admission before password hashing. Limit registration attempts to three per rolling hour per source IP and 30 per rolling hour service-wide, counting failed invitations as attempts. Enforce both counters atomically. Return generic invalid-invitation rejection without indicating whether a secret was used, expired or unknown; use existing FR-4.24 responses for rate/capacity rejection.\n- Recheck invitation validity, account capacity and canonical name uniqueness when committing account creation; consume the invitation in the same transaction. Failed creation must not leave a partial account or consume the invitation. Preserve the 100-account cap and existing sign-in/authenticated limits.\n- Rate counters used by SC-001, SC-009 and SC-010 MUST remain effective across service restarts, retain only the minimum enforcement identity/key, count and window state, and expire when their limiting windows end. Account-deletion cleanup under SC-008 remains required. Verify restart behavior and expiry as well as atomic admission.\n- Verify invalid, expired and replayed invitations, concurrent redemption, capacity and counter boundaries, transaction rollback, and rejection before hashing. Threats: [T-005](THREAT_MODEL.md#t-005), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-011",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-013",
            "DEC-OD-014"
          ],
          "action": "Complete resource budgets",
          "exact_treatment": "Complete resource budgets — ACTIVE\n\n- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.\n- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.\n- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.\n- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.\n- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.29",
          "acceptance_ids": [
            "AC-FR-4.29-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Account registration MUST require a valid, unused, unexpired invitation token provisioned by the pilot operator. The service MUST consume it atomically with account creation; invalid invitations MUST receive generic rejection without creating an account.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.32",
          "acceptance_ids": [
            "AC-FR-4.32-7"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST report endpoint-specific admission and privacy rate limits using FR-4.24 and require an explicit user retry after rate limiting, including recommendation queries; no automatic rate-limit retry is permitted. FR-4.25 continues to govern all mutations. Numeric limits are owned by SC-009–SC-011 in [SECURITY.md](SECURITY.md).",
          "evidence_ids": [
            "POST-E01"
          ]
        }
      ]
    },
    {
      "id": "T-018",
      "title": "Hostile content controls native rendering or browser handoff",
      "tree_id": "S03-AT6",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-3.5–FR-3.6, FR-3.17; SC-002; DESIGN.md Rendering",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "C-SC-002"
      ],
      "original_id": "S03-T6",
      "source_stage": 3,
      "method_id": "S03-M1",
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "mitigation": "Not supplied as a separate proposal; existing planned controls are linked in control_ids.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-003",
        "T-021"
      ],
      "relationship_basis": [
        "Native interpretation/resource safety: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence pending",
          "action": "Implement and verify existing adopted controls; no further unanswered policy choice is identified."
        }
      ]
    },
    {
      "id": "T-019",
      "title": "Approval, original file or catalog diverges during interrupted write",
      "function": "Review/save and recovery",
      "cause": "Filesystem and database operations are separate; process or disk failure is an explicitly specified test condition",
      "local_effect": "File/catalog disagreement or incorrect success display",
      "downstream_effect": "Loss of trustworthy saved state or retry state",
      "affected_ids": [
        "S00-A1"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.29–FR-1.41; Interfaces and persistence; SC-003",
      "control_ids": [
        "C-SC-003"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R1"
      ],
      "original_id": "S04-T1",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain existing specified controls and verify their stated acceptance conditions.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-002",
        "T-007",
        "T-013"
      ],
      "relationship_basis": [
        "File/recovery integrity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence task",
          "action": "Document and verify applicable race-resistant replacement/coordination, cursor binding and interrupted deletion-cleanup recovery; guarantees remain mandatory.",
          "evidence_ids": [
            "POST-E02"
          ]
        }
      ]
    },
    {
      "id": "T-020",
      "title": "Copy or destination has changed since it was recorded/reviewed",
      "function": "Recovery restore",
      "cause": "Recovery is retained until explicit deletion; path substitution checks exist, but persistent recovery-content integrity and changed-destination review are not fully specified",
      "local_effect": "Wrong prior contents or unintended current-file overwrite",
      "downstream_effect": "Recovery can destroy later valid edits",
      "affected_ids": [
        "S00-A1"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.31–FR-1.32, FR-1.37–FR-1.42; SC-003",
      "control_ids": [
        "C-SC-002",
        "C-SC-003"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain specified controls and their acceptance tests; unresolved restore semantics require an explicit decision.",
      "risk_ids": [
        "S04-R2"
      ],
      "original_id": "S04-T2",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain specified controls and their acceptance tests; unresolved restore semantics require an explicit decision.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-002",
        "T-007",
        "T-013"
      ],
      "relationship_basis": [
        "File/recovery integrity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-003",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Approved writes and recovery integrity",
          "exact_treatment": "Approved writes and recovery integrity\n\n- The local domain MUST bind approval to the reviewed file identity, original content fingerprint, and exact field changes. Serialize writes per file and enforce the sequence referenced by DR-3 in [ARCHITECTURE.md](ARCHITECTURE.md) in local services: validation, approval binding, recovery creation, then write. No view or adapter may bypass it; source-change behavior is defined in FR-1.37 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Create and flush a complete recovery copy with owner-only permissions before modifying the original. Stage on the same filesystem as the original, verify audio and unapproved metadata preservation, and use the platform’s atomic replacement operation. Fail safely when replacement cannot preserve required permissions or integrity.\n- Persist operation state before replacement and reconcile interrupted operations from actual file contents on restart. Result and retry behavior is defined in FR-1.34, FR-1.36, and FR-1.41 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Restore only an application-recorded recovery copy to its associated path; reject path substitution. Confirmation, retention, and recovery-copy failure behavior is defined in FR-1.30–FR-1.32 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Record recovery-content integrity when creating the complete recovery copy and verify it again before restoration. Bind restoration to the selected recorded copy and recheck the destination under the existing identity/substitution rules immediately before mutation. Recovery creation before restoration is governed by SC-013 and FR-1.46. Rejection behavior is FR-1.44 in [REQUIREMENTS.md](REQUIREMENTS.md). Threat: [T-020](THREAT_MODEL.md#t-020).\n- Verification: each supported format and stored field, disk-full/read-only conditions, crash injection before/after replacement, concurrent edits, retained copies, and restoration. Release requires unchanged audio and unapproved-field evidence for every supported format. Trace: FR-1.5, FR-1.23–FR-1.34, DR-3.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-013",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-016"
          ],
          "action": "Recovery-before-restore policy",
          "exact_treatment": "Recovery-before-restore policy — ACTIVE\n\nImplement FR-1.46 through the existing SC-003 sequence: verify the selected recovery copy and current destination identity, create and flush a complete integrity-recorded recovery copy of the destination, then perform verified replacement and catalog reconciliation. Failure before replacement leaves the destination unchanged; retain the selected and newly created recovery copies until explicit deletion under FR-1.31. Preserve renewed review, source-change rejection, owner-only permissions, atomic replacement, operation-state persistence and FR-1.44 integrity failure behavior. Verify disk-full/copy failures, changed sources, corrupted copies and interruption before/after replacement; do not report restoration complete until reconciliation. Threat: [T-020](THREAT_MODEL.md#t-020).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-1.44",
          "acceptance_ids": [
            "AC-FR-1.44-1"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST reject restoration when the selected recovery copy fails the integrity check defined in SC-003 in [SECURITY.md](SECURITY.md), leave the destination unchanged, and show a per-file failure.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-1.46",
          "acceptance_ids": [
            "AC-FR-1.46-5"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "Before restoration overwrites the current destination, the system MUST create and verify a complete recovery copy of that destination; failure MUST cancel restoration. All recovery copies remain subject to FR-1.31.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-021",
      "title": "Malformed input exhausts resources or cannot be interpreted safely",
      "function": "Native import and display",
      "cause": "Untrusted media/cover/network inputs and decoder allocations",
      "local_effect": "One import or UI operation fails",
      "downstream_effect": "Loss of availability; processing other files must continue",
      "affected_ids": [
        "S03-A5"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.10–FR-1.11, FR-1.22, FR-1.39; SC-002; DESIGN.md Rendering",
      "control_ids": [
        "C-SC-002"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R3"
      ],
      "original_id": "S04-T3",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain existing specified controls and verify their stated acceptance conditions.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-003",
        "T-018"
      ],
      "relationship_basis": [
        "Native interpretation/resource safety: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-002",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Native input and rendering",
          "exact_treatment": "Native input and rendering\n\n- Treat imported files, metadata, cover images, and network responses as untrusted. Prevent interpretation of metadata as HTML, scripts, shell fragments, or format strings; presentation follows the rendering convention in [DESIGN.md](DESIGN.md).\n- Validate numbers, dates, image type, decoded dimensions, and allocation sizes in the local domain before use; field validity is defined in FR-1.20–FR-1.22 in [REQUIREMENTS.md](REQUIREMENTS.md). Limit cover inputs to 20 MiB encoded and 40 million decoded pixels; observable rejection is defined in FR-1.39 in [REQUIREMENTS.md](REQUIREMENTS.md). Use checked arithmetic and RAII; fuzz media adapters and run address/undefined-behavior sanitizers in supported test builds.\n- Import only selected regular files or regular files beneath selected directories; do not recursively follow symlinks, junctions, or reparse points. Check identity again before write; observable link and source-change behavior is defined in FR-1.37–FR-1.40 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Generate only HTTPS Bandcamp search URLs with encoded artist/title parameters and an allowlisted host. Hand them to the OS URL opener without a shell. Do not execute URLs or commands supplied by metadata.\n- Apply the existing cover byte/pixel limits to embedded artwork as well as separately selected images, before unbounded decoding or allocation. Verify remote response structure before domain use. Additional resource budgets depend on SC-011. Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).\n- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, and the keyboard/scaling acceptance targets in [DESIGN.md](DESIGN.md) on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-011",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-013",
            "DEC-OD-014"
          ],
          "action": "Complete resource budgets",
          "exact_treatment": "Complete resource budgets — ACTIVE\n\n- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.\n- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.\n- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.\n- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.\n- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-1.45",
          "acceptance_ids": [
            "AC-FR-1.45-4"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST reject a file whose metadata processing exceeds the limits in SC-011 in [SECURITY.md](SECURITY.md), leave the source unchanged, show a per-file error, and continue processing other files without silently truncating metadata.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.24",
          "acceptance_ids": [
            "AC-FR-3.24-4"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST reject an external response that exceeds SC-011 limits, show request-failure feedback with an explicit retry action, and never present truncated data as a complete result.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted isolation; enforcement evidence pending",
          "action": "Use the restricted media helper and SC-011 process/memory budgets; keep final replacement authority in the local domain.",
          "asset_ids": [
            "POST-A01"
          ],
          "flow_ids": [
            "POST-F01"
          ],
          "evidence_ids": [
            "POST-E02"
          ]
        }
      ]
    },
    {
      "id": "T-022",
      "title": "Deletion commits but WAL cleanup fails",
      "function": "Shared-library mutation/deletion",
      "cause": "SC-008 explicitly anticipates checkpoint failure",
      "local_effect": "Logical deletion and cleanup have different completion states",
      "downstream_effect": "Premature success can misstate privacy status",
      "affected_ids": [
        "S00-A3"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-4.22, FR-4.27; SC-004, SC-008",
      "control_ids": [
        "C-SC-004",
        "C-SC-008"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R4"
      ],
      "original_id": "S04-T4",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain existing specified controls and verify their stated acceptance conditions.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-006",
        "T-012",
        "T-015"
      ],
      "relationship_basis": [
        "Deletion/eligibility freshness: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "status": "implementation evidence task",
          "action": "Document and verify applicable race-resistant replacement/coordination, cursor binding and interrupted deletion-cleanup recovery; guarantees remain mandatory.",
          "evidence_ids": [
            "POST-E02"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-023",
      "title": "Eligibility changes between pages",
      "function": "Recommendation pagination",
      "cause": "Withdrawal, suspension or replacement changes membership revision",
      "local_effect": "Stale cursor or mixed result versions",
      "downstream_effect": "Withdrawn/suspended contributions exposed or ranking inconsistent",
      "affected_ids": [
        "S03-A4"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-3.11–FR-3.16, FR-4.9, FR-4.13; SC-004",
      "control_ids": [
        "C-SC-004",
        "C-SC-005"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R5"
      ],
      "original_id": "S04-T5",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain existing specified controls and verify their stated acceptance conditions.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-006",
        "T-012",
        "T-015"
      ],
      "relationship_basis": [
        "Deletion/eligibility freshness: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-004",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [],
          "action": "Sharing and deletion",
          "exact_treatment": "Sharing and deletion\n\n- Construct an immutable previewed identifier set bound to the confirmation required by FR-4.4–FR-4.6 in [REQUIREMENTS.md](REQUIREMENTS.md). Allow only release identifiers in the shared-library payload, separate from authentication/protocol context; reject extra fields. No import, save, refresh, retry loop, or background task may silently submit a changed library.\n- Library replacement, withdrawal, and account deletion MUST be transactional. Completion behavior is defined in FR-4.22 and FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md). Session revocation is defined in SC-005; recommendation eligibility is defined in FR-4.13 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Do not cache recommendations or persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.\n- Treat pagination cursors as untrusted input; validate their binding to the authenticated requester and membership revision on every page. The desktop must discard an invalidated accumulation under FR-3.19 in [REQUIREMENTS.md](REQUIREMENTS.md). Verify requester substitution and revision changes without treating a cursor as authorization. Threats: [T-006](THREAT_MODEL.md#t-006), [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023).\n- Verification: exact preview/submission equality, extra-field rejection, transaction rollback, concurrent withdrawal/suspension during pagination, and immediate session revocation. Trace: FR-4.4–FR-4.9, FR-4.13–FR-4.14, DR-6.",
          "evidence_ids": [
            "S00-E3",
            "S01-E3",
            "S02-E3",
            "S03-E3",
            "S04-E3",
            "S05-E3",
            "S07-E03",
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-3.19",
          "acceptance_ids": [
            "AC-FR-3.19-3"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "The system MUST discard an incomplete recommendation result when its membership revision is invalidated and require the fresh query in FR-3.16 before displaying a completed ranking.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "implementation evidence task",
          "action": "Document and verify applicable race-resistant replacement/coordination, cursor binding and interrupted deletion-cleanup recovery; guarantees remain mandatory.",
          "evidence_ids": [
            "POST-E02"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    },
    {
      "id": "T-024",
      "title": "Credential store, certificate or metadata endpoint unavailable",
      "function": "Credentials and network adapters",
      "cause": "Explicitly specified secure-storage, TLS and request-failure cases",
      "local_effect": "Sign-in persistence or online functions fail closed",
      "downstream_effect": "Local workflows must remain usable",
      "affected_ids": [
        "S00-A2"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.17, FR-3.9, FR-4.20; NFR-2.1–NFR-2.2; SC-005",
      "control_ids": [
        "C-SC-005"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R6"
      ],
      "original_id": "S04-T6",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain existing specified controls and verify their stated acceptance conditions.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [],
      "post_analysis_actions": [
        {
          "status": "implementation evidence pending",
          "action": "Implement and verify existing adopted controls; no further unanswered policy choice is identified."
        }
      ]
    },
    {
      "id": "T-025",
      "title": "Single service store unavailable or bounded workload misses target",
      "function": "Pilot storage and workload",
      "cause": "One API host and local SQLite store; persistent service backups deliberately excluded",
      "local_effect": "Service unavailable or membership/account data unavailable",
      "downstream_effect": "Service release blocked on workload failure; no persistent backup recovery promised",
      "affected_ids": [
        "S03-A6"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "NFR-3.1; OD-005, OD-007; SC-007–SC-008",
      "control_ids": [
        "C-SC-001",
        "C-SC-007",
        "C-SC-008"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R7"
      ],
      "original_id": "S04-T7",
      "source_stage": 4,
      "method_id": "S04-M1",
      "source_artifact": "threat-model/stages/04-fmea.md",
      "mitigation": "Retain existing specified controls and verify their stated acceptance conditions.",
      "rating_status": "Unrated: no approved method or inputs supplied",
      "related_threat_ids": [
        "T-005",
        "T-009",
        "T-017"
      ],
      "relationship_basis": [
        "Resource admission/service capacity: same documented adverse event; complementary methods, not independent verification."
      ],
      "post_analysis_actions": [
        {
          "control_id": "C-SC-011",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-013",
            "DEC-OD-014"
          ],
          "action": "Complete resource budgets",
          "exact_treatment": "Complete resource budgets — ACTIVE\n\n- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.\n- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.\n- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.\n- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.\n- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "control_id": "C-SC-014",
          "status": "ACTIVE adopted treatment; implementation/acceptance evidence pending",
          "decision_ids": [
            "DEC-OD-017"
          ],
          "action": "Service recovery objectives",
          "exact_treatment": "Service recovery objectives — ACTIVE\n\nImplement FR-4.31's best-effort empty-service reprovisioning after loss of the single service store. Do not introduce snapshots or persistent database backups prohibited by SC-008. Reprovision host restrictions, TLS, initial Admin and invitation generation before renewed enrollment; lost sessions are invalid and previous memberships cannot be reconstructed from logs. Record a store-loss recovery exercise and clean migration/rollback evidence before pilot release. Recovery must not revive deleted memberships or silently resubmit desktop libraries. No data-recovery guarantee or recovery-time deadline is promised. Threat: [T-025](THREAT_MODEL.md#t-025).",
          "evidence_ids": [
            "POST-E03"
          ]
        },
        {
          "requirement_id": "REQ-FR-4.31",
          "acceptance_ids": [
            "AC-FR-4.31-8"
          ],
          "status": "adopted behavior; future acceptance verification required",
          "action": "If the pilot service store is lost, the service MUST report unavailability until the operator reprovisions an empty service. Returning users MUST register with new invitations and explicitly resubmit libraries. The pilot promises neither recovery of lost service data nor a recovery deadline; local files and local workflows remain independent.",
          "evidence_ids": [
            "POST-E01"
          ]
        },
        {
          "status": "adopted presentation; native verification pending",
          "action": "Apply DESIGN.md Privacy and pilot feedback, External disclosure context, and Incomplete operations as relevant; preserve plain text and accessible status distinctions.",
          "evidence_ids": [
            "POST-E04"
          ]
        }
      ]
    }
  ],
  "controls": [
    {
      "id": "C-SC-001",
      "source_id": "SC-001",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-001",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C1",
            "source_id": "SC-001",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-001",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C1",
            "source_id": "SC-001",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-001",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C1",
            "source_id": "SC-001",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-001",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C1",
            "specification_id": "SC-001",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C1",
            "specification_id": "SC-001",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C1",
            "specification_id": "SC-001",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C01",
            "source_id": "SC-001",
            "name": "Service boundary controls",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-001",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Service boundary controls",
      "exact_text": "Service boundary controls\n\n- The API MUST validate bounded JSON request schemas, reject extra properties, and validate MusicBrainz release identifiers as UUIDs before domain processing. Schemas are application-owned, never client-supplied executable definitions.\n- Every protected operation MUST authenticate and recheck account status. Derive ownership from the session; deny cross-account access and require the Admin role for suspension/restoration. Parameterize SQL and authorize before mutation.\n- Enforce a pilot capacity of 100 accounts and 10,000 distinct release identifiers per account; library bodies are limited to 512 KiB and other request bodies to 16 KiB. Limit recommendation pages to 200 results and 64 KiB. Enforce a 15-second API request deadline and a 10-second outbound lookup deadline. Failure responses follow FR-4.23–FR-4.25 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Permit at most 60 authenticated requests per minute per account and 10 sign-in attempts per minute per source IP and normalized username, tracked independently. Bound queued work; observable rejection behavior is defined in FR-4.18 and FR-4.24 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Verification: test missing, forged, expired, suspended, non-owner, and non-Admin sessions; malformed/oversized requests; injection strings; capacity boundaries; and response schemas that exclude other users’ identities and complete libraries. Trace: FR-4.3, FR-4.10–FR-4.15, DR-4–DR-5.",
      "decision_ids": [],
      "threat_ids": []
    },
    {
      "id": "C-SC-002",
      "source_id": "SC-002",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-002",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C2",
            "source_id": "SC-002",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-002",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C2",
            "source_id": "SC-002",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-002",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C2",
            "source_id": "SC-002",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-002",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C2",
            "specification_id": "SC-002",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C2",
            "specification_id": "SC-002",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C2",
            "specification_id": "SC-002",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C02",
            "source_id": "SC-002",
            "name": "Native input and rendering",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-002",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Native input and rendering",
      "exact_text": "Native input and rendering\n\n- Treat imported files, metadata, cover images, and network responses as untrusted. Prevent interpretation of metadata as HTML, scripts, shell fragments, or format strings; presentation follows the rendering convention in [DESIGN.md](DESIGN.md).\n- Validate numbers, dates, image type, decoded dimensions, and allocation sizes in the local domain before use; field validity is defined in FR-1.20–FR-1.22 in [REQUIREMENTS.md](REQUIREMENTS.md). Limit cover inputs to 20 MiB encoded and 40 million decoded pixels; observable rejection is defined in FR-1.39 in [REQUIREMENTS.md](REQUIREMENTS.md). Use checked arithmetic and RAII; fuzz media adapters and run address/undefined-behavior sanitizers in supported test builds.\n- Import only selected regular files or regular files beneath selected directories; do not recursively follow symlinks, junctions, or reparse points. Check identity again before write; observable link and source-change behavior is defined in FR-1.37–FR-1.40 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Generate only HTTPS Bandcamp search URLs with encoded artist/title parameters and an allowlisted host. Hand them to the OS URL opener without a shell. Do not execute URLs or commands supplied by metadata.\n- Apply the existing cover byte/pixel limits to embedded artwork as well as separately selected images, before unbounded decoding or allocation. Verify remote response structure before domain use. Additional resource budgets depend on SC-011. Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).\n- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, and the keyboard/scaling acceptance targets in [DESIGN.md](DESIGN.md) on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.",
      "decision_ids": [],
      "threat_ids": [
        "T-003",
        "T-005",
        "T-021"
      ]
    },
    {
      "id": "C-SC-003",
      "source_id": "SC-003",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-003",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C3",
            "source_id": "SC-003",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-003",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C3",
            "source_id": "SC-003",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-003",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C3",
            "source_id": "SC-003",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-003",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C3",
            "specification_id": "SC-003",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C3",
            "specification_id": "SC-003",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C3",
            "specification_id": "SC-003",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C03",
            "source_id": "SC-003",
            "name": "Approved writes and recovery integrity",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-003",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Approved writes and recovery integrity",
      "exact_text": "Approved writes and recovery integrity\n\n- The local domain MUST bind approval to the reviewed file identity, original content fingerprint, and exact field changes. Serialize writes per file and enforce the sequence referenced by DR-3 in [ARCHITECTURE.md](ARCHITECTURE.md) in local services: validation, approval binding, recovery creation, then write. No view or adapter may bypass it; source-change behavior is defined in FR-1.37 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Create and flush a complete recovery copy with owner-only permissions before modifying the original. Stage on the same filesystem as the original, verify audio and unapproved metadata preservation, and use the platform’s atomic replacement operation. Fail safely when replacement cannot preserve required permissions or integrity.\n- Persist operation state before replacement and reconcile interrupted operations from actual file contents on restart. Result and retry behavior is defined in FR-1.34, FR-1.36, and FR-1.41 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Restore only an application-recorded recovery copy to its associated path; reject path substitution. Confirmation, retention, and recovery-copy failure behavior is defined in FR-1.30–FR-1.32 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Record recovery-content integrity when creating the complete recovery copy and verify it again before restoration. Bind restoration to the selected recorded copy and recheck the destination under the existing identity/substitution rules immediately before mutation. Recovery creation before restoration is governed by SC-013 and FR-1.46. Rejection behavior is FR-1.44 in [REQUIREMENTS.md](REQUIREMENTS.md). Threat: [T-020](THREAT_MODEL.md#t-020).\n- Verification: each supported format and stored field, disk-full/read-only conditions, crash injection before/after replacement, concurrent edits, retained copies, and restoration. Release requires unchanged audio and unapproved-field evidence for every supported format. Trace: FR-1.5, FR-1.23–FR-1.34, DR-3.",
      "decision_ids": [],
      "threat_ids": [
        "T-020"
      ]
    },
    {
      "id": "C-SC-004",
      "source_id": "SC-004",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-004",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C4",
            "source_id": "SC-004",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-004",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C4",
            "source_id": "SC-004",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-004",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C4",
            "source_id": "SC-004",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-004",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C4",
            "specification_id": "SC-004",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C4",
            "specification_id": "SC-004",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C4",
            "specification_id": "SC-004",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C04",
            "source_id": "SC-004",
            "name": "Sharing and deletion",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-004",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Sharing and deletion",
      "exact_text": "Sharing and deletion\n\n- Construct an immutable previewed identifier set bound to the confirmation required by FR-4.4–FR-4.6 in [REQUIREMENTS.md](REQUIREMENTS.md). Allow only release identifiers in the shared-library payload, separate from authentication/protocol context; reject extra fields. No import, save, refresh, retry loop, or background task may silently submit a changed library.\n- Library replacement, withdrawal, and account deletion MUST be transactional. Completion behavior is defined in FR-4.22 and FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md). Session revocation is defined in SC-005; recommendation eligibility is defined in FR-4.13 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Do not cache recommendations or persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.\n- Treat pagination cursors as untrusted input; validate their binding to the authenticated requester and membership revision on every page. The desktop must discard an invalidated accumulation under FR-3.19 in [REQUIREMENTS.md](REQUIREMENTS.md). Verify requester substitution and revision changes without treating a cursor as authorization. Threats: [T-006](THREAT_MODEL.md#t-006), [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023).\n- Verification: exact preview/submission equality, extra-field rejection, transaction rollback, concurrent withdrawal/suspension during pagination, and immediate session revocation. Trace: FR-4.4–FR-4.9, FR-4.13–FR-4.14, DR-6.",
      "decision_ids": [],
      "threat_ids": [
        "T-006",
        "T-015",
        "T-023"
      ]
    },
    {
      "id": "C-SC-005",
      "source_id": "SC-005",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-005",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C5",
            "source_id": "SC-005",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-005",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C5",
            "source_id": "SC-005",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-005",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C5",
            "source_id": "SC-005",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-005",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C5",
            "specification_id": "SC-005",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C5",
            "specification_id": "SC-005",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C5",
            "specification_id": "SC-005",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C05",
            "source_id": "SC-005",
            "name": "Credentials, sessions, and transport",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-005",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Credentials, sessions, and transport",
      "exact_text": "Credentials, sessions, and transport\n\n- Hash passwords with Argon2id using at least 19 MiB memory, two iterations, parallelism one, and a unique random salt. Password acceptance is defined in FR-4.17 in [REQUIREMENTS.md](REQUIREMENTS.md); never store or log plaintext passwords. These hashing minima follow the [OWASP password-storage guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).\n- Generate opaque session secrets from 32 cryptographically random bytes and store only their SHA-256 digests server-side. Send bearer tokens only in Authorization headers, never URLs. Expire sessions after 30 minutes idle or 24 hours absolute, whichever occurs first; sign-out, suspension, and deletion revoke them immediately. These lifetimes are project decisions informed by [OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).\n- Store client tokens in Windows Credential Manager, macOS Keychain, or Linux Secret Service. If secure storage is unavailable, keep the token in memory only (restart behavior is defined in FR-4.20 in [REQUIREMENTS.md](REQUIREMENTS.md)). Never persist passwords. Provision the initial Admin through a local operator command; role-setting rejection is defined in FR-4.21 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Require TLS 1.2 or newer with certificate/hostname verification for service and metadata calls. Never disable verification or downgrade to plaintext. The operator owns API certificate renewal; failed verification ends the request. Do not forward credentials across redirects or origins.\n- Verification: stored hash inspection, invalid certificates, expired/revoked sessions, credential-store failure, restart behavior, role escalation, and secret-free logs. Trace: FR-4.2–FR-4.3, FR-4.16–FR-4.21, OD-006.",
      "decision_ids": [],
      "threat_ids": []
    },
    {
      "id": "C-SC-006",
      "source_id": "SC-006",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-006",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C6",
            "source_id": "SC-006",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-006",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C6",
            "source_id": "SC-006",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-006",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C6",
            "source_id": "SC-006",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-006",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C6",
            "specification_id": "SC-006",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C6",
            "specification_id": "SC-006",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C6",
            "specification_id": "SC-006",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C06",
            "source_id": "SC-006",
            "name": "Domain authorization",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-006",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Domain authorization",
      "exact_text": "Domain authorization\n\nTechnology selection is recorded in OD-004 in [ARCHITECTURE.md](ARCHITECTURE.md). Implement deny-by-default owner/Admin checks in the service domain, including direct invocation paths outside HTTP handlers. Test every role/operation pair and ensure a hidden desktop control is never treated as an authorization decision. Trace: FR-4.11–FR-4.15, DR-5.",
      "decision_ids": [],
      "threat_ids": []
    },
    {
      "id": "C-SC-007",
      "source_id": "SC-007",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-007",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C7",
            "source_id": "SC-007",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-007",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C7",
            "source_id": "SC-007",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-007",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C7",
            "source_id": "SC-007",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-007",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C7",
            "specification_id": "SC-007",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C7",
            "specification_id": "SC-007",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C7",
            "specification_id": "SC-007",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C07",
            "source_id": "SC-007",
            "name": "Build and host controls",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-007",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Build and host controls",
      "exact_text": "Build and host controls\n\nDeployment selection is recorded in OD-005 in [ARCHITECTURE.md](ARCHITECTURE.md). Run the API as a dedicated non-root systemd user with write access only to its service database/state directory. Restrict inbound traffic to the HTTPS API. Pin exact compiler, SDK, Qt, TagLib, SQLite, Node.js, and Fastify patches in reproducible lockfiles/build manifests; version-line choices do not permit floating dependencies. Require the same acceptance checks for dependency updates. Sign Windows and macOS artifacts and publish authenticated Linux package checksums. Verify artifact integrity, scan dependencies against upstream advisories, and record an SBOM. The operator provisions the TLS certificate. Block release for unmitigated applicable high/critical vulnerabilities. Test clean installation, upgrades, and rollback on each acceptance platform; verify package signatures/checksums and service filesystem restrictions. Trace: OD-001–OD-003, OD-005, OD-007 in [ARCHITECTURE.md](ARCHITECTURE.md).",
      "decision_ids": [],
      "threat_ids": []
    },
    {
      "id": "C-SC-008",
      "source_id": "SC-008",
      "evidence_ids": [
        "S00-E3",
        "S01-E3",
        "S02-E3",
        "S03-E3",
        "S04-E3",
        "S05-E3",
        "S07-E03",
        "POST-E03"
      ],
      "locator": "SECURITY.md SC-008",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "source_records": [
        {
          "stage": 0,
          "record": {
            "id": "S00-C8",
            "source_id": "SC-008",
            "evidence_ids": [
              "S00-E3"
            ],
            "locator": "SECURITY.md SC-008",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 1,
          "record": {
            "id": "S01-C8",
            "source_id": "SC-008",
            "evidence_ids": [
              "S01-E3"
            ],
            "locator": "SECURITY.md SC-008",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 2,
          "record": {
            "id": "S02-C8",
            "source_id": "SC-008",
            "evidence_ids": [
              "S02-E3"
            ],
            "locator": "SECURITY.md SC-008",
            "status": "adopted, unimplemented and unverified"
          }
        },
        {
          "stage": 3,
          "record": {
            "id": "S03-C8",
            "specification_id": "SC-008",
            "evidence_ids": [
              "S03-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 4,
          "record": {
            "id": "S04-C8",
            "specification_id": "SC-008",
            "evidence_ids": [
              "S04-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 5,
          "record": {
            "id": "S05-C8",
            "specification_id": "SC-008",
            "evidence_ids": [
              "S05-E3"
            ],
            "status": "adopted planned control; unimplemented and untested"
          }
        },
        {
          "stage": 7,
          "record": {
            "id": "S07-C08",
            "source_id": "SC-008",
            "name": "Privacy and operational evidence",
            "evidence_ids": [
              "S07-E03"
            ],
            "source_section": "SECURITY.md SC-008",
            "status": "adopted plan; not implemented or tested"
          }
        }
      ],
      "source_stages": [
        0,
        1,
        2,
        3,
        4,
        5,
        7
      ],
      "identity_basis": "Same baseline specification defines this identical scoped entity/mechanism; differing labels/properties preserved in source_records.",
      "name": "Privacy and operational evidence",
      "exact_text": "Privacy and operational evidence\n\n- Treat account identifiers, release memberships, and security logs as personal data. Shared-library content restrictions are defined in FR-4.7 in [REQUIREMENTS.md](REQUIREMENTS.md). Local catalog and recovery files use owner-only permissions.\n- Log operation type, result, time, and correlation ID; exclude passwords, bearer tokens, invitation secrets, payload bodies, local paths, and complete libraries. Retain service security logs for 30 days and restrict access to operators. Alert on repeated authentication throttling (20 events in 5 minutes), failed deletion transactions, or certificate renewal failures through operator monitoring. Invitation-secret exclusion traces to [T-009](THREAT_MODEL.md#t-009).\n- The closed pilot uses no persistent service database backups (recommendation snapshot restrictions are defined in SC-004), so committed account/library deletion leaves no application-managed backup copy. Enable SQLite secure deletion and checkpoint/truncate WAL after deletion before reporting success; on checkpoint failure retry cleanup; user-visible status is defined in FR-4.22 in [REQUIREMENTS.md](REQUIREMENTS.md). This is logical application deletion, not a promise of forensic erasure on storage hardware. Do not enable provider snapshots without an adopted deletion/retention design. Local recovery retention is defined in FR-1.31 in [REQUIREMENTS.md](REQUIREMENTS.md).\n- Before public launch, the maintainer MUST record deployment jurisdiction, processing basis, user notice, retention/deletion handling, and dependency-license obligations in the release evidence. This gate does not assert a legal determination or waive obligations during the pilot.\n- Verification: payload/log inspection, timed retention cleanup, account/library deletion including WAL cleanup, local recovery retention, and a completed release review. Trace: [REQUIREMENTS.md](REQUIREMENTS.md) release scope, FR-1.31, FR-4.7–FR-4.9, FR-4.14.",
      "decision_ids": [],
      "threat_ids": [
        "T-009"
      ]
    },
    {
      "id": "C-SC-009",
      "specification_id": "SC-009",
      "name": "Recommendation inference protection",
      "exact_text": "Recommendation inference protection — ACTIVE\n\n- Enforce FR-3.20–FR-3.23 in the service domain before pagination. Compute exact ranking only over qualifying releases; prevent identity, candidate-support count and cohort-size disclosure in response bodies, cursor contents and errors. Present only the required generic aggregate reason. Existing SC-001/SC-004/SC-008 and FR-4.10 remain mandatory.\n- Limit each account to two admitted library replacements in any rolling 24 hours and five admitted recommendation queries in any rolling hour. Count admission atomically before calculation or mutation; rejected validation/authentication attempts remain subject to SC-001. Each cursor chain belongs to one admitted query; its page requests do not consume further query admissions, but all page requests remain subject to SC-001's authenticated-request limit. A fresh query after revision invalidation consumes a new admission. Preserve withdrawal and account deletion access; they are not library replacements. Rate-limit failure and explicit-retry behavior follow FR-4.24–FR-4.25 and FR-4.32 in REQUIREMENTS.md.\n- Do not claim that cohort thresholds, omitted counts or invitations provide anonymity or eliminate inference. Prior knowledge, collusion and comparisons over time remain residual threats. Release requires adversarial tests for fewer-than-required cohorts/contributors, contributor removal at thresholds, repeated replacements, colluding invited accounts, cross-page revision changes, and differential outputs. Verify that the specified minimums, output restrictions and limits hold and that tested recommendation functions do not disclose identities or complete libraries contrary to FR-4.10. A demonstrated violation blocks service release; record test limitations and remaining inference risk in release evidence.\n- Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-010"
      ],
      "threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "C-SC-010",
      "specification_id": "SC-010",
      "name": "Pilot enrollment and registration admission",
      "exact_text": "Pilot enrollment and registration admission — ACTIVE\n\n- Implement FR-4.29 through the local operator provisioning path described in ARCHITECTURE.md. Generate invitation secrets from 32 cryptographically random bytes, store only their SHA-256 digests, and expire unused invitations seven days after generation. Do not log secrets or place them in URLs. No service Admin invitation API is introduced.\n- Validate invitation validity and registration admission before password hashing. Limit registration attempts to three per rolling hour per source IP and 30 per rolling hour service-wide, counting failed invitations as attempts. Enforce both counters atomically. Return generic invalid-invitation rejection without indicating whether a secret was used, expired or unknown; use existing FR-4.24 responses for rate/capacity rejection.\n- Recheck invitation validity, account capacity and canonical name uniqueness when committing account creation; consume the invitation in the same transaction. Failed creation must not leave a partial account or consume the invitation. Preserve the 100-account cap and existing sign-in/authenticated limits.\n- Rate counters used by SC-001, SC-009 and SC-010 MUST remain effective across service restarts, retain only the minimum enforcement identity/key, count and window state, and expire when their limiting windows end. Account-deletion cleanup under SC-008 remains required. Verify restart behavior and expiry as well as atomic admission.\n- Verify invalid, expired and replayed invitations, concurrent redemption, capacity and counter boundaries, transaction rollback, and rejection before hashing. Threats: [T-005](THREAT_MODEL.md#t-005), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-011",
        "DEC-OD-012"
      ],
      "threat_ids": [
        "T-005",
        "T-009",
        "T-017"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "C-SC-011",
      "specification_id": "SC-011",
      "name": "Complete resource budgets",
      "exact_text": "Complete resource budgets — ACTIVE\n\n- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.\n- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.\n- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.\n- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.\n- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-013",
        "DEC-OD-014"
      ],
      "threat_ids": [
        "T-003",
        "T-005",
        "T-017",
        "T-021",
        "T-025"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "C-SC-012",
      "specification_id": "SC-012",
      "name": "Consistent account-name identity",
      "exact_text": "Consistent account-name identity — ACTIVE\n\nApply FR-4.30's accepted spelling and lowercase canonical identity consistently to registration uniqueness, sign-in lookup and the normalized-username throttle required by SC-001. Enforce canonical uniqueness transactionally. Reject invalid spellings rather than silently removing characters. Verify case variants cannot obtain separate throttle identities or ambiguous account ownership, including concurrent registration. This policy does not normalize, truncate or restrict passwords beyond FR-4.17. Threats: [T-001](THREAT_MODEL.md#t-001), [T-009](THREAT_MODEL.md#t-009).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-015"
      ],
      "threat_ids": [
        "T-001",
        "T-009"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "C-SC-013",
      "specification_id": "SC-013",
      "name": "Recovery-before-restore policy",
      "exact_text": "Recovery-before-restore policy — ACTIVE\n\nImplement FR-1.46 through the existing SC-003 sequence: verify the selected recovery copy and current destination identity, create and flush a complete integrity-recorded recovery copy of the destination, then perform verified replacement and catalog reconciliation. Failure before replacement leaves the destination unchanged; retain the selected and newly created recovery copies until explicit deletion under FR-1.31. Preserve renewed review, source-change rejection, owner-only permissions, atomic replacement, operation-state persistence and FR-1.44 integrity failure behavior. Verify disk-full/copy failures, changed sources, corrupted copies and interruption before/after replacement; do not report restoration complete until reconciliation. Threat: [T-020](THREAT_MODEL.md#t-020).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-016"
      ],
      "threat_ids": [
        "T-020"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "C-SC-014",
      "specification_id": "SC-014",
      "name": "Service recovery objectives",
      "exact_text": "Service recovery objectives — ACTIVE\n\nImplement FR-4.31's best-effort empty-service reprovisioning after loss of the single service store. Do not introduce snapshots or persistent database backups prohibited by SC-008. Reprovision host restrictions, TLS, initial Admin and invitation generation before renewed enrollment; lost sessions are invalid and previous memberships cannot be reconstructed from logs. Record a store-loss recovery exercise and clean migration/rollback evidence before pilot release. Recovery must not revive deleted memberships or silently resubmit desktop libraries. No data-recovery guarantee or recovery-time deadline is promised. Threat: [T-025](THREAT_MODEL.md#t-025).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-017"
      ],
      "threat_ids": [
        "T-025"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "C-SC-015",
      "specification_id": "SC-015",
      "name": "Privacy release-context evidence",
      "exact_text": "Privacy release-context evidence — ACTIVE\n\n- Verify the prospective pilot hosting location defined in ARCHITECTURE.md and the participant eligibility defined in FR-4.34 before pilot collection. Record the actual deployment and eligibility evidence; the adopted scope is not proof that a host or participants already exist. The operator's invitation workflow must confirm eligibility without collecting identity-document copies or adding service profile fields.\n- Adopt a processing plan of consent for voluntary library sharing, contractual necessity for account/service operation, and legitimate interests for the limited security logging in SC-008. These are intended bases for review, not established legal conclusions. Before any pilot personal-data collection, the maintainer must record the applicable review and evidence substantiating each operation's basis, scope, necessity, and applicable safeguards; record the logging interest/balancing assessment and consent/withdrawal design. If the review does not substantiate the plan, collection and pilot release must not begin; a reviewed specification amendment is required before using another plan.\n- Before enrollment, publish a notice with the actual operator identity/contact, processing purposes and data categories, intended bases, recipients/external services, account/library deletion, 30-day security-log retention, no persistent service backups, recommendation inference risks, applicable rights/contact route and withdrawal process. Explain that sharing withdrawal ends sharing, account deletion ends account operation, and the disclosed security-log retention is governed separately under the reviewed logging basis. Show external lookup disclosure under FR-3.18. The actual notice and review records are release evidence, not invented contents in this specification.\n- Verify notice delivery and the specified consent, withdrawal, deletion and retention behavior before pilot release. Preserve SC-008's broader public-launch review, including dependency-license obligations. Required evidence is outstanding; no compliance, anonymity or implemented-control claim follows from this ACTIVE rule. Threats: [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012).",
      "status": "ACTIVE adopted specification; unimplemented and unverified",
      "decision_ids": [
        "DEC-OD-018",
        "DEC-OD-019"
      ],
      "threat_ids": [
        "T-010",
        "T-011",
        "T-012"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    }
  ],
  "requirements": [
    {
      "id": "S07-R01",
      "source": "REQUIREMENTS.md FR-1.1–FR-4.27 and NFR-1.1–NFR-3.1",
      "authority": "project specification",
      "edition": "not supplied",
      "status": "required product behavior; unverified",
      "applicability": "first release local native desktop and closed recommendation pilot",
      "evidence_ids": [
        "S07-E01"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-R02",
      "source": "DESIGN.md Layout, Components and Presentation constraints",
      "authority": "project specification",
      "edition": "alpha",
      "status": "acceptance targets; untested",
      "applicability": "native UI keyboard, scaling and plain-text rendering",
      "evidence_ids": [
        "S07-E04"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "REQ-FR-1.44",
      "specification_id": "FR-1.44",
      "exact_text": "The system MUST reject restoration when the selected recovery copy fails the integrity check defined in SC-003 in [SECURITY.md](SECURITY.md), leave the destination unchanged, and show a per-file failure.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-020"
      ],
      "flow_ids": [
        "S00-F2"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-1.44-1",
          "exact_text": "A modified retained recovery copy causes a per-file failure and no destination write; an intact copy still follows FR-1.32 and FR-1.37–FR-1.42.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-1.45",
      "specification_id": "FR-1.45",
      "exact_text": "The system MUST reject a file whose metadata processing exceeds the limits in SC-011 in [SECURITY.md](SECURITY.md), leave the source unchanged, show a per-file error, and continue processing other files without silently truncating metadata.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-003",
        "T-005",
        "T-021"
      ],
      "flow_ids": [
        "POST-F01"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-1.45-4",
          "exact_text": "Exercise every processing/response limit at and beyond its bound: failure leaves source files unchanged, continues other file work, and never silently truncates results.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-1.46",
      "specification_id": "FR-1.46",
      "exact_text": "Before restoration overwrites the current destination, the system MUST create and verify a complete recovery copy of that destination; failure MUST cancel restoration. All recovery copies remain subject to FR-1.31.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-020"
      ],
      "flow_ids": [
        "S00-F2"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-1.46-5",
          "exact_text": "Restoration creates a verified copy of the current destination before mutation; disk-full/copy failure cancels restoration and retains earlier copies.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.2",
      "specification_id": "FR-3.2",
      "exact_text": "The system MUST show new-release recommendations from other participating users whose shared libraries have at least one release in common with the current user's shared library, subject to the privacy eligibility rules FR-3.20–FR-3.23.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.2-6",
          "exact_text": "Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.18",
      "specification_id": "FR-3.18",
      "exact_text": "Before an external lookup or purchase-search action sends data, the system MUST identify the receiving service and the search terms or release identifiers being sent, and explain that recommendation sharing being disabled does not disable these user-requested disclosures. This is informational context for the initiating workflow, not an additional confirmation gate for each lookup request.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-011"
      ],
      "flow_ids": [
        "S00-F3",
        "S00-F5"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.18-2",
          "exact_text": "Before MusicBrainz lookup and Bandcamp handoff, the recipient and outgoing terms/identifiers are available with sharing both enabled and disabled.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.19",
      "specification_id": "FR-3.19",
      "exact_text": "The system MUST discard an incomplete recommendation result when its membership revision is invalidated and require the fresh query in FR-3.16 before displaying a completed ranking.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-015",
        "T-023"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.19-3",
          "exact_text": "Invalidate a revision between pages: no mixed or partial ranking is displayed; the fresh query uses current eligibility.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.20",
      "specification_id": "FR-3.20",
      "exact_text": "The system MUST return shared-library recommendations only when at least five other eligible submitted libraries overlap the requester's submitted library. Withdrawn, suspended and requester-owned libraries MUST NOT count toward this minimum.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.20-6",
          "exact_text": "Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.21",
      "specification_id": "FR-3.21",
      "exact_text": "A recommended release MUST occur in at least three of those eligible other libraries. The system MUST apply this privacy eligibility rule before ranking qualifying releases exactly as FR-3.3 requires; FR-3.12–FR-3.13 still apply.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.21-6",
          "exact_text": "Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.22",
      "specification_id": "FR-3.22",
      "exact_text": "The API and desktop MUST NOT expose numerical contributor counts, contributing identities, or individual libraries with recommendations. The desktop MUST use a generic aggregate reason, such as Recommended from shared libraries. Internal counts remain necessary for FR-3.3.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.22-6",
          "exact_text": "Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.23",
      "specification_id": "FR-3.23",
      "exact_text": "When privacy eligibility leaves no recommendations, the system MUST explain that there is insufficient shared information to show recommendations while protecting participants, without revealing cohort sizes or suppressed releases.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-004",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.23-6",
          "exact_text": "Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-3.24",
      "specification_id": "FR-3.24",
      "exact_text": "The system MUST reject an external response that exceeds SC-011 limits, show request-failure feedback with an explicit retry action, and never present truncated data as a complete result.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-005",
        "T-021"
      ],
      "flow_ids": [
        "S00-F3"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-3.24-4",
          "exact_text": "Exercise every processing/response limit at and beyond its bound: failure leaves source files unchanged, continues other file work, and never silently truncates results.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.28",
      "specification_id": "FR-4.28",
      "exact_text": "The system MUST disclose before sharing that recommendations can reveal patterns about shared music despite privacy safeguards; it MUST NOT promise anonymity or protection from every inference. FR-4.10 remains required and service release requires SC-009 verification.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-004",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.28-6",
          "exact_text": "Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.29",
      "specification_id": "FR-4.29",
      "exact_text": "Account registration MUST require a valid, unused, unexpired invitation token provisioned by the pilot operator. The service MUST consume it atomically with account creation; invalid invitations MUST receive generic rejection without creating an account.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-009",
        "T-017"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.29-7",
          "exact_text": "Reject expired/reused invitations and racing reuse without partial accounts; equivalent username case shares uniqueness and throttle identity; every admission limit returns the defined failure.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.30",
      "specification_id": "FR-4.30",
      "exact_text": "Usernames MUST contain 3–32 ASCII letters, digits, or underscores. The service MUST use ASCII lowercase as the canonical account identity for uniqueness, sign-in and throttling. FR-4.17 password handling is unchanged.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-001",
        "T-009"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.30-7",
          "exact_text": "Reject expired/reused invitations and racing reuse without partial accounts; equivalent username case shares uniqueness and throttle identity; every admission limit returns the defined failure.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.31",
      "specification_id": "FR-4.31",
      "exact_text": "If the pilot service store is lost, the service MUST report unavailability until the operator reprovisions an empty service. Returning users MUST register with new invitations and explicitly resubmit libraries. The pilot promises neither recovery of lost service data nor a recovery deadline; local files and local workflows remain independent.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-025"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.31-8",
          "exact_text": "Simulate store loss: unavailable service, empty reprovisioning, new invitations and explicit resubmission; no automatic sharing or change to local music.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.32",
      "specification_id": "FR-4.32",
      "exact_text": "The system MUST report endpoint-specific admission and privacy rate limits using FR-4.24 and require an explicit user retry after rate limiting, including recommendation queries; no automatic rate-limit retry is permitted. FR-4.25 continues to govern all mutations. Numeric limits are owned by SC-009–SC-011 in [SECURITY.md](SECURITY.md).",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-005",
        "T-009",
        "T-017"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.32-7",
          "exact_text": "Reject expired/reused invitations and racing reuse without partial accounts; equivalent username case shares uniqueness and throttle identity; every admission limit returns the defined failure.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.33",
      "specification_id": "FR-4.33",
      "exact_text": "Before registration and before enabling sharing, the system MUST present the service notice required by SC-015 in [SECURITY.md](SECURITY.md). Sharing consent MUST remain separate, explicit and disabled by default.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-010",
        "T-011",
        "T-012"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.33-9",
          "exact_text": "Notice and separate sharing consent appear before the applicable action; eligibility is checked before invitations; required release evidence is present before pilot data collection.",
          "status": "required future check; not executed"
        }
      ]
    },
    {
      "id": "REQ-FR-4.34",
      "specification_id": "FR-4.34",
      "exact_text": "The closed pilot MUST admit only participants aged 18 or older and resident in the EEA through operator-controlled invitations. The operator MUST determine eligibility before issuing invitations; the application MUST NOT introduce additional identity-document collection. This is the adopted pilot scope, not a statement that any participant has been verified.",
      "authority": "project REQUIREMENTS.md",
      "edition": "final resolution source hash in POST-E01",
      "status": "adopted; future verification required",
      "applicability": "first-release native desktop and closed pilot",
      "evidence_ids": [
        "POST-E01"
      ],
      "threat_ids": [
        "T-009",
        "T-010"
      ],
      "flow_ids": [
        "S00-F4"
      ],
      "acceptance_criteria": [
        {
          "id": "AC-FR-4.34-9",
          "exact_text": "Notice and separate sharing consent appear before the applicable action; eligibility is checked before invitations; required release evidence is present before pilot data collection.",
          "status": "required future check; not executed"
        }
      ]
    }
  ],
  "risks": [
    {
      "id": "S04-R1",
      "threat_ids": [
        "T-019"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-R2",
      "threat_ids": [
        "T-020"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-R3",
      "threat_ids": [
        "T-021"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-R4",
      "threat_ids": [
        "T-022"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-R5",
      "threat_ids": [
        "T-023"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-R6",
      "threat_ids": [
        "T-024"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-R7",
      "threat_ids": [
        "T-025"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists.",
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    }
  ],
  "attack_trees": [
    {
      "id": "S03-AT1",
      "root_id": "S03-N10",
      "nodes": [
        {
          "id": "S03-N10",
          "name": "Unauthorized music-file change",
          "operator": "AND",
          "children": [
            "S03-N11",
            "S03-N12"
          ],
          "affected_ids": [
            "S00-A1"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-002",
            "C-SC-003"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N11",
          "name": "Attacker-controlled input reaches a selected file or review proposal",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S00-A1"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-002",
            "C-SC-003"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        },
        {
          "id": "S03-N12",
          "name": "Approval binding, identity checking, or mandatory write sequence fails",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S00-A1"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-002",
            "C-SC-003"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-AT2",
      "root_id": "S03-N20",
      "nodes": [
        {
          "id": "S03-N20",
          "name": "Unauthorized account or shared-library change",
          "operator": "AND",
          "children": [
            "S03-N21",
            "S03-N22"
          ],
          "affected_ids": [
            "S00-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-001",
            "C-SC-005",
            "C-SC-006"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N21",
          "name": "Unauthenticated, non-owner, suspended or non-Admin request reaches a service operation",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S00-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-001",
            "C-SC-005",
            "C-SC-006"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        },
        {
          "id": "S03-N22",
          "name": "Authentication or domain authorization fails",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S00-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-001",
            "C-SC-005",
            "C-SC-006"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-AT3",
      "root_id": "S03-N30",
      "nodes": [
        {
          "id": "S03-N30",
          "name": "Disclosure of a withdrawn or suspended library through a stale result",
          "operator": "AND",
          "children": [
            "S03-N31",
            "S03-N32"
          ],
          "affected_ids": [
            "S03-A4"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-004",
            "C-SC-005"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N31",
          "name": "Membership eligibility changes during paginated calculation",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A4"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-004",
            "C-SC-005"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        },
        {
          "id": "S03-N32",
          "name": "Cursor revision or per-page eligibility checks fail",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A4"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-004",
            "C-SC-005"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-AT4",
      "root_id": "S03-N40",
      "nodes": [
        {
          "id": "S03-N40",
          "name": "Unconfirmed library disclosure",
          "operator": "OR",
          "children": [
            "S03-N41",
            "S03-N42"
          ],
          "affected_ids": [
            "S00-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-004"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N41",
          "name": "Previewed set changes before submission without renewed confirmation",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S00-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-004"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        },
        {
          "id": "S03-N42",
          "name": "A retry or background action submits unconfirmed local changes",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S00-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-004"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-AT5",
      "root_id": "S03-N50",
      "nodes": [
        {
          "id": "S03-N50",
          "name": "Service exhaustion prevents recommendation access",
          "operator": "OR",
          "children": [
            "S03-N51",
            "S03-N52"
          ],
          "affected_ids": [
            "S03-A6"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-001",
            "C-SC-007"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N51",
          "name": "Request, queue or capacity bounds fail",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A6"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-001",
            "C-SC-007"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        },
        {
          "id": "S03-N52",
          "name": "Expensive unauthenticated registration work is admitted without an evidenced admission budget",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A6"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-001",
            "C-SC-007"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-AT6",
      "root_id": "S03-N60",
      "nodes": [
        {
          "id": "S03-N60",
          "name": "Hostile content controls native rendering or browser handoff",
          "operator": "OR",
          "children": [
            "S03-N61",
            "S03-N62"
          ],
          "affected_ids": [
            "S03-A5"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-002"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N61",
          "name": "Imported or returned metadata is interpreted rather than displayed as text",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A5"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-002"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        },
        {
          "id": "S03-N62",
          "name": "Untrusted metadata supplies an executable URL or shell command to link opening",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A5"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "C-SC-002"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    }
  ],
  "attack_paths": [
    {
      "id": "S01-AP1",
      "threat_id": "T-008",
      "steps": [
        "Participant submits a confirmed library",
        "Service computes eligible libraries by overlap",
        "Service returns ranked release identifiers/counts",
        "Caller may infer memberships where the eligible cohort is distinctive"
      ],
      "affected_ids": [
        "S00-D3",
        "S00-F4"
      ],
      "evidence_ids": [
        "S01-E1",
        "S01-E2"
      ],
      "control_ids": [
        "C-SC-001",
        "C-SC-004",
        "C-SC-008"
      ],
      "assumptions": [
        "Actual cohort distinguishability and adversarial prior knowledge are unobserved; the final inference is conditional."
      ],
      "risk_ids": [],
      "status": "design path, not executed",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S03-P1-1",
      "tree_id": "S03-AT1",
      "node_ids": [
        "S03-N10",
        "S03-N11",
        "S03-N12"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P2-1",
      "tree_id": "S03-AT2",
      "node_ids": [
        "S03-N20",
        "S03-N21",
        "S03-N22"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P3-1",
      "tree_id": "S03-AT3",
      "node_ids": [
        "S03-N30",
        "S03-N31",
        "S03-N32"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P4-1",
      "tree_id": "S03-AT4",
      "node_ids": [
        "S03-N40",
        "S03-N41"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P4-2",
      "tree_id": "S03-AT4",
      "node_ids": [
        "S03-N40",
        "S03-N42"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P5-1",
      "tree_id": "S03-AT5",
      "node_ids": [
        "S03-N50",
        "S03-N51"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P5-2",
      "tree_id": "S03-AT5",
      "node_ids": [
        "S03-N50",
        "S03-N52"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P6-1",
      "tree_id": "S03-AT6",
      "node_ids": [
        "S03-N60",
        "S03-N61"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S03-P6-2",
      "tree_id": "S03-AT6",
      "node_ids": [
        "S03-N60",
        "S03-N62"
      ],
      "status": "logically satisfiable conditional path; feasibility unknown",
      "method_id": "S03-M1",
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking.",
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    }
  ],
  "visualizations": [
    {
      "id": "S07-V01",
      "source": "ARCHITECTURE.md Data flow and trust boundaries",
      "type": "Mermaid flowchart",
      "status": "planned logical architecture; calls/access arrows with implicit response direction",
      "evidence_ids": [
        "S07-E02"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "D09-01",
      "title": "System Context",
      "purpose": "Show local editing and remote discovery/sharing context",
      "audience": "Product and security reviewers",
      "view": "System Context",
      "model_record_ids": [
        "S08-SCOPE",
        "S00-U1",
        "S00-U2",
        "S00-U3",
        "S00-U4",
        "S07-ACT05",
        "S07-A10",
        "S07-A11",
        "S00-F1",
        "S00-F4",
        "S00-F3",
        "S00-F5"
      ],
      "specification": {
        "elements": [
          {
            "model_id": "S08-SCOPE",
            "label": "Tag Zeppelin",
            "kind": "system",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U1",
            "label": "Current desktop user",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U2",
            "label": "Participating service user",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U3",
            "label": "Recommendation-service Admin",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U4",
            "label": "Operator",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-ACT05",
            "label": "Project maintainer",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A10",
            "label": "MusicBrainz",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A11",
            "label": "OS browser/Bandcamp",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          }
        ],
        "connections": [
          {
            "id": "D09-CTX-S00-U1",
            "source_id": "S00-U1",
            "destination_id": "S08-SCOPE",
            "direction": "request and result",
            "label": "Native interaction: local collection/review",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [],
            "control_ids": []
          },
          {
            "id": "D09-CTX-S00-U2",
            "source_id": "S00-U2",
            "destination_id": "S08-SCOPE",
            "direction": "request and result",
            "label": "HTTPS JSON through native client: account and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [
              "S00-B3"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [],
            "control_ids": []
          },
          {
            "id": "D09-CTX-S00-U3",
            "source_id": "S00-U3",
            "destination_id": "S08-SCOPE",
            "direction": "request and result",
            "label": "HTTPS JSON: Admin suspension/restoration",
            "data_sensitivity": "personal data",
            "boundary_ids": [
              "S00-B3"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [],
            "control_ids": []
          },
          {
            "id": "D09-CTX-S07-A10",
            "source_id": "S08-SCOPE",
            "destination_id": "S07-A10",
            "direction": "outbound with response as applicable",
            "label": "HTTPS: metadata search terms/identifiers and response",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-011"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ]
          },
          {
            "id": "D09-CTX-S07-A11",
            "source_id": "S08-SCOPE",
            "destination_id": "S07-A11",
            "direction": "outbound with response as applicable",
            "label": "OS browser handoff: HTTPS purchase query",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F5"
            ],
            "threat_ids": [
              "T-011"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ]
          }
        ],
        "boundary_groups": [
          {
            "id": "S00-B1",
            "label": "Filesystem to desktop media adapter",
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B2",
            "label": "Desktop to external services",
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B3",
            "label": "Desktop to authenticated recommendation API",
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B4",
            "label": "API handler to service domain authorization",
            "control_ids": [
              "C-SC-006"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "POST-B01",
            "label": "Desktop media adapter to restricted helper process",
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-011"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "ACTIVE adopted limits and isolation, not verified"
          }
        ],
        "ordering_constraints": [
          "Actors on left; native desktop then API/domain then service store; external integrations on separate right branch.",
          "Group internal logical components without implying additional deployment.",
          "Threat IDs appear outside component labels."
        ],
        "legend": {
          "arrow": "documented call/data direction; return to caller where stated",
          "dashed_border": "trust boundary; ordinary grouping has a labeled plain border",
          "neutral_T_marker": "unrated design threat; no severity color or order",
          "control": "adopted planned control, not verified; ACTIVE is specification status only",
          "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"
        },
        "threat_legend": {},
        "annotations": [
          "All controls are specification plans. No observed implementation or verified mitigation.",
          "OD-010–OD-019 are resolved; SC-001–SC-015 are ACTIVE adopted specifications. Required implementation, workload, privacy-review and release evidence remains pending.",
          "Operator and maintainer responsibilities are evidenced; their concrete operational communication protocols are unspecified and no edges are invented."
        ],
        "text_preview": "S00-U1 → S08-SCOPE [Native interaction: local collection/review]; S00-U2 → S08-SCOPE [HTTPS JSON through native client: account and memberships]; S00-U3 → S08-SCOPE [HTTPS JSON: Admin suspension/restoration]; S08-SCOPE → S07-A10 [HTTPS: metadata search terms/identifiers and response]; S08-SCOPE → S07-A11 [OS browser handoff: HTTPS purchase query]"
      },
      "omissions": [
        "Exact endpoint methods/paths and runtime topology are not evidenced.",
        "Local protocols beyond stated ports/adapters are not assigned wire protocols.",
        "No universal sensitivity class or risk score is invented.",
        "Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge."
      ],
      "validation_notes": [
        "Model IDs and flow references checked against stage08; not rendered."
      ]
    },
    {
      "id": "D09-02",
      "title": "Container and Component Architecture",
      "purpose": "Show logical modules, stores and enforcement placement",
      "audience": "Developers and architecture reviewers",
      "view": "Container/Component",
      "model_record_ids": [
        "S00-U1",
        "S00-U4",
        "S03-A5",
        "S07-A02",
        "S07-A03",
        "S07-A04",
        "S00-A2",
        "S00-A1",
        "S07-A12",
        "S07-A05",
        "S07-A06",
        "S00-A3",
        "S07-A10",
        "S07-A11",
        "POST-A01",
        "S00-F1",
        "S00-F2",
        "S00-F3",
        "S00-F5",
        "S00-F4",
        "POST-F01",
        "POST-F02"
      ],
      "specification": {
        "elements": [
          {
            "model_id": "S00-U1",
            "label": "Current desktop user",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U4",
            "label": "Operator",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S03-A5",
            "label": "Desktop presentation",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "Qt 6.8 Widgets, C++17",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A02",
            "label": "Local application/domain services",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A03",
            "label": "Persistence/media adapters",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "TagLib 2.x adapter with restricted media helper; filesystem and SQLite adapters",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A04",
            "label": "Desktop discovery/sharing adapters",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-A2",
            "label": "Local catalog, proposals, approvals and operation state",
            "kind": "data store",
            "zone": "S00-Z1",
            "technology": "SQLite 3.x local catalog",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-A1",
            "label": "Music files and recovery copies",
            "kind": "data store",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A12",
            "label": "Fastify API",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "Node.js 24 LTS, Fastify 5, JavaScript ES2022",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A05",
            "label": "Service account/sharing domain",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A06",
            "label": "Recommendation calculation",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-A3",
            "label": "Service accounts, sessions and release memberships",
            "kind": "data store",
            "zone": "S00-Z3",
            "technology": "SQLite 3.x service store",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A10",
            "label": "MusicBrainz",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A11",
            "label": "OS browser/Bandcamp",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "POST-A01",
            "label": "Restricted local media helper",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "Child process behind media adapter; TagLib 2.x media parsing/transformation",
            "threat_ids": [],
            "control_ids": []
          }
        ],
        "connections": [
          {
            "id": "D09-C01",
            "source_id": "S00-U1",
            "destination_id": "S03-A5",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Native interaction: selected files, fields and decisions",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [
              "T-002",
              "T-003"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C02",
            "source_id": "S03-A5",
            "destination_id": "S07-A02",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Application-service contracts: review/save/restore",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C03",
            "source_id": "S07-A02",
            "destination_id": "S07-A03",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Abstract media/filesystem ports: bound approved changes",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C04",
            "source_id": "S07-A03",
            "destination_id": "S00-A1",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Filesystem access: music and recovery contents",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B1"
            ],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C05",
            "source_id": "S07-A03",
            "destination_id": "S00-A2",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "SQLite adapter: catalog/review/recovery state",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [
              "T-002",
              "T-019"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C06",
            "source_id": "S07-A02",
            "destination_id": "S07-A04",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Network ports: discovery and sharing requests",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-011",
              "T-016",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C07",
            "source_id": "S07-A04",
            "destination_id": "S07-A10",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "HTTPS: search terms / release identifiers and metadata",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-003",
              "T-005",
              "T-011",
              "T-021",
              "T-024"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C08",
            "source_id": "S07-A04",
            "destination_id": "S07-A11",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "OS browser handoff, generated HTTPS purchase search URL",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F5"
            ],
            "threat_ids": [
              "T-011",
              "T-018"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C09",
            "source_id": "S07-A04",
            "destination_id": "S07-A12",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages",
            "data_sensitivity": "account/membership data is personal data",
            "boundary_ids": [
              "S00-B3"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-004",
              "T-005",
              "T-006",
              "T-008",
              "T-009",
              "T-010",
              "T-012",
              "T-014",
              "T-015",
              "T-016",
              "T-017",
              "T-022",
              "T-023"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C10",
            "source_id": "S07-A12",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "In-process domain invocation: authenticated account/library operation",
            "data_sensitivity": "personal data",
            "boundary_ids": [
              "S00-B4"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-016",
              "T-022"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C11",
            "source_id": "S07-A05",
            "destination_id": "S00-A3",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "SQLite adapter: accounts, sessions and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-022"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C12",
            "source_id": "S07-A06",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Owner-defined read interfaces: eligibility and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-004",
              "T-008",
              "T-010",
              "T-015",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C13",
            "source_id": "S07-A12",
            "destination_id": "S07-A06",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "In-process domain invocation: recommendation calculation",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-004",
              "T-005",
              "T-008",
              "T-010",
              "T-015",
              "T-017",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C14",
            "source_id": "S07-A03",
            "destination_id": "POST-A01",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Bounded local process contract: selected input/staged file and operation data",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "POST-B01"
            ],
            "flow_ids": [
              "POST-F01"
            ],
            "threat_ids": [
              "T-003",
              "T-005",
              "T-021"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007"
            ]
          },
          {
            "id": "D09-C15",
            "source_id": "S00-U4",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Local operator command: issue invitations; concrete invocation syntax unspecified",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "POST-F02"
            ],
            "threat_ids": [
              "T-001",
              "T-009",
              "T-017"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007"
            ]
          }
        ],
        "boundary_groups": [
          {
            "id": "S00-B1",
            "label": "Filesystem to desktop media adapter",
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B2",
            "label": "Desktop to external services",
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B3",
            "label": "Desktop to authenticated recommendation API",
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B4",
            "label": "API handler to service domain authorization",
            "control_ids": [
              "C-SC-006"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "POST-B01",
            "label": "Desktop media adapter to restricted helper process",
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-011"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "ACTIVE adopted limits and isolation, not verified"
          }
        ],
        "ordering_constraints": [
          "Actors on left; native desktop then API/domain then service store; external integrations on separate right branch.",
          "Group internal logical components without implying additional deployment.",
          "Threat IDs appear outside component labels."
        ],
        "legend": {
          "arrow": "documented call/data direction; return to caller where stated",
          "dashed_border": "trust boundary; ordinary grouping has a labeled plain border",
          "neutral_T_marker": "unrated design threat; no severity color or order",
          "control": "adopted planned control, not verified; ACTIVE is specification status only",
          "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"
        },
        "threat_legend": {},
        "annotations": [
          "All controls are specification plans. No observed implementation or verified mitigation.",
          "OD-010–OD-019 are resolved; SC-001–SC-015 are ACTIVE adopted specifications. Required implementation, workload, privacy-review and release evidence remains pending."
        ],
        "text_preview": "S00-U1 → S03-A5 [Native interaction: selected files, fields and decisions]; S03-A5 → S07-A02 [Application-service contracts: review/save/restore]; S07-A02 → S07-A03 [Abstract media/filesystem ports: bound approved changes]; S07-A03 → S00-A1 [Filesystem access: music and recovery contents]; S07-A03 → S00-A2 [SQLite adapter: catalog/review/recovery state]; S07-A02 → S07-A04 [Network ports: discovery and sharing requests]; S07-A04 → S07-A10 [HTTPS: search terms / release identifiers and metadata]; S07-A04 → S07-A11 [OS browser handoff, generated HTTPS purchase search URL]; S07-A04 → S07-A12 [HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages]; S07-A12 → S07-A05 [In-process domain invocation: authenticated account/library operation]; S07-A05 → S00-A3 [SQLite adapter: accounts, sessions and memberships]; S07-A06 → S07-A05 [Owner-defined read interfaces: eligibility and memberships]; S07-A12 → S07-A06 [In-process domain invocation: recommendation calculation]; S07-A03 → POST-A01 [Bounded local process contract: selected input/staged file and operation data]; S00-U4 → S07-A05 [Local operator command: issue invitations; concrete invocation syntax unspecified]"
      },
      "omissions": [
        "Exact endpoint methods/paths and runtime topology are not evidenced.",
        "Local protocols beyond stated ports/adapters are not assigned wire protocols.",
        "No universal sensitivity class or risk score is invented.",
        "Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge."
      ],
      "validation_notes": [
        "Model IDs and flow references checked against stage08; not rendered."
      ]
    },
    {
      "id": "D09-03",
      "title": "Data Flow Diagram",
      "purpose": "Trace sensitive flows and trust crossings",
      "audience": "Security and privacy reviewers",
      "view": "Data Flow",
      "model_record_ids": [
        "S00-U1",
        "S00-U4",
        "S03-A5",
        "S07-A02",
        "S07-A03",
        "S07-A04",
        "S00-A2",
        "S00-A1",
        "S07-A12",
        "S07-A05",
        "S07-A06",
        "S00-A3",
        "S07-A10",
        "S07-A11",
        "POST-A01",
        "S00-F1",
        "S00-F2",
        "S00-F3",
        "S00-F5",
        "S00-F4",
        "POST-F01",
        "POST-F02"
      ],
      "specification": {
        "elements": [
          {
            "model_id": "S00-U1",
            "label": "Current desktop user",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U4",
            "label": "Operator",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S03-A5",
            "label": "Desktop presentation",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "Qt 6.8 Widgets, C++17",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A02",
            "label": "Local application/domain services",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A03",
            "label": "Persistence/media adapters",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "TagLib 2.x adapter with restricted media helper; filesystem and SQLite adapters",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A04",
            "label": "Desktop discovery/sharing adapters",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-A2",
            "label": "Local catalog, proposals, approvals and operation state",
            "kind": "data store",
            "zone": "S00-Z1",
            "technology": "SQLite 3.x local catalog",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-A1",
            "label": "Music files and recovery copies",
            "kind": "data store",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A12",
            "label": "Fastify API",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "Node.js 24 LTS, Fastify 5, JavaScript ES2022",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A05",
            "label": "Service account/sharing domain",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A06",
            "label": "Recommendation calculation",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-A3",
            "label": "Service accounts, sessions and release memberships",
            "kind": "data store",
            "zone": "S00-Z3",
            "technology": "SQLite 3.x service store",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A10",
            "label": "MusicBrainz",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S07-A11",
            "label": "OS browser/Bandcamp",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "POST-A01",
            "label": "Restricted local media helper",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "Child process behind media adapter; TagLib 2.x media parsing/transformation",
            "threat_ids": [],
            "control_ids": []
          }
        ],
        "connections": [
          {
            "id": "D09-C01",
            "source_id": "S00-U1",
            "destination_id": "S03-A5",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Native interaction: selected files, fields and decisions",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [
              "T-002",
              "T-003"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C02",
            "source_id": "S03-A5",
            "destination_id": "S07-A02",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Application-service contracts: review/save/restore",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C03",
            "source_id": "S07-A02",
            "destination_id": "S07-A03",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Abstract media/filesystem ports: bound approved changes",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C04",
            "source_id": "S07-A03",
            "destination_id": "S00-A1",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Filesystem access: music and recovery contents",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B1"
            ],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C05",
            "source_id": "S07-A03",
            "destination_id": "S00-A2",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "SQLite adapter: catalog/review/recovery state",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [
              "T-002",
              "T-019"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C06",
            "source_id": "S07-A02",
            "destination_id": "S07-A04",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Network ports: discovery and sharing requests",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-011",
              "T-016",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C07",
            "source_id": "S07-A04",
            "destination_id": "S07-A10",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "HTTPS: search terms / release identifiers and metadata",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-003",
              "T-005",
              "T-011",
              "T-021",
              "T-024"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C08",
            "source_id": "S07-A04",
            "destination_id": "S07-A11",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "OS browser handoff, generated HTTPS purchase search URL",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F5"
            ],
            "threat_ids": [
              "T-011",
              "T-018"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C09",
            "source_id": "S07-A04",
            "destination_id": "S07-A12",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages",
            "data_sensitivity": "account/membership data is personal data",
            "boundary_ids": [
              "S00-B3"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-004",
              "T-005",
              "T-006",
              "T-008",
              "T-009",
              "T-010",
              "T-012",
              "T-014",
              "T-015",
              "T-016",
              "T-017",
              "T-022",
              "T-023"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C10",
            "source_id": "S07-A12",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "In-process domain invocation: authenticated account/library operation",
            "data_sensitivity": "personal data",
            "boundary_ids": [
              "S00-B4"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-016",
              "T-022"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C11",
            "source_id": "S07-A05",
            "destination_id": "S00-A3",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "SQLite adapter: accounts, sessions and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-022"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C12",
            "source_id": "S07-A06",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Owner-defined read interfaces: eligibility and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-004",
              "T-008",
              "T-010",
              "T-015",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C13",
            "source_id": "S07-A12",
            "destination_id": "S07-A06",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "In-process domain invocation: recommendation calculation",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-004",
              "T-005",
              "T-008",
              "T-010",
              "T-015",
              "T-017",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C14",
            "source_id": "S07-A03",
            "destination_id": "POST-A01",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Bounded local process contract: selected input/staged file and operation data",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "POST-B01"
            ],
            "flow_ids": [
              "POST-F01"
            ],
            "threat_ids": [
              "T-003",
              "T-005",
              "T-021"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007"
            ]
          },
          {
            "id": "D09-C15",
            "source_id": "S00-U4",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Local operator command: issue invitations; concrete invocation syntax unspecified",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "POST-F02"
            ],
            "threat_ids": [
              "T-001",
              "T-009",
              "T-017"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007"
            ]
          }
        ],
        "boundary_groups": [
          {
            "id": "S00-B1",
            "label": "Filesystem to desktop media adapter",
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B2",
            "label": "Desktop to external services",
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B3",
            "label": "Desktop to authenticated recommendation API",
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B4",
            "label": "API handler to service domain authorization",
            "control_ids": [
              "C-SC-006"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "POST-B01",
            "label": "Desktop media adapter to restricted helper process",
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-011"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "ACTIVE adopted limits and isolation, not verified"
          }
        ],
        "ordering_constraints": [
          "Actors on left; native desktop then API/domain then service store; external integrations on separate right branch.",
          "Group internal logical components without implying additional deployment.",
          "Threat IDs appear outside component labels."
        ],
        "legend": {
          "arrow": "documented call/data direction; return to caller where stated",
          "dashed_border": "trust boundary; ordinary grouping has a labeled plain border",
          "neutral_T_marker": "unrated design threat; no severity color or order",
          "control": "adopted planned control, not verified; ACTIVE is specification status only",
          "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"
        },
        "threat_legend": {},
        "annotations": [
          "All controls are specification plans. No observed implementation or verified mitigation.",
          "OD-010–OD-019 are resolved; SC-001–SC-015 are ACTIVE adopted specifications. Required implementation, workload, privacy-review and release evidence remains pending."
        ],
        "text_preview": "S00-U1 → S03-A5 [Native interaction: selected files, fields and decisions]; S03-A5 → S07-A02 [Application-service contracts: review/save/restore]; S07-A02 → S07-A03 [Abstract media/filesystem ports: bound approved changes]; S07-A03 → S00-A1 [Filesystem access: music and recovery contents]; S07-A03 → S00-A2 [SQLite adapter: catalog/review/recovery state]; S07-A02 → S07-A04 [Network ports: discovery and sharing requests]; S07-A04 → S07-A10 [HTTPS: search terms / release identifiers and metadata]; S07-A04 → S07-A11 [OS browser handoff, generated HTTPS purchase search URL]; S07-A04 → S07-A12 [HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages]; S07-A12 → S07-A05 [In-process domain invocation: authenticated account/library operation]; S07-A05 → S00-A3 [SQLite adapter: accounts, sessions and memberships]; S07-A06 → S07-A05 [Owner-defined read interfaces: eligibility and memberships]; S07-A12 → S07-A06 [In-process domain invocation: recommendation calculation]; S07-A03 → POST-A01 [Bounded local process contract: selected input/staged file and operation data]; S00-U4 → S07-A05 [Local operator command: issue invitations; concrete invocation syntax unspecified]"
      },
      "omissions": [
        "Exact endpoint methods/paths and runtime topology are not evidenced.",
        "Local protocols beyond stated ports/adapters are not assigned wire protocols.",
        "No universal sensitivity class or risk score is invented.",
        "Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge."
      ],
      "validation_notes": [
        "Model IDs and flow references checked against stage08; not rendered."
      ]
    },
    {
      "id": "D09-04",
      "title": "Threat-Annotated Architecture",
      "purpose": "Locate all 25 unrated scenarios and planned controls",
      "audience": "Security reviewers",
      "view": "Threat-Annotated Architecture",
      "model_record_ids": [
        "S00-U1",
        "S00-U4",
        "S03-A5",
        "S07-A02",
        "S07-A03",
        "S07-A04",
        "S00-A2",
        "S00-A1",
        "S07-A12",
        "S07-A05",
        "S07-A06",
        "S00-A3",
        "S07-A10",
        "S07-A11",
        "POST-A01",
        "S00-F1",
        "S00-F2",
        "S00-F3",
        "S00-F5",
        "S00-F4",
        "POST-F01",
        "POST-F02"
      ],
      "specification": {
        "elements": [
          {
            "model_id": "S00-U1",
            "label": "Current desktop user",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S00-U4",
            "label": "Operator",
            "kind": "actor",
            "zone": "not further assigned by source",
            "technology": "not specified for this element",
            "threat_ids": [],
            "control_ids": []
          },
          {
            "model_id": "S03-A5",
            "label": "Desktop presentation",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "Qt 6.8 Widgets, C++17",
            "threat_ids": [
              "T-003",
              "T-011",
              "T-018",
              "T-021"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "model_id": "S07-A02",
            "label": "Local application/domain services",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-005"
            ]
          },
          {
            "model_id": "S07-A03",
            "label": "Persistence/media adapters",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "TagLib 2.x adapter with restricted media helper; filesystem and SQLite adapters",
            "threat_ids": [
              "T-002",
              "T-003",
              "T-013",
              "T-019",
              "T-020",
              "T-021"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "model_id": "S07-A04",
            "label": "Desktop discovery/sharing adapters",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-006",
              "T-011",
              "T-012",
              "T-015",
              "T-016",
              "T-023",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "model_id": "S00-A2",
            "label": "Local catalog, proposals, approvals and operation state",
            "kind": "data store",
            "zone": "S00-Z1",
            "technology": "SQLite 3.x local catalog",
            "threat_ids": [
              "T-002",
              "T-007",
              "T-019",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-005"
            ]
          },
          {
            "model_id": "S00-A1",
            "label": "Music files and recovery copies",
            "kind": "data store",
            "zone": "S00-Z1",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "model_id": "S07-A12",
            "label": "Fastify API",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "Node.js 24 LTS, Fastify 5, JavaScript ES2022",
            "threat_ids": [
              "T-001",
              "T-005",
              "T-009",
              "T-014",
              "T-017"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007"
            ]
          },
          {
            "model_id": "S07-A05",
            "label": "Service account/sharing domain",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-015",
              "T-016",
              "T-022",
              "T-023"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "model_id": "S07-A06",
            "label": "Recommendation calculation",
            "kind": "component",
            "zone": "S00-Z3",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-004",
              "T-005",
              "T-008",
              "T-010",
              "T-015",
              "T-017",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "model_id": "S00-A3",
            "label": "Service accounts, sessions and release memberships",
            "kind": "data store",
            "zone": "S00-Z3",
            "technology": "SQLite 3.x service store",
            "threat_ids": [
              "T-001",
              "T-004",
              "T-006",
              "T-008",
              "T-009",
              "T-010",
              "T-012",
              "T-014",
              "T-015",
              "T-016",
              "T-017",
              "T-022",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "model_id": "S07-A10",
            "label": "MusicBrainz",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-011",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "model_id": "S07-A11",
            "label": "OS browser/Bandcamp",
            "kind": "component",
            "zone": "S00-Z4",
            "technology": "not specified for this element",
            "threat_ids": [
              "T-011",
              "T-018"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "model_id": "POST-A01",
            "label": "Restricted local media helper",
            "kind": "component",
            "zone": "S00-Z1",
            "technology": "Child process behind media adapter; TagLib 2.x media parsing/transformation",
            "threat_ids": [
              "T-003",
              "T-005",
              "T-021"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007"
            ]
          }
        ],
        "connections": [
          {
            "id": "D09-C01",
            "source_id": "S00-U1",
            "destination_id": "S03-A5",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Native interaction: selected files, fields and decisions",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [
              "T-002",
              "T-003"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C02",
            "source_id": "S03-A5",
            "destination_id": "S07-A02",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Application-service contracts: review/save/restore",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C03",
            "source_id": "S07-A02",
            "destination_id": "S07-A03",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Abstract media/filesystem ports: bound approved changes",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C04",
            "source_id": "S07-A03",
            "destination_id": "S00-A1",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Filesystem access: music and recovery contents",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B1"
            ],
            "flow_ids": [
              "S00-F2"
            ],
            "threat_ids": [
              "T-002",
              "T-007",
              "T-013",
              "T-019",
              "T-020"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C05",
            "source_id": "S07-A03",
            "destination_id": "S00-A2",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "SQLite adapter: catalog/review/recovery state",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F1"
            ],
            "threat_ids": [
              "T-002",
              "T-019"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ]
          },
          {
            "id": "D09-C06",
            "source_id": "S07-A02",
            "destination_id": "S07-A04",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Network ports: discovery and sharing requests",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-011",
              "T-016",
              "T-024"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C07",
            "source_id": "S07-A04",
            "destination_id": "S07-A10",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "HTTPS: search terms / release identifiers and metadata",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F3"
            ],
            "threat_ids": [
              "T-003",
              "T-005",
              "T-011",
              "T-021",
              "T-024"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C08",
            "source_id": "S07-A04",
            "destination_id": "S07-A11",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "OS browser handoff, generated HTTPS purchase search URL",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "S00-B2"
            ],
            "flow_ids": [
              "S00-F5"
            ],
            "threat_ids": [
              "T-011",
              "T-018"
            ],
            "control_ids": [
              "C-SC-002",
              "C-SC-005",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C09",
            "source_id": "S07-A04",
            "destination_id": "S07-A12",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages",
            "data_sensitivity": "account/membership data is personal data",
            "boundary_ids": [
              "S00-B3"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-004",
              "T-005",
              "T-006",
              "T-008",
              "T-009",
              "T-010",
              "T-012",
              "T-014",
              "T-015",
              "T-016",
              "T-017",
              "T-022",
              "T-023"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C10",
            "source_id": "S07-A12",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "In-process domain invocation: authenticated account/library operation",
            "data_sensitivity": "personal data",
            "boundary_ids": [
              "S00-B4"
            ],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-016",
              "T-022"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C11",
            "source_id": "S07-A05",
            "destination_id": "S00-A3",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "SQLite adapter: accounts, sessions and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-001",
              "T-006",
              "T-012",
              "T-014",
              "T-022"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-006",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C12",
            "source_id": "S07-A06",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Owner-defined read interfaces: eligibility and memberships",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-004",
              "T-008",
              "T-010",
              "T-015",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C13",
            "source_id": "S07-A12",
            "destination_id": "S07-A06",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "In-process domain invocation: recommendation calculation",
            "data_sensitivity": "personal data",
            "boundary_ids": [],
            "flow_ids": [
              "S00-F4"
            ],
            "threat_ids": [
              "T-004",
              "T-005",
              "T-008",
              "T-010",
              "T-015",
              "T-017",
              "T-023",
              "T-025"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-004",
              "C-SC-005",
              "C-SC-007",
              "C-SC-008"
            ]
          },
          {
            "id": "D09-C14",
            "source_id": "S07-A03",
            "destination_id": "POST-A01",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Bounded local process contract: selected input/staged file and operation data",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [
              "POST-B01"
            ],
            "flow_ids": [
              "POST-F01"
            ],
            "threat_ids": [
              "T-003",
              "T-005",
              "T-021"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-007"
            ]
          },
          {
            "id": "D09-C15",
            "source_id": "S00-U4",
            "destination_id": "S07-A05",
            "direction": "source to destination; result returns to caller where applicable",
            "label": "Local operator command: issue invitations; concrete invocation syntax unspecified",
            "data_sensitivity": "not classified by source",
            "boundary_ids": [],
            "flow_ids": [
              "POST-F02"
            ],
            "threat_ids": [
              "T-001",
              "T-009",
              "T-017"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-005",
              "C-SC-006",
              "C-SC-007"
            ]
          }
        ],
        "boundary_groups": [
          {
            "id": "S00-B1",
            "label": "Filesystem to desktop media adapter",
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B2",
            "label": "Desktop to external services",
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B3",
            "label": "Desktop to authenticated recommendation API",
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B4",
            "label": "API handler to service domain authorization",
            "control_ids": [
              "C-SC-006"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "POST-B01",
            "label": "Desktop media adapter to restricted helper process",
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-011"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "ACTIVE adopted limits and isolation, not verified"
          }
        ],
        "ordering_constraints": [
          "Actors on left; native desktop then API/domain then service store; external integrations on separate right branch.",
          "Group internal logical components without implying additional deployment.",
          "Threat IDs appear outside component labels."
        ],
        "legend": {
          "arrow": "documented call/data direction; return to caller where stated",
          "dashed_border": "trust boundary; ordinary grouping has a labeled plain border",
          "neutral_T_marker": "unrated design threat; no severity color or order",
          "control": "adopted planned control, not verified; ACTIVE is specification status only",
          "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"
        },
        "threat_legend": {
          "T-001": "Unauthorized account or Admin operation",
          "T-002": "Unreviewed or destructive media mutation",
          "T-003": "Untrusted native input interpretation",
          "T-004": "Cross-user membership inference",
          "T-005": "Resource exhaustion at API and parser boundaries",
          "T-006": "Stale sharing or deletion results",
          "T-007": "Approved edits can lose integrity during interrupted file operations",
          "T-008": "Recommendation output can disclose participant memberships",
          "T-009": "Unauthenticated work can consume bounded pilot capacity",
          "T-010": "Linking or detecting memberships through overlap output",
          "T-011": "External lookup disclosure can be mistaken for sharing being disabled",
          "T-012": "Deletion or withdrawal can leave stale membership exposure",
          "T-013": "Unauthorized music-file change",
          "T-014": "Unauthorized account or shared-library change",
          "T-015": "Disclosure of a withdrawn or suspended library through a stale result",
          "T-016": "Unconfirmed library disclosure",
          "T-017": "Service exhaustion prevents recommendation access",
          "T-018": "Hostile content controls native rendering or browser handoff",
          "T-019": "Approval, original file or catalog diverges during interrupted write",
          "T-020": "Copy or destination has changed since it was recorded/reviewed",
          "T-021": "Malformed input exhausts resources or cannot be interpreted safely",
          "T-022": "Deletion commits but WAL cleanup fails",
          "T-023": "Eligibility changes between pages",
          "T-024": "Credential store, certificate or metadata endpoint unavailable",
          "T-025": "Single service store unavailable or bounded workload misses target"
        },
        "annotations": [
          "All controls are specification plans. No observed implementation or verified mitigation.",
          "OD-010–OD-019 are resolved; SC-001–SC-015 are ACTIVE adopted specifications. Required implementation, workload, privacy-review and release evidence remains pending."
        ],
        "text_preview": "S00-U1 → S03-A5 [Native interaction: selected files, fields and decisions]; S03-A5 → S07-A02 [Application-service contracts: review/save/restore]; S07-A02 → S07-A03 [Abstract media/filesystem ports: bound approved changes]; S07-A03 → S00-A1 [Filesystem access: music and recovery contents]; S07-A03 → S00-A2 [SQLite adapter: catalog/review/recovery state]; S07-A02 → S07-A04 [Network ports: discovery and sharing requests]; S07-A04 → S07-A10 [HTTPS: search terms / release identifiers and metadata]; S07-A04 → S07-A11 [OS browser handoff, generated HTTPS purchase search URL]; S07-A04 → S07-A12 [HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages]; S07-A12 → S07-A05 [In-process domain invocation: authenticated account/library operation]; S07-A05 → S00-A3 [SQLite adapter: accounts, sessions and memberships]; S07-A06 → S07-A05 [Owner-defined read interfaces: eligibility and memberships]; S07-A12 → S07-A06 [In-process domain invocation: recommendation calculation]; S07-A03 → POST-A01 [Bounded local process contract: selected input/staged file and operation data]; S00-U4 → S07-A05 [Local operator command: issue invitations; concrete invocation syntax unspecified]"
      },
      "omissions": [
        "Exact endpoint methods/paths and runtime topology are not evidenced.",
        "Local protocols beyond stated ports/adapters are not assigned wire protocols.",
        "No universal sensitivity class or risk score is invented.",
        "Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge."
      ],
      "validation_notes": [
        "Model IDs and flow references checked against stage08; not rendered."
      ]
    },
    {
      "id": "D09-05",
      "title": "Attack Surface Map",
      "purpose": "Enumerate every documented entry surface and policy",
      "audience": "Security and API reviewers",
      "view": "Attack Surface",
      "model_record_ids": [
        "S00-P1",
        "S00-P2",
        "S00-P3",
        "S00-P4",
        "S00-P5",
        "S07-EP02",
        "S07-EP03",
        "S07-EP04",
        "POST-EP01"
      ],
      "specification": {
        "elements": [
          {
            "model_id": "S00-P1",
            "label": "Selected media, folders and JPEG/PNG cover art",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [
              "T-002",
              "T-003",
              "T-005"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "No service account required for local/MusicBrainz functions",
            "authorization": "Current user-selected local scope; explicit approval required for writes",
            "threat_count": 3,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S00-P2",
            "label": "MusicBrainz responses and native metadata rendering",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [
              "T-003",
              "T-005",
              "T-011"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "No service account required for local/MusicBrainz functions",
            "authorization": "Current user-selected local scope; explicit approval required for writes",
            "threat_count": 3,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S00-P3",
            "label": "Public registration and sign-in HTTPS JSON",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [
              "T-001",
              "T-005",
              "T-009"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "Registration and sign-in precede established session; registration requires valid invitation",
            "authorization": "No client-selected roles; valid operator invitation and SC-010 admission precede hashing",
            "threat_count": 3,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S00-P4",
            "label": "Protected account, library and recommendation HTTPS JSON",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [
              "T-001",
              "T-004",
              "T-005",
              "T-006",
              "T-008",
              "T-010",
              "T-012"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "Valid unsuspended session required",
            "authorization": "Session ownership; Admin for suspension/restoration; domain deny-by-default",
            "threat_count": 7,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S00-P5",
            "label": "Local operator initial Admin command",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [
              "T-001"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "Local operator command; exact mechanism not specified",
            "authorization": "Initial Admin provisioning; concrete operator execution controls not specified",
            "threat_count": 1,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S07-EP02",
            "label": "Metadata manual entry and match selection",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "No service account required for local/MusicBrainz functions",
            "authorization": "Current user-selected local scope; explicit approval required for writes",
            "threat_count": 0,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S07-EP03",
            "label": "HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "Not fully specified at this grouped granularity",
            "authorization": "See SC-001/SC-006 operation policy",
            "threat_count": 0,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "S07-EP04",
            "label": "MusicBrainz response ingress",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "No service account required for local/MusicBrainz functions",
            "authorization": "Current user-selected local scope; explicit approval required for writes",
            "threat_count": 0,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          },
          {
            "model_id": "POST-EP01",
            "label": "Local operator invitation issue command",
            "kind": "entry point",
            "zone": "source-defined surface; grouped operations may cross zones",
            "threat_ids": [
              "T-001",
              "T-009",
              "T-017"
            ],
            "control_ids": [
              "C-SC-001",
              "C-SC-002",
              "C-SC-005",
              "C-SC-006"
            ],
            "authentication": "Local operator command; concrete invocation not specified",
            "authorization": "Issue invitations under SC-010; no remote Admin invitation API",
            "threat_count": 3,
            "count_scope": "Explicit affected_ids mappings only; zero is not proof of absence. Composite entry points overlap; do not sum counts."
          }
        ],
        "connections": [],
        "boundary_groups": [
          {
            "id": "S00-B1",
            "label": "Filesystem to desktop media adapter",
            "control_ids": [
              "C-SC-002",
              "C-SC-003"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B2",
            "label": "Desktop to external services",
            "control_ids": [
              "C-SC-002",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B3",
            "label": "Desktop to authenticated recommendation API",
            "control_ids": [
              "C-SC-001",
              "C-SC-004",
              "C-SC-005"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "S00-B4",
            "label": "API handler to service domain authorization",
            "control_ids": [
              "C-SC-006"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "adopted plan; no implemented/verified control evidence"
          },
          {
            "id": "POST-B01",
            "label": "Desktop media adapter to restricted helper process",
            "control_ids": [
              "C-SC-002",
              "C-SC-003",
              "C-SC-011"
            ],
            "style": "dashed border with explicit trust boundary label",
            "status": "ACTIVE adopted limits and isolation, not verified"
          }
        ],
        "ordering_constraints": [
          "Actors on left; native desktop then API/domain then service store; external integrations on separate right branch.",
          "Group internal logical components without implying additional deployment.",
          "Threat IDs appear outside component labels."
        ],
        "legend": {
          "arrow": "documented call/data direction; return to caller where stated",
          "dashed_border": "trust boundary; ordinary grouping has a labeled plain border",
          "neutral_T_marker": "unrated design threat; no severity color or order",
          "control": "adopted planned control, not verified; ACTIVE is specification status only",
          "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"
        },
        "threat_legend": {},
        "annotations": [
          "All controls are specification plans. No observed implementation or verified mitigation.",
          "OD-010–OD-019 are resolved; SC-001–SC-015 are ACTIVE adopted specifications. Required implementation, workload, privacy-review and release evidence remains pending."
        ],
        "text_preview": "S00-P1: Selected media, folders and JPEG/PNG cover art — No service account required for local/MusicBrainz functions; S00-P2: MusicBrainz responses and native metadata rendering — No service account required for local/MusicBrainz functions; S00-P3: Public registration and sign-in HTTPS JSON — Registration and sign-in precede established session; registration requires valid invitation; S00-P4: Protected account, library and recommendation HTTPS JSON — Valid unsuspended session required; S00-P5: Local operator initial Admin command — Local operator command; exact mechanism not specified; S07-EP02: Metadata manual entry and match selection — No service account required for local/MusicBrainz functions; S07-EP03: HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration — Not fully specified at this grouped granularity; S07-EP04: MusicBrainz response ingress — No service account required for local/MusicBrainz functions; POST-EP01: Local operator invitation issue command — Local operator command; concrete invocation not specified"
      },
      "omissions": [
        "Exact endpoint methods/paths and runtime topology are not evidenced.",
        "Local protocols beyond stated ports/adapters are not assigned wire protocols.",
        "No universal sensitivity class or risk score is invented.",
        "Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge."
      ],
      "validation_notes": [
        "Model IDs and flow references checked against stage08; not rendered."
      ]
    }
  ],
  "coverage": [
    {
      "id": "S00-CV1",
      "element_id": "S00-A1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-002"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV2",
      "element_id": "S00-A2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-002"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV3",
      "element_id": "S00-A3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-006"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-004"
          ]
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV4",
      "element_id": "S00-A4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV5",
      "element_id": "S00-U1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV6",
      "element_id": "S00-U2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV7",
      "element_id": "S00-U3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV8",
      "element_id": "S00-U4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV9",
      "element_id": "S00-D1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV10",
      "element_id": "S00-D2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV11",
      "element_id": "S00-D3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-006"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-004"
          ]
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV12",
      "element_id": "S00-D4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV13",
      "element_id": "S00-Z1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV14",
      "element_id": "S00-Z2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV15",
      "element_id": "S00-Z3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV16",
      "element_id": "S00-Z4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV17",
      "element_id": "S00-B1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-002"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV18",
      "element_id": "S00-B2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV19",
      "element_id": "S00-B3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-004"
          ]
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV20",
      "element_id": "S00-B4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV21",
      "element_id": "S00-F1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV22",
      "element_id": "S00-F2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-002"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV23",
      "element_id": "S00-F3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV24",
      "element_id": "S00-F4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-006"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-004"
          ]
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV25",
      "element_id": "S00-F5",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV26",
      "element_id": "S00-F6",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV27",
      "element_id": "S00-P1",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-002"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV28",
      "element_id": "S00-P2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-003"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV29",
      "element_id": "S00-P3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV30",
      "element_id": "S00-P4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-006"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-004"
          ]
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-005"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S00-CV31",
      "element_id": "S00-P5",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-001"
          ]
        },
        "Tampering": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Denial of Service": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Elevation of Privilege": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md"
    },
    {
      "id": "S01-CV1",
      "method_id": "S01-M",
      "stage": 1,
      "name": "Objectives",
      "status": "completed with evidence gaps",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [
        "S01-G2"
      ],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-CV2",
      "method_id": "S01-M",
      "stage": 2,
      "name": "Technical scope",
      "status": "completed from specifications",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-CV3",
      "method_id": "S01-M",
      "stage": 3,
      "name": "Decomposition",
      "status": "completed from specifications",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-CV4",
      "method_id": "S01-M",
      "stage": 4,
      "name": "Threat analysis",
      "status": "completed with evidence gaps",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [
        "S01-G3"
      ],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-CV5",
      "method_id": "S01-M",
      "stage": 5,
      "name": "Weakness analysis",
      "status": "completed with evidence gaps",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [
        "S01-G1"
      ],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-CV6",
      "method_id": "S01-M",
      "stage": 6,
      "name": "Attack modeling",
      "status": "completed with evidence gaps",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [
        "S01-G1"
      ],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S01-CV7",
      "method_id": "S01-M",
      "stage": 7,
      "name": "Risk and impact analysis",
      "status": "completed with evidence gaps",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "gap_ids": [
        "S01-G2"
      ],
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md"
    },
    {
      "id": "S02-CV1",
      "element_id": "S00-D1",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-011"
          ]
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV2",
      "element_id": "S00-D2",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV3",
      "element_id": "S00-D3",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Data disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010",
            "T-012"
          ]
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV4",
      "element_id": "S00-D4",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV5",
      "element_id": "S00-A1",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV6",
      "element_id": "S00-A2",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV7",
      "element_id": "S00-A3",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Data disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010",
            "T-012"
          ]
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV8",
      "element_id": "S00-A4",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV9",
      "element_id": "S00-U1",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV10",
      "element_id": "S00-U2",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV11",
      "element_id": "S00-U3",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV12",
      "element_id": "S00-U4",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV13",
      "element_id": "S00-F1",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV14",
      "element_id": "S00-F2",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV15",
      "element_id": "S00-F3",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-011"
          ]
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV16",
      "element_id": "S00-F4",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Data disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010",
            "T-012"
          ]
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV17",
      "element_id": "S00-F5",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-011"
          ]
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV18",
      "element_id": "S00-F6",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV19",
      "element_id": "S00-P1",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV20",
      "element_id": "S00-P2",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-011"
          ]
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV21",
      "element_id": "S00-P3",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV22",
      "element_id": "S00-P4",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010"
          ]
        },
        "Data disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "T-010",
            "T-012"
          ]
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S02-CV23",
      "element_id": "S00-P5",
      "method_id": "S02-M",
      "dispositions": {
        "Linking": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Identifying": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Detecting": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Data disclosure": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Unawareness and unintervenability": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Non-compliance": {
          "status": "not assessed: legal scope evidence missing",
          "threat_ids": []
        }
      },
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md"
    },
    {
      "id": "S03-CV1",
      "status": "assessed",
      "description": "Six roots cover file integrity, access control, sharing privacy, native content, and availability. Each node reachable; child references resolve. Control IDs are shared defenses across roots; no leaf is duplicated across trees. No supplied authoritative CAPEC material; identifiers omitted.",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md"
    },
    {
      "id": "S04-CV1",
      "function": "Review/save and recovery",
      "status": "assessed",
      "threat_ids": [
        "T-019"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV2",
      "function": "Recovery restore",
      "status": "assessed",
      "threat_ids": [
        "T-020"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV3",
      "function": "Native import and display",
      "status": "assessed",
      "threat_ids": [
        "T-021"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV4",
      "function": "Shared-library mutation/deletion",
      "status": "assessed",
      "threat_ids": [
        "T-022"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV5",
      "function": "Recommendation pagination",
      "status": "assessed",
      "threat_ids": [
        "T-023"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV6",
      "function": "Credentials and network adapters",
      "status": "assessed",
      "threat_ids": [
        "T-024"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV7",
      "function": "Pilot storage and workload",
      "status": "assessed",
      "threat_ids": [
        "T-025"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S04-CV8",
      "status": "assessed with no additional evidenced scenario",
      "description": "Collection queries/filters, manual edits, matching/discovery, account administration, packaging and upgrades covered through six architecture components and their specified controls; no operational failures or additional ratings supplied.",
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md"
    },
    {
      "id": "S05-CV1",
      "phase": "Data sourcing/preparation for ML",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV2",
      "phase": "Training/adaptation",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV3",
      "phase": "Model evaluation",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV4",
      "phase": "Model artifact storage",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV5",
      "phase": "Model deployment",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV6",
      "phase": "Model inference",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV7",
      "phase": "Model monitoring/feedback",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV8",
      "phase": "LLM retrieval/agents/tools",
      "status": "Not applicable to specified release",
      "rationale": "No such model lifecycle component is evidenced; FR-3.2–FR-3.3 and FR-3.11–FR-3.16 fully specify deterministic recommendation calculation. MusicBrainz is metadata lookup, not model retrieval.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV9",
      "method_id": "S05-M1",
      "status": "Not applicable at lifecycle scope",
      "description": "No AI assets to which ATLAS tactics/techniques can be mapped; ordinary metadata, authorization and privacy risks remain in other methods.",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV10",
      "method_id": "S05-M2",
      "status": "Not applicable at lifecycle scope; exact checklist unverified",
      "description": "No training, learned parameters, model inputs/outputs or ML serving exists in the specified architecture.",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S05-CV11",
      "method_id": "S05-M3",
      "status": "Not applicable",
      "description": "No LLM behavior present.",
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md"
    },
    {
      "id": "S06-COV01",
      "phase": 1,
      "name": "Technology stack identification",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV02",
      "phase": 2,
      "name": "Entry point enumeration",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV03",
      "phase": 3,
      "name": "Data store analysis",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV04",
      "phase": 4,
      "name": "Authentication and authorization architecture",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV05",
      "phase": 5,
      "name": "Security controls inventory",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV06",
      "phase": 6,
      "name": "Deployment and infrastructure analysis",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV07",
      "phase": 7,
      "name": "AI/ML component analysis",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S06-COV08",
      "phase": 8,
      "name": "Trust boundary identification",
      "disposition": "Not applicable to implementation: no implementation exists",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "limit": "Document intent is extracted independently by stage07; this phase cannot verify runtime enforcement.",
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md"
    },
    {
      "id": "S07-COV01",
      "category": "Assets",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV02",
      "category": "Actors",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV03",
      "category": "Data",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV04",
      "category": "Flows",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV05",
      "category": "Trust boundaries",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV06",
      "category": "Existing threats",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; existing threat catalog and supplied numerical risk ratings absent",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV07",
      "category": "Controls",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV08",
      "category": "Assumptions",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV09",
      "category": "Requirements",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S07-COV10",
      "category": "Gaps",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps",
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md"
    },
    {
      "id": "S08-COV00",
      "stage": 0,
      "artifact": "threat-model/stages/00-stride.md",
      "methods": [
        "S00-M"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S00-CV1",
        "S00-CV2",
        "S00-CV3",
        "S00-CV4",
        "S00-CV5",
        "S00-CV6",
        "S00-CV7",
        "S00-CV8",
        "S00-CV9",
        "S00-CV10",
        "S00-CV11",
        "S00-CV12",
        "S00-CV13",
        "S00-CV14",
        "S00-CV15",
        "S00-CV16",
        "S00-CV17",
        "S00-CV18",
        "S00-CV19",
        "S00-CV20",
        "S00-CV21",
        "S00-CV22",
        "S00-CV23",
        "S00-CV24",
        "S00-CV25",
        "S00-CV26",
        "S00-CV27",
        "S00-CV28",
        "S00-CV29",
        "S00-CV30",
        "S00-CV31"
      ],
      "threat_count": 6,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV01",
      "stage": 1,
      "artifact": "threat-model/stages/01-pasta.md",
      "methods": [
        "S01-M"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S01-CV1",
        "S01-CV2",
        "S01-CV3",
        "S01-CV4",
        "S01-CV5",
        "S01-CV6",
        "S01-CV7"
      ],
      "threat_count": 3,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV02",
      "stage": 2,
      "artifact": "threat-model/stages/02-linddun.md",
      "methods": [
        "S02-M"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S02-CV1",
        "S02-CV2",
        "S02-CV3",
        "S02-CV4",
        "S02-CV5",
        "S02-CV6",
        "S02-CV7",
        "S02-CV8",
        "S02-CV9",
        "S02-CV10",
        "S02-CV11",
        "S02-CV12",
        "S02-CV13",
        "S02-CV14",
        "S02-CV15",
        "S02-CV16",
        "S02-CV17",
        "S02-CV18",
        "S02-CV19",
        "S02-CV20",
        "S02-CV21",
        "S02-CV22",
        "S02-CV23"
      ],
      "threat_count": 3,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV03",
      "stage": 3,
      "artifact": "threat-model/stages/03-attack-trees.md",
      "methods": [
        "S03-M1"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S03-CV1"
      ],
      "threat_count": 6,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV04",
      "stage": 4,
      "artifact": "threat-model/stages/04-fmea.md",
      "methods": [
        "S04-M1"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S04-CV1",
        "S04-CV2",
        "S04-CV3",
        "S04-CV4",
        "S04-CV5",
        "S04-CV6",
        "S04-CV7",
        "S04-CV8"
      ],
      "threat_count": 7,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV05",
      "stage": 5,
      "artifact": "threat-model/stages/05-ai-ml.md",
      "methods": [
        "S05-M1",
        "S05-M2",
        "S05-M3"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S05-CV1",
        "S05-CV2",
        "S05-CV3",
        "S05-CV4",
        "S05-CV5",
        "S05-CV6",
        "S05-CV7",
        "S05-CV8",
        "S05-CV9",
        "S05-CV10",
        "S05-CV11"
      ],
      "threat_count": 0,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV06",
      "stage": 6,
      "artifact": "threat-model/stages/06-repository.md",
      "methods": [
        "S06-METHOD"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S06-COV01",
        "S06-COV02",
        "S06-COV03",
        "S06-COV04",
        "S06-COV05",
        "S06-COV06",
        "S06-COV07",
        "S06-COV08"
      ],
      "threat_count": 0,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "S08-COV07",
      "stage": 7,
      "artifact": "threat-model/stages/07-documents.md",
      "methods": [
        "S07-METHOD"
      ],
      "input_scope": "All four specifications; stage06 additionally complete tracked repository baseline",
      "upstream_coverage_ids": [
        "S07-COV01",
        "S07-COV02",
        "S07-COV03",
        "S07-COV04",
        "S07-COV05",
        "S07-COV06",
        "S07-COV07",
        "S07-COV08",
        "S07-COV09",
        "S07-COV10"
      ],
      "threat_count": 0,
      "evidence_limit": "Same specification evidence; no implementation/effectiveness claim"
    },
    {
      "id": "POST-COV01",
      "selected_flow_id": "S00-F2",
      "selection_basis": "PASTA T-007 and FMEA T-019/T-020 assess cross-store integrity; explanatory sequence emphasis, not risk rank.",
      "threat_ids": [
        "T-007",
        "T-019",
        "T-020"
      ],
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S04-E1",
        "S04-E2",
        "POST-E03"
      ]
    },
    {
      "id": "POST-COV02",
      "description": "Resolved policy and post-analysis architecture coverage: all adopted new FR texts, fifteen exact controls, ten OD and five RQ resolutions; helper, invitation, identifier-only output and prospective deployment added. No runtime evidence inferred.",
      "element_ids": [
        "POST-A01",
        "POST-B01",
        "POST-F01",
        "POST-F02",
        "POST-EP01",
        "POST-D01"
      ],
      "evidence_ids": [
        "POST-E01",
        "POST-E02",
        "POST-E03",
        "POST-E04"
      ]
    }
  ],
  "conflicts": [],
  "gaps": [
    {
      "id": "S00-G1",
      "description": "No code, test results, measured API workload or operational evidence establishes that adopted controls work.",
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "all four specifications"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S00-G2",
      "description": "No stated inference-resistance policy reconciles exact recommendation counts/ranking with FR-4.10 in very small overlap cohorts.",
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "FR-3.2–FR-3.3, FR-4.10"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-010"
      ]
    },
    {
      "id": "S00-G3",
      "description": "Queue capacity, registration abuse admission policy, and outbound response byte/collection bounds are not specified; existing deadlines and authenticated/sign-in limits do not resolve these design choices.",
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "SC-001, SC-002, SC-005"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-012",
        "DEC-OD-013",
        "DEC-OD-014"
      ]
    },
    {
      "id": "S00-G4",
      "description": "No approved risk-scoring method or ratings supplied.",
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ],
      "source_locators": [
        "all four specifications"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 0,
      "source_artifact": "threat-model/stages/00-stride.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S01-G1",
      "description": "No implementation, measured weakness, incident record, attack simulation or control-effectiveness evidence is supplied.",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "all four specifications"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S01-G2",
      "description": "No supplied risk appetite, business-loss values, likelihood inputs or approved risk method; risk remains unrated.",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "all four specifications"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S01-G3",
      "description": "No external threat intelligence or evidenced malicious actor activity is supplied; participating callers and untrusted input are exposure evidence, not proof of hostile activity.",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "FR-4.2; SC-002"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S01-G4",
      "description": "Closed-pilot admission criteria and registration resource admission policy are unspecified.",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "REQUIREMENTS.md release scope; FR-4.2; SC-001"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-011",
        "DEC-OD-012"
      ]
    },
    {
      "id": "S01-G5",
      "description": "Inference-resistance expectations for exact recommendation results are unspecified.",
      "evidence_ids": [
        "S01-E1",
        "S01-E2",
        "S01-E3",
        "S01-E4"
      ],
      "source_locators": [
        "FR-3.2–FR-3.3, FR-4.10"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 1,
      "source_artifact": "threat-model/stages/01-pasta.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-010"
      ]
    },
    {
      "id": "S02-G1",
      "description": "Deployment jurisdiction, processing basis, user notice and legal-scope applicability are not supplied; SC-008 establishes a public-launch evidence gate and explicitly does not waive pilot obligations. No compliance conclusion is possible.",
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "SC-008"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence.",
      "current_context": "Germany/EEA scope and intended operation-specific bases adopted in OD-018/OD-019; actual deployment, notice, applicable review and substantiation still required before collection.",
      "decision_ids": [
        "DEC-OD-018",
        "DEC-OD-019"
      ]
    },
    {
      "id": "S02-G2",
      "description": "The privacy expectation for inference from exact small-cohort recommendation outputs is unspecified.",
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "FR-3.2–FR-3.3, FR-4.10"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-010"
      ]
    },
    {
      "id": "S02-G3",
      "description": "No implementation, log samples, deletion tests or notice artifacts demonstrate the planned privacy controls.",
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "SC-004, SC-008"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S02-G4",
      "description": "No approved privacy risk method or ratings are supplied.",
      "evidence_ids": [
        "S02-E1",
        "S02-E2",
        "S02-E3",
        "S02-E4"
      ],
      "source_locators": [
        "all four specifications"
      ],
      "status": "missing evidence, not demonstrated defect",
      "source_stage": 2,
      "source_artifact": "threat-model/stages/02-linddun.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S03-G1",
      "description": "No runtime, failure history, verification results, or supplied risk prioritization method; this is not proof controls fail.",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S03-G2",
      "description": "Registration exists and password hashing is resource-intensive under SC-005, but SC-001 specifies sign-in and authenticated limits only. Registration admission/rate budget and closed-pilot enrollment mechanism are not specified; no exploit is demonstrated.",
      "evidence_ids": [
        "S03-E1",
        "S03-E3"
      ],
      "source_stage": 3,
      "source_artifact": "threat-model/stages/03-attack-trees.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-011",
        "DEC-OD-012"
      ]
    },
    {
      "id": "S04-G1",
      "description": "No runtime, failure history, verification results, or supplied risk prioritization method; this is not proof controls fail.",
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S04-G2",
      "description": "Recovery-copy content integrity across retention and handling of legitimate destination edits before restore are not fully specified. Existing recorded-path and substitution checks do not by themselves decide these semantics.",
      "evidence_ids": [
        "S04-E1",
        "S04-E3"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-016"
      ]
    },
    {
      "id": "S04-G3",
      "description": "Service recovery objectives are absent. No-backup pilot policy is explicit, not an accidental absence; consequence requires acceptance/operational evidence, not an invented backup requirement.",
      "evidence_ids": [
        "S04-E2",
        "S04-E3"
      ],
      "source_stage": 4,
      "source_artifact": "threat-model/stages/04-fmea.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-017"
      ]
    },
    {
      "id": "S05-G1",
      "description": "No runtime, failure history, verification results, or supplied risk prioritization method; this is not proof controls fail.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2",
        "S05-E3",
        "S05-E4"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S05-G2",
      "description": "OWASP exact draft revision/category list and ATLAS latest-release status were not verified. No taxonomy-level completeness or identifier mappings are claimed. This does not prevent the specification-supported no-AI applicability finding.",
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "source_stage": 5,
      "source_artifact": "threat-model/stages/05-ai-ml.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S06-G01",
      "description": "Implementation and effective-control evidence unavailable. No implementation exists. Cannot enumerate actual routes, schemas, credentials, deployment settings, database configuration, enforcement paths, or verified controls.",
      "evidence_ids": [
        "S06-E01",
        "S06-E02"
      ],
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S06-G02",
      "description": "Exact dependency patches/build manifests absent at pre-implementation baseline. Planned stack corpus is not adopted authority; caller project rules remain unverified against corpus and runtime. Unmatched: C++17, JavaScript ES2022, TagLib2, SQLite3, CMake3.28, MSVC2022, Xcode16, GCC13, systemd, Ubuntu24.04. Alternative matches for gRPC/A2A/Foundry/Genkit are not architecture evidence.",
      "evidence_ids": [
        "S06-E03",
        "S06-E04",
        "S06-E05"
      ],
      "source_stage": 6,
      "source_artifact": "threat-model/stages/06-repository.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S07-G01",
      "description": "Document dates and authors not supplied; no runtime or test evidence. Component responsibilities exist, but individual component owners not supplied. Currency unknown, not stale.",
      "evidence_ids": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S07-G02",
      "description": "Concrete HTTP methods/paths, schema versions, pagination cursor integrity format, and normalization rules for usernames are not defined. Authentication and authorization intent is defined; absent detail is not proof of a bypass.",
      "evidence_ids": [
        "S07-E02",
        "S07-E03"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence.",
      "current_context": "Account-name policy resolved by OD-015/FR-4.30; concrete API route/schema and cursor implementation evidence still pending.",
      "decision_ids": [
        "DEC-OD-015"
      ]
    },
    {
      "id": "S07-G03",
      "description": "Queued-work bound lacks a chosen capacity; registration has no explicit unauthenticated throttle; outbound response/metadata/parser work bounds beyond image limits and deadlines are not specified. Existing capacity, body, page and rate limits remain adopted.",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-012",
        "DEC-OD-013",
        "DEC-OD-014"
      ]
    },
    {
      "id": "S07-G04",
      "description": "Public-launch jurisdiction, processing basis, notice and license evidence is required by SC-008 but values are absent; pilot obligations are explicitly not waived.",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence.",
      "current_context": "Germany/EEA scope and intended operation-specific bases adopted in OD-018/OD-019; actual deployment, notice, applicable review and substantiation still required before collection.",
      "decision_ids": [
        "DEC-OD-018",
        "DEC-OD-019"
      ]
    },
    {
      "id": "S07-G05",
      "description": "Exact ranked identifiers/counts and repeated user-controlled library submissions are specified, but privacy inference resistance and accepted residual disclosure are not settled. No direct identity/full-library endpoint is allowed.",
      "evidence_ids": [
        "S07-E01",
        "S07-E02",
        "S07-E03"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-010"
      ]
    },
    {
      "id": "S07-G06",
      "description": "Owner-only recovery copies, file identity binding, and atomic replacement are specified; hard-link aliases, cross-process serialization, precise platform identity strategy, and crash-safe deletion-completion coordination are not detailed. No actual race is demonstrated.",
      "evidence_ids": [
        "S07-E01",
        "S07-E02",
        "S07-E03"
      ],
      "source_stage": 7,
      "source_artifact": "threat-model/stages/07-documents.md",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S08-G01",
      "description": "S05-F1 is a composite recommendation-and-label flow observed in only one upstream record. It is supported by REQUIREMENTS/ARCHITECTURE and overlaps S00-F4 and S00-F3; keep distinct because endpoints/data scope differ. No shadow flow or defect inferred.",
      "affected_ids": [
        "S05-F1",
        "S00-F4",
        "S00-F3"
      ],
      "evidence_ids": [
        "S05-E1",
        "S05-E2"
      ],
      "needed_evidence": "Implementation/interface call traces to reconcile runtime flow granularity.",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S08-G02",
      "description": "Component-level assets from document absorption have no separate scenario records; composite assets and flow threats cover relevant functions. No evidence proves exhaustive component-level behavior coverage.",
      "evidence_ids": [
        "S07-E02"
      ],
      "needed_evidence": "Implemented component/interface inventory and mapped acceptance/security tests.",
      "post_analysis_status": "Evidence gap remains; baseline statement preserved as historical. Current design values do not establish runtime, test, taxonomy or legal evidence."
    },
    {
      "id": "S08-G03",
      "description": "No source fragment establishes a material contradiction. Conditional tension between exact recommendation outputs and inference-resistant interpretation of FR-4.10 remains an unresolved privacy decision, not a proven contradiction.",
      "related_threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "evidence_ids": [
        "S00-E1",
        "S00-E2"
      ],
      "needed_evidence": "Adopted product privacy outcome and security treatment decision.",
      "post_analysis_status": "Design choice resolved; implementation and effectiveness remain unverified",
      "resolved_by_decision_ids": [
        "DEC-OD-010"
      ]
    },
    {
      "id": "DEC-OD-010",
      "specification_id": "OD-010",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Apply the qualifying-cohort, contributor, ranking and disclosure requirements in FR-3.20–FR-3.23, with bounded query/replacement access and adversarial privacy verification in SC-009.",
      "dependent_control_ids": [
        "C-SC-009"
      ],
      "threat_ids": [
        "T-004",
        "T-008",
        "T-010"
      ],
      "owning_product_items": [
        "RQ-001"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-011",
      "specification_id": "OD-011",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Require the single-use operator invitation in FR-4.29; generate and consume it under SC-010.",
      "dependent_control_ids": [
        "C-SC-010"
      ],
      "threat_ids": [
        "T-009",
        "T-017"
      ],
      "owning_product_items": [
        "RQ-002"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-012",
      "specification_id": "OD-012",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Enforce the registration admission budgets in SC-010 before expensive account creation.",
      "dependent_control_ids": [
        "C-SC-010"
      ],
      "threat_ids": [
        "T-005",
        "T-009",
        "T-017"
      ],
      "owning_product_items": [],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-013",
      "specification_id": "OD-013",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Enforce the API and password-hashing concurrency/queue budgets in SC-011 within the existing request deadline.",
      "dependent_control_ids": [
        "C-SC-011"
      ],
      "threat_ids": [
        "T-005",
        "T-017",
        "T-025"
      ],
      "owning_product_items": [],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-014",
      "specification_id": "OD-014",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Enforce the response, metadata and parser budgets in SC-011; failure behavior is FR-1.45 and FR-3.24.",
      "dependent_control_ids": [
        "C-SC-011"
      ],
      "threat_ids": [
        "T-003",
        "T-005",
        "T-021"
      ],
      "owning_product_items": [],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-015",
      "specification_id": "OD-015",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Apply FR-4.30 account-name acceptance and canonical equivalence consistently through SC-012.",
      "dependent_control_ids": [
        "C-SC-012"
      ],
      "threat_ids": [
        "T-001",
        "T-009"
      ],
      "owning_product_items": [
        "RQ-005"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-016",
      "specification_id": "OD-016",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Require a verified recovery copy before restoration under FR-1.46 and SC-013.",
      "dependent_control_ids": [
        "C-SC-013"
      ],
      "threat_ids": [
        "T-020"
      ],
      "owning_product_items": [
        "RQ-003"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-017",
      "specification_id": "OD-017",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Use FR-4.31's empty-service reprovisioning outcome after store loss; retain the no-backup policy and verify recovery under SC-014.",
      "dependent_control_ids": [
        "C-SC-014"
      ],
      "threat_ids": [
        "T-025"
      ],
      "owning_product_items": [
        "RQ-004"
      ],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-018",
      "specification_id": "OD-018",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Use the prospective pilot location in ARCHITECTURE.md and participant scope in FR-4.34; substantiate actual deployment and eligibility before pilot collection under SC-015.",
      "dependent_control_ids": [
        "C-SC-015"
      ],
      "threat_ids": [
        "T-010",
        "T-011",
        "T-012"
      ],
      "owning_product_items": [],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-OD-019",
      "specification_id": "OD-019",
      "status": "RESOLVED; adopted, verification pending",
      "description": "Adopt the operation-specific processing plan and pre-pilot notice/review gate in SC-015. Its legal and operational evidence must substantiate the plan before collection; no legal conclusion is asserted.",
      "dependent_control_ids": [
        "C-SC-015"
      ],
      "threat_ids": [
        "T-010",
        "T-011",
        "T-012"
      ],
      "owning_product_items": [],
      "evidence_ids": [
        "POST-E03"
      ]
    },
    {
      "id": "DEC-RQ-001",
      "specification_id": "RQ-001",
      "owner": "REQUIREMENTS.md",
      "status": "RESOLVED; adopted product policy, unimplemented",
      "description": "Privacy eligibility and count suppression are defined in FR-3.20–FR-3.23; disclosure and verification are defined in FR-4.28. Exact ranking remains required for qualifying results.",
      "dependencies": "OD-010; T-004, T-008, T-010",
      "evidence_ids": [
        "POST-E01"
      ]
    },
    {
      "id": "DEC-RQ-002",
      "specification_id": "RQ-002",
      "owner": "REQUIREMENTS.md",
      "status": "RESOLVED; adopted product policy, unimplemented",
      "description": "Operator invitations govern closed-pilot enrollment under FR-4.29 and FR-4.34.",
      "dependencies": "OD-011; T-009, T-017",
      "evidence_ids": [
        "POST-E01"
      ]
    },
    {
      "id": "DEC-RQ-003",
      "specification_id": "RQ-003",
      "owner": "REQUIREMENTS.md",
      "status": "RESOLVED; adopted product policy, unimplemented",
      "description": "Restoration first preserves the current destination under FR-1.46.",
      "dependencies": "OD-016; T-020",
      "evidence_ids": [
        "POST-E01"
      ]
    },
    {
      "id": "DEC-RQ-004",
      "specification_id": "RQ-004",
      "owner": "REQUIREMENTS.md",
      "status": "RESOLVED; adopted product policy, unimplemented",
      "description": "Store-loss behavior and absence of a recovery deadline are explicit in FR-4.31; no-backup controls remain unchanged.",
      "dependencies": "OD-017; T-025",
      "evidence_ids": [
        "POST-E01"
      ]
    },
    {
      "id": "DEC-RQ-005",
      "specification_id": "RQ-005",
      "owner": "REQUIREMENTS.md",
      "status": "RESOLVED; adopted product policy, unimplemented",
      "description": "Account-name acceptance and equivalence are defined in FR-4.30.",
      "dependencies": "OD-015; T-001, T-009",
      "evidence_ids": [
        "POST-E01"
      ]
    }
  ]
}
```

## System Context

ID: D09-01. Purpose: Show local editing and remote discovery/sharing context. Audience: Product and security reviewers.

| Model ID | Element | Kind | Zone | Threats / controls |
| --- | --- | --- | --- | --- |
| S08-SCOPE | Tag Zeppelin | system | not further assigned by source | None assigned |
| S00-U1 | Current desktop user | actor | not further assigned by source | None assigned |
| S00-U2 | Participating service user | actor | not further assigned by source | None assigned |
| S00-U3 | Recommendation-service Admin | actor | not further assigned by source | None assigned |
| S00-U4 | Operator | actor | not further assigned by source | None assigned |
| S07-ACT05 | Project maintainer | actor | not further assigned by source | None assigned |
| S07-A10 | MusicBrainz | component | S00-Z4 | None assigned |
| S07-A11 | OS browser/Bandcamp | component | S00-Z4 | None assigned |

| Connection | Source → destination | Data / protocol | Sensitivity | Boundaries |
| --- | --- | --- | --- | --- |
| D09-CTX-S00-U1 | S00-U1 → S08-SCOPE | Native interaction: local collection/review | not classified by source | None specified |
| D09-CTX-S00-U2 | S00-U2 → S08-SCOPE | HTTPS JSON through native client: account and memberships | personal data | S00-B3 |
| D09-CTX-S00-U3 | S00-U3 → S08-SCOPE | HTTPS JSON: Admin suspension/restoration | personal data | S00-B3 |
| D09-CTX-S07-A10 | S08-SCOPE → S07-A10 | HTTPS: metadata search terms/identifiers and response | not classified by source | S00-B2 |
| D09-CTX-S07-A11 | S08-SCOPE → S07-A11 | OS browser handoff: HTTPS purchase query | not classified by source | S00-B2 |

Text preview: S00-U1 → S08-SCOPE [Native interaction: local collection/review]; S00-U2 → S08-SCOPE [HTTPS JSON through native client: account and memberships]; S00-U3 → S08-SCOPE [HTTPS JSON: Admin suspension/restoration]; S08-SCOPE → S07-A10 [HTTPS: metadata search terms/identifiers and response]; S08-SCOPE → S07-A11 [OS browser handoff: HTTPS purchase query]

Legend: {"arrow": "documented call/data direction; return to caller where stated", "dashed_border": "trust boundary; ordinary grouping has a labeled plain border", "neutral_T_marker": "unrated design threat; no severity color or order", "control": "adopted planned control, not verified; ACTIVE is specification status only", "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"}

Boundary groups, source annotations, entry authentication/counts and precise ordering constraints are preserved in this diagram’s Model specification.

Omissions: Exact endpoint methods/paths and runtime topology are not evidenced. Local protocols beyond stated ports/adapters are not assigned wire protocols. No universal sensitivity class or risk score is invented. Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge.

Validation: Model IDs and flow references checked against stage08; not rendered.

## Container and Component Architecture

ID: D09-02. Purpose: Show logical modules, stores and enforcement placement. Audience: Developers and architecture reviewers.

| Model ID | Element | Kind | Zone | Threats / controls |
| --- | --- | --- | --- | --- |
| S00-U1 | Current desktop user | actor | not further assigned by source | None assigned |
| S00-U4 | Operator | actor | not further assigned by source | None assigned |
| S03-A5 | Desktop presentation | component | S00-Z1 | None assigned |
| S07-A02 | Local application/domain services | component | S00-Z1 | None assigned |
| S07-A03 | Persistence/media adapters | component | S00-Z1 | None assigned |
| S07-A04 | Desktop discovery/sharing adapters | component | S00-Z1 | None assigned |
| S00-A2 | Local catalog, proposals, approvals and operation state | data store | S00-Z1 | None assigned |
| S00-A1 | Music files and recovery copies | data store | S00-Z1 | None assigned |
| S07-A12 | Fastify API | component | S00-Z3 | None assigned |
| S07-A05 | Service account/sharing domain | component | S00-Z3 | None assigned |
| S07-A06 | Recommendation calculation | component | S00-Z3 | None assigned |
| S00-A3 | Service accounts, sessions and release memberships | data store | S00-Z3 | None assigned |
| S07-A10 | MusicBrainz | component | S00-Z4 | None assigned |
| S07-A11 | OS browser/Bandcamp | component | S00-Z4 | None assigned |
| POST-A01 | Restricted local media helper | component | S00-Z1 | None assigned |

| Connection | Source → destination | Data / protocol | Sensitivity | Boundaries |
| --- | --- | --- | --- | --- |
| D09-C01 | S00-U1 → S03-A5 | Native interaction: selected files, fields and decisions | not classified by source | None specified |
| D09-C02 | S03-A5 → S07-A02 | Application-service contracts: review/save/restore | not classified by source | None specified |
| D09-C03 | S07-A02 → S07-A03 | Abstract media/filesystem ports: bound approved changes | not classified by source | None specified |
| D09-C04 | S07-A03 → S00-A1 | Filesystem access: music and recovery contents | not classified by source | S00-B1 |
| D09-C05 | S07-A03 → S00-A2 | SQLite adapter: catalog/review/recovery state | not classified by source | None specified |
| D09-C06 | S07-A02 → S07-A04 | Network ports: discovery and sharing requests | not classified by source | None specified |
| D09-C07 | S07-A04 → S07-A10 | HTTPS: search terms / release identifiers and metadata | not classified by source | S00-B2 |
| D09-C08 | S07-A04 → S07-A11 | OS browser handoff, generated HTTPS purchase search URL | not classified by source | S00-B2 |
| D09-C09 | S07-A04 → S07-A12 | HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages | account/membership data is personal data | S00-B3 |
| D09-C10 | S07-A12 → S07-A05 | In-process domain invocation: authenticated account/library operation | personal data | S00-B4 |
| D09-C11 | S07-A05 → S00-A3 | SQLite adapter: accounts, sessions and memberships | personal data | None specified |
| D09-C12 | S07-A06 → S07-A05 | Owner-defined read interfaces: eligibility and memberships | personal data | None specified |
| D09-C13 | S07-A12 → S07-A06 | In-process domain invocation: recommendation calculation | personal data | None specified |
| D09-C14 | S07-A03 → POST-A01 | Bounded local process contract: selected input/staged file and operation data | not classified by source | POST-B01 |
| D09-C15 | S00-U4 → S07-A05 | Local operator command: issue invitations; concrete invocation syntax unspecified | not classified by source | None specified |

Text preview: S00-U1 → S03-A5 [Native interaction: selected files, fields and decisions]; S03-A5 → S07-A02 [Application-service contracts: review/save/restore]; S07-A02 → S07-A03 [Abstract media/filesystem ports: bound approved changes]; S07-A03 → S00-A1 [Filesystem access: music and recovery contents]; S07-A03 → S00-A2 [SQLite adapter: catalog/review/recovery state]; S07-A02 → S07-A04 [Network ports: discovery and sharing requests]; S07-A04 → S07-A10 [HTTPS: search terms / release identifiers and metadata]; S07-A04 → S07-A11 [OS browser handoff, generated HTTPS purchase search URL]; S07-A04 → S07-A12 [HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages]; S07-A12 → S07-A05 [In-process domain invocation: authenticated account/library operation]; S07-A05 → S00-A3 [SQLite adapter: accounts, sessions and memberships]; S07-A06 → S07-A05 [Owner-defined read interfaces: eligibility and memberships]; S07-A12 → S07-A06 [In-process domain invocation: recommendation calculation]; S07-A03 → POST-A01 [Bounded local process contract: selected input/staged file and operation data]; S00-U4 → S07-A05 [Local operator command: issue invitations; concrete invocation syntax unspecified]

Legend: {"arrow": "documented call/data direction; return to caller where stated", "dashed_border": "trust boundary; ordinary grouping has a labeled plain border", "neutral_T_marker": "unrated design threat; no severity color or order", "control": "adopted planned control, not verified; ACTIVE is specification status only", "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"}

Boundary groups, source annotations, entry authentication/counts and precise ordering constraints are preserved in this diagram’s Model specification.

Omissions: Exact endpoint methods/paths and runtime topology are not evidenced. Local protocols beyond stated ports/adapters are not assigned wire protocols. No universal sensitivity class or risk score is invented. Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge.

Validation: Model IDs and flow references checked against stage08; not rendered.

## Data Flow Diagram

ID: D09-03. Purpose: Trace sensitive flows and trust crossings. Audience: Security and privacy reviewers.

| Model ID | Element | Kind | Zone | Threats / controls |
| --- | --- | --- | --- | --- |
| S00-U1 | Current desktop user | actor | not further assigned by source | None assigned |
| S00-U4 | Operator | actor | not further assigned by source | None assigned |
| S03-A5 | Desktop presentation | component | S00-Z1 | None assigned |
| S07-A02 | Local application/domain services | component | S00-Z1 | None assigned |
| S07-A03 | Persistence/media adapters | component | S00-Z1 | None assigned |
| S07-A04 | Desktop discovery/sharing adapters | component | S00-Z1 | None assigned |
| S00-A2 | Local catalog, proposals, approvals and operation state | data store | S00-Z1 | None assigned |
| S00-A1 | Music files and recovery copies | data store | S00-Z1 | None assigned |
| S07-A12 | Fastify API | component | S00-Z3 | None assigned |
| S07-A05 | Service account/sharing domain | component | S00-Z3 | None assigned |
| S07-A06 | Recommendation calculation | component | S00-Z3 | None assigned |
| S00-A3 | Service accounts, sessions and release memberships | data store | S00-Z3 | None assigned |
| S07-A10 | MusicBrainz | component | S00-Z4 | None assigned |
| S07-A11 | OS browser/Bandcamp | component | S00-Z4 | None assigned |
| POST-A01 | Restricted local media helper | component | S00-Z1 | None assigned |

| Connection | Source → destination | Data / protocol | Sensitivity | Boundaries |
| --- | --- | --- | --- | --- |
| D09-C01 | S00-U1 → S03-A5 | Native interaction: selected files, fields and decisions | not classified by source | None specified |
| D09-C02 | S03-A5 → S07-A02 | Application-service contracts: review/save/restore | not classified by source | None specified |
| D09-C03 | S07-A02 → S07-A03 | Abstract media/filesystem ports: bound approved changes | not classified by source | None specified |
| D09-C04 | S07-A03 → S00-A1 | Filesystem access: music and recovery contents | not classified by source | S00-B1 |
| D09-C05 | S07-A03 → S00-A2 | SQLite adapter: catalog/review/recovery state | not classified by source | None specified |
| D09-C06 | S07-A02 → S07-A04 | Network ports: discovery and sharing requests | not classified by source | None specified |
| D09-C07 | S07-A04 → S07-A10 | HTTPS: search terms / release identifiers and metadata | not classified by source | S00-B2 |
| D09-C08 | S07-A04 → S07-A11 | OS browser handoff, generated HTTPS purchase search URL | not classified by source | S00-B2 |
| D09-C09 | S07-A04 → S07-A12 | HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages | account/membership data is personal data | S00-B3 |
| D09-C10 | S07-A12 → S07-A05 | In-process domain invocation: authenticated account/library operation | personal data | S00-B4 |
| D09-C11 | S07-A05 → S00-A3 | SQLite adapter: accounts, sessions and memberships | personal data | None specified |
| D09-C12 | S07-A06 → S07-A05 | Owner-defined read interfaces: eligibility and memberships | personal data | None specified |
| D09-C13 | S07-A12 → S07-A06 | In-process domain invocation: recommendation calculation | personal data | None specified |
| D09-C14 | S07-A03 → POST-A01 | Bounded local process contract: selected input/staged file and operation data | not classified by source | POST-B01 |
| D09-C15 | S00-U4 → S07-A05 | Local operator command: issue invitations; concrete invocation syntax unspecified | not classified by source | None specified |

Text preview: S00-U1 → S03-A5 [Native interaction: selected files, fields and decisions]; S03-A5 → S07-A02 [Application-service contracts: review/save/restore]; S07-A02 → S07-A03 [Abstract media/filesystem ports: bound approved changes]; S07-A03 → S00-A1 [Filesystem access: music and recovery contents]; S07-A03 → S00-A2 [SQLite adapter: catalog/review/recovery state]; S07-A02 → S07-A04 [Network ports: discovery and sharing requests]; S07-A04 → S07-A10 [HTTPS: search terms / release identifiers and metadata]; S07-A04 → S07-A11 [OS browser handoff, generated HTTPS purchase search URL]; S07-A04 → S07-A12 [HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages]; S07-A12 → S07-A05 [In-process domain invocation: authenticated account/library operation]; S07-A05 → S00-A3 [SQLite adapter: accounts, sessions and memberships]; S07-A06 → S07-A05 [Owner-defined read interfaces: eligibility and memberships]; S07-A12 → S07-A06 [In-process domain invocation: recommendation calculation]; S07-A03 → POST-A01 [Bounded local process contract: selected input/staged file and operation data]; S00-U4 → S07-A05 [Local operator command: issue invitations; concrete invocation syntax unspecified]

Legend: {"arrow": "documented call/data direction; return to caller where stated", "dashed_border": "trust boundary; ordinary grouping has a labeled plain border", "neutral_T_marker": "unrated design threat; no severity color or order", "control": "adopted planned control, not verified; ACTIVE is specification status only", "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"}

Boundary groups, source annotations, entry authentication/counts and precise ordering constraints are preserved in this diagram’s Model specification.

Omissions: Exact endpoint methods/paths and runtime topology are not evidenced. Local protocols beyond stated ports/adapters are not assigned wire protocols. No universal sensitivity class or risk score is invented. Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge.

Validation: Model IDs and flow references checked against stage08; not rendered.

## Threat-Annotated Architecture

ID: D09-04. Purpose: Locate all 25 unrated scenarios and planned controls. Audience: Security reviewers.

| Model ID | Element | Kind | Zone | Threats / controls |
| --- | --- | --- | --- | --- |
| S00-U1 | Current desktop user | actor | not further assigned by source | None assigned |
| S00-U4 | Operator | actor | not further assigned by source | None assigned |
| S03-A5 | Desktop presentation | component | S00-Z1 | T-003, T-011, T-018, T-021, C-SC-002, C-SC-005, C-SC-008 |
| S07-A02 | Local application/domain services | component | S00-Z1 | T-002, T-007, T-013, T-019, T-020, T-024, C-SC-002, C-SC-003, C-SC-005 |
| S07-A03 | Persistence/media adapters | component | S00-Z1 | T-002, T-003, T-013, T-019, T-020, T-021, C-SC-002, C-SC-003 |
| S07-A04 | Desktop discovery/sharing adapters | component | S00-Z1 | T-006, T-011, T-012, T-015, T-016, T-023, T-024, C-SC-002, C-SC-004, C-SC-005, C-SC-008 |
| S00-A2 | Local catalog, proposals, approvals and operation state | data store | S00-Z1 | T-002, T-007, T-019, T-024, C-SC-002, C-SC-003, C-SC-005 |
| S00-A1 | Music files and recovery copies | data store | S00-Z1 | T-002, T-007, T-013, T-019, T-020, C-SC-002, C-SC-003 |
| S07-A12 | Fastify API | component | S00-Z3 | T-001, T-005, T-009, T-014, T-017, C-SC-001, C-SC-002, C-SC-005, C-SC-006, C-SC-007 |
| S07-A05 | Service account/sharing domain | component | S00-Z3 | T-001, T-006, T-012, T-014, T-015, T-016, T-022, T-023, C-SC-001, C-SC-004, C-SC-005, C-SC-006, C-SC-008 |
| S07-A06 | Recommendation calculation | component | S00-Z3 | T-004, T-005, T-008, T-010, T-015, T-017, T-023, T-025, C-SC-001, C-SC-002, C-SC-004, C-SC-005, C-SC-007, C-SC-008 |
| S00-A3 | Service accounts, sessions and release memberships | data store | S00-Z3 | T-001, T-004, T-006, T-008, T-009, T-010, T-012, T-014, T-015, T-016, T-017, T-022, T-023, T-025, C-SC-001, C-SC-004, C-SC-005, C-SC-006, C-SC-007, C-SC-008 |
| S07-A10 | MusicBrainz | component | S00-Z4 | T-011, T-024, C-SC-002, C-SC-005, C-SC-008 |
| S07-A11 | OS browser/Bandcamp | component | S00-Z4 | T-011, T-018, C-SC-002, C-SC-005, C-SC-008 |
| POST-A01 | Restricted local media helper | component | S00-Z1 | T-003, T-005, T-021, C-SC-001, C-SC-002, C-SC-005, C-SC-007 |

| Connection | Source → destination | Data / protocol | Sensitivity | Boundaries |
| --- | --- | --- | --- | --- |
| D09-C01 | S00-U1 → S03-A5 | Native interaction: selected files, fields and decisions | not classified by source | None specified |
| D09-C02 | S03-A5 → S07-A02 | Application-service contracts: review/save/restore | not classified by source | None specified |
| D09-C03 | S07-A02 → S07-A03 | Abstract media/filesystem ports: bound approved changes | not classified by source | None specified |
| D09-C04 | S07-A03 → S00-A1 | Filesystem access: music and recovery contents | not classified by source | S00-B1 |
| D09-C05 | S07-A03 → S00-A2 | SQLite adapter: catalog/review/recovery state | not classified by source | None specified |
| D09-C06 | S07-A02 → S07-A04 | Network ports: discovery and sharing requests | not classified by source | None specified |
| D09-C07 | S07-A04 → S07-A10 | HTTPS: search terms / release identifiers and metadata | not classified by source | S00-B2 |
| D09-C08 | S07-A04 → S07-A11 | OS browser handoff, generated HTTPS purchase search URL | not classified by source | S00-B2 |
| D09-C09 | S07-A04 → S07-A12 | HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages | account/membership data is personal data | S00-B3 |
| D09-C10 | S07-A12 → S07-A05 | In-process domain invocation: authenticated account/library operation | personal data | S00-B4 |
| D09-C11 | S07-A05 → S00-A3 | SQLite adapter: accounts, sessions and memberships | personal data | None specified |
| D09-C12 | S07-A06 → S07-A05 | Owner-defined read interfaces: eligibility and memberships | personal data | None specified |
| D09-C13 | S07-A12 → S07-A06 | In-process domain invocation: recommendation calculation | personal data | None specified |
| D09-C14 | S07-A03 → POST-A01 | Bounded local process contract: selected input/staged file and operation data | not classified by source | POST-B01 |
| D09-C15 | S00-U4 → S07-A05 | Local operator command: issue invitations; concrete invocation syntax unspecified | not classified by source | None specified |

Text preview: S00-U1 → S03-A5 [Native interaction: selected files, fields and decisions]; S03-A5 → S07-A02 [Application-service contracts: review/save/restore]; S07-A02 → S07-A03 [Abstract media/filesystem ports: bound approved changes]; S07-A03 → S00-A1 [Filesystem access: music and recovery contents]; S07-A03 → S00-A2 [SQLite adapter: catalog/review/recovery state]; S07-A02 → S07-A04 [Network ports: discovery and sharing requests]; S07-A04 → S07-A10 [HTTPS: search terms / release identifiers and metadata]; S07-A04 → S07-A11 [OS browser handoff, generated HTTPS purchase search URL]; S07-A04 → S07-A12 [HTTPS JSON: sessions/invitation registration, confirmed identifiers and ranked identifier-only pages]; S07-A12 → S07-A05 [In-process domain invocation: authenticated account/library operation]; S07-A05 → S00-A3 [SQLite adapter: accounts, sessions and memberships]; S07-A06 → S07-A05 [Owner-defined read interfaces: eligibility and memberships]; S07-A12 → S07-A06 [In-process domain invocation: recommendation calculation]; S07-A03 → POST-A01 [Bounded local process contract: selected input/staged file and operation data]; S00-U4 → S07-A05 [Local operator command: issue invitations; concrete invocation syntax unspecified]

Legend: {"arrow": "documented call/data direction; return to caller where stated", "dashed_border": "trust boundary; ordinary grouping has a labeled plain border", "neutral_T_marker": "unrated design threat; no severity color or order", "control": "adopted planned control, not verified; ACTIVE is specification status only", "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"}

Boundary groups, source annotations, entry authentication/counts and precise ordering constraints are preserved in this diagram’s Model specification.

Omissions: Exact endpoint methods/paths and runtime topology are not evidenced. Local protocols beyond stated ports/adapters are not assigned wire protocols. No universal sensitivity class or risk score is invented. Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge.

Validation: Model IDs and flow references checked against stage08; not rendered.

## Attack Surface Map

ID: D09-05. Purpose: Enumerate every documented entry surface and policy. Audience: Security and API reviewers.

| Model ID | Element | Kind | Zone | Threats / controls |
| --- | --- | --- | --- | --- |
| S00-P1 | Selected media, folders and JPEG/PNG cover art | entry point | source-defined surface; grouped operations may cross zones | T-002, T-003, T-005, C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S00-P2 | MusicBrainz responses and native metadata rendering | entry point | source-defined surface; grouped operations may cross zones | T-003, T-005, T-011, C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S00-P3 | Public registration and sign-in HTTPS JSON | entry point | source-defined surface; grouped operations may cross zones | T-001, T-005, T-009, C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S00-P4 | Protected account, library and recommendation HTTPS JSON | entry point | source-defined surface; grouped operations may cross zones | T-001, T-004, T-005, T-006, T-008, T-010, T-012, C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S00-P5 | Local operator initial Admin command | entry point | source-defined surface; grouped operations may cross zones | T-001, C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S07-EP02 | Metadata manual entry and match selection | entry point | source-defined surface; grouped operations may cross zones | C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S07-EP03 | HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration | entry point | source-defined surface; grouped operations may cross zones | C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| S07-EP04 | MusicBrainz response ingress | entry point | source-defined surface; grouped operations may cross zones | C-SC-001, C-SC-002, C-SC-005, C-SC-006 |
| POST-EP01 | Local operator invitation issue command | entry point | source-defined surface; grouped operations may cross zones | T-001, T-009, T-017, C-SC-001, C-SC-002, C-SC-005, C-SC-006 |

| Connection | Source → destination | Data / protocol | Sensitivity | Boundaries |
| --- | --- | --- | --- | --- |

Text preview: S00-P1: Selected media, folders and JPEG/PNG cover art — No service account required for local/MusicBrainz functions; S00-P2: MusicBrainz responses and native metadata rendering — No service account required for local/MusicBrainz functions; S00-P3: Public registration and sign-in HTTPS JSON — Registration and sign-in precede established session; registration requires valid invitation; S00-P4: Protected account, library and recommendation HTTPS JSON — Valid unsuspended session required; S00-P5: Local operator initial Admin command — Local operator command; exact mechanism not specified; S07-EP02: Metadata manual entry and match selection — No service account required for local/MusicBrainz functions; S07-EP03: HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration — Not fully specified at this grouped granularity; S07-EP04: MusicBrainz response ingress — No service account required for local/MusicBrainz functions; POST-EP01: Local operator invitation issue command — Local operator command; concrete invocation not specified

Legend: {"arrow": "documented call/data direction; return to caller where stated", "dashed_border": "trust boundary; ordinary grouping has a labeled plain border", "neutral_T_marker": "unrated design threat; no severity color or order", "control": "adopted planned control, not verified; ACTIVE is specification status only", "sensitivity": "Only source-supplied personal-data classification is used; others say not classified"}

Boundary groups, source annotations, entry authentication/counts and precise ordering constraints are preserved in this diagram’s Model specification.

Omissions: Exact endpoint methods/paths and runtime topology are not evidenced. Local protocols beyond stated ports/adapters are not assigned wire protocols. No universal sensitivity class or risk score is invented. Operator bootstrap and logs have textual requirements but insufficient component/path detail for a concrete runtime edge.

Validation: Model IDs and flow references checked against stage08; not rendered.
