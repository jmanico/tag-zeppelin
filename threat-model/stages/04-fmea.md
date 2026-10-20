# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": [
    {
      "id": "S04-SCOPE",
      "description": "Specification-only analysis of native desktop and closed recommendation pilot; all four supplied specifications read independently for this method. No implementation or operational effectiveness claimed.",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a"
    }
  ],
  "evidence": [
    {
      "id": "S04-E1",
      "source": "REQUIREMENTS.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    },
    {
      "id": "S04-E2",
      "source": "ARCHITECTURE.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    },
    {
      "id": "S04-E3",
      "source": "SECURITY.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    },
    {
      "id": "S04-E4",
      "source": "DESIGN.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    }
  ],
  "methods": [
    {
      "id": "S04-M1",
      "name": "FMEA",
      "rating_method": "Not supplied; scenarios unranked; no likelihood, severity, cost, owner, deadline or residual-risk score inferred."
    }
  ],
  "threats": [
    {
      "id": "S04-T1",
      "title": "Approval, original file or catalog diverges during interrupted write",
      "function": "Review/save and recovery",
      "cause": "Filesystem and database operations are separate; process or disk failure is an explicitly specified test condition",
      "local_effect": "File/catalog disagreement or incorrect success display",
      "downstream_effect": "Loss of trustworthy saved state or retry state",
      "affected_ids": [
        "S04-A1"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.29\u2013FR-1.41; Interfaces and persistence; SC-003",
      "control_ids": [
        "S04-C3"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R1"
      ]
    },
    {
      "id": "S04-T2",
      "title": "Copy or destination has changed since it was recorded/reviewed",
      "function": "Recovery restore",
      "cause": "Recovery is retained until explicit deletion; path substitution checks exist, but persistent recovery-content integrity and changed-destination review are not fully specified",
      "local_effect": "Wrong prior contents or unintended current-file overwrite",
      "downstream_effect": "Recovery can destroy later valid edits",
      "affected_ids": [
        "S04-A1"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.31\u2013FR-1.32, FR-1.37\u2013FR-1.42; SC-003",
      "control_ids": [
        "S04-C2",
        "S04-C3"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain specified controls and their acceptance tests; unresolved restore semantics require an explicit decision.",
      "risk_ids": [
        "S04-R2"
      ]
    },
    {
      "id": "S04-T3",
      "title": "Malformed input exhausts resources or cannot be interpreted safely",
      "function": "Native import and display",
      "cause": "Untrusted media/cover/network inputs and decoder allocations",
      "local_effect": "One import or UI operation fails",
      "downstream_effect": "Loss of availability; processing other files must continue",
      "affected_ids": [
        "S04-A5"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.10\u2013FR-1.11, FR-1.22, FR-1.39; SC-002; DESIGN.md Rendering",
      "control_ids": [
        "S04-C2"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R3"
      ]
    },
    {
      "id": "S04-T4",
      "title": "Deletion commits but WAL cleanup fails",
      "function": "Shared-library mutation/deletion",
      "cause": "SC-008 explicitly anticipates checkpoint failure",
      "local_effect": "Logical deletion and cleanup have different completion states",
      "downstream_effect": "Premature success can misstate privacy status",
      "affected_ids": [
        "S04-A3"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-4.22, FR-4.27; SC-004, SC-008",
      "control_ids": [
        "S04-C4",
        "S04-C8"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R4"
      ]
    },
    {
      "id": "S04-T5",
      "title": "Eligibility changes between pages",
      "function": "Recommendation pagination",
      "cause": "Withdrawal, suspension or replacement changes membership revision",
      "local_effect": "Stale cursor or mixed result versions",
      "downstream_effect": "Withdrawn/suspended contributions exposed or ranking inconsistent",
      "affected_ids": [
        "S04-A4"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-3.11\u2013FR-3.16, FR-4.9, FR-4.13; SC-004",
      "control_ids": [
        "S04-C4",
        "S04-C5"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R5"
      ]
    },
    {
      "id": "S04-T6",
      "title": "Credential store, certificate or metadata endpoint unavailable",
      "function": "Credentials and network adapters",
      "cause": "Explicitly specified secure-storage, TLS and request-failure cases",
      "local_effect": "Sign-in persistence or online functions fail closed",
      "downstream_effect": "Local workflows must remain usable",
      "affected_ids": [
        "S04-A2"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "FR-1.17, FR-3.9, FR-4.20; NFR-2.1\u2013NFR-2.2; SC-005",
      "control_ids": [
        "S04-C5"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R6"
      ]
    },
    {
      "id": "S04-T7",
      "title": "Single service store unavailable or bounded workload misses target",
      "function": "Pilot storage and workload",
      "cause": "One API host and local SQLite store; persistent service backups deliberately excluded",
      "local_effect": "Service unavailable or membership/account data unavailable",
      "downstream_effect": "Service release blocked on workload failure; no persistent backup recovery promised",
      "affected_ids": [
        "S04-A6"
      ],
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ],
      "locator": "NFR-3.1; OD-005, OD-007; SC-007\u2013SC-008",
      "control_ids": [
        "S04-C1",
        "S04-C7",
        "S04-C8"
      ],
      "assumptions": [
        "Prospective failure mode; no occurrence or implementation failure established."
      ],
      "proposed_treatment": "Retain existing specified controls and verify their stated acceptance conditions.",
      "risk_ids": [
        "S04-R7"
      ]
    }
  ],
  "controls": [
    {
      "id": "S04-C1",
      "specification_id": "SC-001",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C2",
      "specification_id": "SC-002",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C3",
      "specification_id": "SC-003",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C4",
      "specification_id": "SC-004",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C5",
      "specification_id": "SC-005",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C6",
      "specification_id": "SC-006",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C7",
      "specification_id": "SC-007",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S04-C8",
      "specification_id": "SC-008",
      "evidence_ids": [
        "S04-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    }
  ],
  "requirements": [],
  "risks": [
    {
      "id": "S04-R1",
      "threat_ids": [
        "S04-T1"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    },
    {
      "id": "S04-R2",
      "threat_ids": [
        "S04-T2"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    },
    {
      "id": "S04-R3",
      "threat_ids": [
        "S04-T3"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    },
    {
      "id": "S04-R4",
      "threat_ids": [
        "S04-T4"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    },
    {
      "id": "S04-R5",
      "threat_ids": [
        "S04-T5"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    },
    {
      "id": "S04-R6",
      "threat_ids": [
        "S04-T6"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    },
    {
      "id": "S04-R7",
      "threat_ids": [
        "S04-T7"
      ],
      "method_id": "S04-M1",
      "status": "unranked",
      "residual_risk": "Not reassessed; no treated implementation exists."
    }
  ],
  "attack_trees": [],
  "attack_paths": [],
  "visualizations": [],
  "coverage": [
    {
      "id": "S04-CV1",
      "function": "Review/save and recovery",
      "status": "assessed",
      "threat_ids": [
        "S04-T1"
      ]
    },
    {
      "id": "S04-CV2",
      "function": "Recovery restore",
      "status": "assessed",
      "threat_ids": [
        "S04-T2"
      ]
    },
    {
      "id": "S04-CV3",
      "function": "Native import and display",
      "status": "assessed",
      "threat_ids": [
        "S04-T3"
      ]
    },
    {
      "id": "S04-CV4",
      "function": "Shared-library mutation/deletion",
      "status": "assessed",
      "threat_ids": [
        "S04-T4"
      ]
    },
    {
      "id": "S04-CV5",
      "function": "Recommendation pagination",
      "status": "assessed",
      "threat_ids": [
        "S04-T5"
      ]
    },
    {
      "id": "S04-CV6",
      "function": "Credentials and network adapters",
      "status": "assessed",
      "threat_ids": [
        "S04-T6"
      ]
    },
    {
      "id": "S04-CV7",
      "function": "Pilot storage and workload",
      "status": "assessed",
      "threat_ids": [
        "S04-T7"
      ]
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
      ]
    }
  ],
  "conflicts": [],
  "gaps": [
    {
      "id": "S04-G1",
      "description": "No runtime, failure history, verification results, or supplied risk prioritization method; this is not proof controls fail.",
      "evidence_ids": [
        "S04-E1",
        "S04-E2",
        "S04-E3",
        "S04-E4"
      ]
    },
    {
      "id": "S04-G2",
      "description": "Recovery-copy content integrity across retention and handling of legitimate destination edits before restore are not fully specified. Existing recorded-path and substitution checks do not by themselves decide these semantics.",
      "evidence_ids": [
        "S04-E1",
        "S04-E3"
      ]
    },
    {
      "id": "S04-G3",
      "description": "Service recovery objectives are absent. No-backup pilot policy is explicit, not an accidental absence; consequence requires acceptance/operational evidence, not an invented backup requirement.",
      "evidence_ids": [
        "S04-E2",
        "S04-E3"
      ]
    }
  ],
  "system": {
    "assets": [
      {
        "id": "S04-A1",
        "name": "Music files and recovery copies",
        "locator": "FR-1.26\u2013FR-1.43",
        "evidence_ids": [
          "S04-E1",
          "S04-E2",
          "S04-E4"
        ]
      },
      {
        "id": "S04-A2",
        "name": "Local review and catalog state",
        "locator": "Interfaces and persistence",
        "evidence_ids": [
          "S04-E1",
          "S04-E2",
          "S04-E4"
        ]
      },
      {
        "id": "S04-A3",
        "name": "Accounts, sessions and memberships",
        "locator": "FR-4.1\u2013FR-4.27",
        "evidence_ids": [
          "S04-E1",
          "S04-E2",
          "S04-E4"
        ]
      },
      {
        "id": "S04-A4",
        "name": "Recommendation results",
        "locator": "FR-3.2\u2013FR-3.16",
        "evidence_ids": [
          "S04-E1",
          "S04-E2",
          "S04-E4"
        ]
      },
      {
        "id": "S04-A5",
        "name": "Desktop presentation",
        "locator": "Components",
        "evidence_ids": [
          "S04-E1",
          "S04-E2",
          "S04-E4"
        ]
      },
      {
        "id": "S04-A6",
        "name": "Service availability",
        "locator": "NFR-3.1",
        "evidence_ids": [
          "S04-E1",
          "S04-E2",
          "S04-E4"
        ]
      }
    ],
    "actors": [],
    "data": [],
    "zones": [],
    "boundaries": [],
    "flows": [],
    "entry_points": []
  }
}
```

## Summary

Scope: seven prospective failure modes across the supplied functions. No incident history, rating factors, RPN formula or residual-risk reassessment was supplied; all items remain unranked. Controls are planned and untested. No conflicts identified.

| Function | Failure mode | Effect | Planned controls |
| --- | --- | --- | --- |
| Review/save and recovery | Approval, original file or catalog diverges during interrupted write | Loss of trustworthy saved state or retry state | SC-003 |
| Recovery restore | Copy or destination has changed since it was recorded/reviewed | Recovery can destroy later valid edits | SC-002, SC-003 |
| Native import and display | Malformed input exhausts resources or cannot be interpreted safely | Loss of availability; processing other files must continue | SC-002 |
| Shared-library mutation/deletion | Deletion commits but WAL cleanup fails | Premature success can misstate privacy status | SC-004, SC-008 |
| Recommendation pagination | Eligibility changes between pages | Withdrawn/suspended contributions exposed or ranking inconsistent | SC-004, SC-005 |
| Credentials and network adapters | Credential store, certificate or metadata endpoint unavailable | Local workflows must remain usable | SC-005 |
| Pilot storage and workload | Single service store unavailable or bounded workload misses target | Service release blocked on workload failure; no persistent backup recovery promised | SC-001, SC-007, SC-008 |

Common causes/cascades: disk/process failure links music-file replacement and catalog recovery; membership changes link deletion and pagination; network failures must not disable local functions. The existing treatments remain proposals for implementation and verification. Restore-copy integrity, changed-destination behavior, and service recovery objectives need explicit evidence or decisions. The deliberate no-backup policy is preserved.
