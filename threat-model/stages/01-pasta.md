# THREAT_MODEL_FRAGMENT

## Model
```json
{
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
  },
  "evidence": [
    {
      "id": "S01-E1",
      "file": "REQUIREMENTS.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    },
    {
      "id": "S01-E2",
      "file": "ARCHITECTURE.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    },
    {
      "id": "S01-E3",
      "file": "SECURITY.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    },
    {
      "id": "S01-E4",
      "file": "DESIGN.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    }
  ],
  "system": {
    "assets": [
      {
        "id": "S01-A1",
        "name": "Music files and recovery copies",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-A2",
        "name": "Local catalog, proposals, approvals and operation state",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-A3",
        "name": "Service accounts, sessions and release memberships",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-A4",
        "name": "Native desktop and recommendation API availability",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ],
    "actors": [
      {
        "id": "S01-U1",
        "name": "Current desktop user",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-U2",
        "name": "Participating service user",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-U3",
        "name": "Recommendation-service Admin",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-U4",
        "name": "Operator",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ],
    "data": [
      {
        "id": "S01-D1",
        "name": "Audio, editable metadata, identifiers, paths and images",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-D2",
        "name": "Username, password and session secret",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-D3",
        "name": "Shared release identifiers and account memberships",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-D4",
        "name": "Operation type, result, time and correlation ID security logs",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ],
    "zones": [
      {
        "id": "S01-Z1",
        "name": "Native desktop process",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-Z2",
        "name": "User filesystem",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-Z3",
        "name": "Recommendation service host",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-Z4",
        "name": "External MusicBrainz and browser Bandcamp services",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ],
    "boundaries": [
      {
        "id": "S01-B1",
        "name": "Filesystem to desktop media adapter",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-B2",
        "name": "Desktop to external services",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-B3",
        "name": "Desktop to authenticated recommendation API",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-B4",
        "name": "API handler to service domain authorization",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ],
    "flows": [
      {
        "id": "S01-F1",
        "name": "Import/query: presentation to local services to media/catalog and results",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-F2",
        "name": "Review/save/restore: local domain to filesystem and catalog",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-F3",
        "name": "Discovery: catalog to adapter to MusicBrainz to local domain/presentation",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-F4",
        "name": "Sharing/recommendations: desktop to API to domain to service store and results",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-F5",
        "name": "Purchase search: desktop adapter to OS browser and Bandcamp",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-F6",
        "name": "API operations to operator security logs",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ],
    "entry_points": [
      {
        "id": "S01-P1",
        "name": "Selected media, folders and JPEG/PNG cover art",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-P2",
        "name": "MusicBrainz responses and native metadata rendering",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-P3",
        "name": "Public registration and sign-in HTTPS JSON",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-P4",
        "name": "Protected account, library and recommendation HTTPS JSON",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S01-P5",
        "name": "Local operator initial Admin command",
        "evidence_ids": [
          "S01-E1",
          "S01-E2",
          "S01-E3"
        ],
        "status": "specified"
      }
    ]
  },
  "methods": [
    {
      "id": "S01-M",
      "name": "PASTA"
    }
  ],
  "threats": [
    {
      "id": "S01-T1",
      "title": "Approved edits can lose integrity during interrupted file operations",
      "category": "Tampering",
      "scenario": "Review, recovery creation, atomic replacement and catalog reconciliation cross independent persistence operations. A changed source or interruption threatens preservation and accurate saved-state reporting unless the specified sequence holds.",
      "affected_ids": [
        "S01-A1",
        "S01-A2",
        "S01-F2",
        "S01-B1"
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
        "S01-C2",
        "S01-C3"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S01-T2",
      "title": "Recommendation output can disclose participant memberships",
      "category": "Information Disclosure",
      "scenario": "Exact overlap-based ranking and counts may expose memberships of a small or distinctive eligible set, conflicting with the intended privacy outcome if that outcome includes inference resistance.",
      "affected_ids": [
        "S01-A3",
        "S01-D3",
        "S01-F4",
        "S01-P4"
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
        "S01-C1",
        "S01-C4",
        "S01-C8"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S01-T3",
      "title": "Unauthenticated work can consume bounded pilot capacity",
      "category": "Denial of Service",
      "scenario": "Registration and password sign-in precede authenticated account limits and consume a 100-account pilot and hashing/host resources. Their admission policy needs to preserve the closed-pilot and bounded-work objectives.",
      "affected_ids": [
        "S01-A3",
        "S01-A4",
        "S01-P3",
        "S01-B3"
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
        "S01-C1",
        "S01-C5",
        "S01-C7"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    }
  ],
  "controls": [
    {
      "id": "S01-C1",
      "source_id": "SC-001",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-001",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C2",
      "source_id": "SC-002",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-002",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C3",
      "source_id": "SC-003",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-003",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C4",
      "source_id": "SC-004",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-004",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C5",
      "source_id": "SC-005",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-005",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C6",
      "source_id": "SC-006",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-006",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C7",
      "source_id": "SC-007",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-007",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S01-C8",
      "source_id": "SC-008",
      "evidence_ids": [
        "S01-E3"
      ],
      "locator": "SECURITY.md SC-008",
      "status": "adopted, unimplemented and unverified"
    }
  ],
  "requirements": [],
  "risks": [],
  "attack_trees": [],
  "attack_paths": [
    {
      "id": "S01-AP1",
      "threat_id": "S01-T2",
      "steps": [
        "Participant submits a confirmed library",
        "Service computes eligible libraries by overlap",
        "Service returns ranked release identifiers/counts",
        "Caller may infer memberships where the eligible cohort is distinctive"
      ],
      "affected_ids": [
        "S01-D3",
        "S01-F4"
      ],
      "evidence_ids": [
        "S01-E1",
        "S01-E2"
      ],
      "control_ids": [
        "S01-C1",
        "S01-C4",
        "S01-C8"
      ],
      "assumptions": [
        "Actual cohort distinguishability and adversarial prior knowledge are unobserved; the final inference is conditional."
      ],
      "risk_ids": [],
      "status": "design path, not executed"
    }
  ],
  "visualizations": [],
  "coverage": [
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
      ]
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
      "gap_ids": []
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
      "gap_ids": []
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
      ]
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
      ]
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
      ]
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
      ]
    }
  ],
  "conflicts": [],
  "gaps": [
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
    }
  ]
}
```

## Summary
Objectives are explicit review, preservation, offline local use and discovery within a bounded closed pilot. Decomposition identifies local files/catalog, the remote account/membership store, external lookups and operator logs. All seven PASTA stages completed; the coverage records distinguish evidence gaps.

Three supported design scenarios concern media integrity, recommendation inference, and registration admission/resource consumption. The sole attack path is a conditional inference path over specified recommendation behavior; it was not executed. No demonstrated implementation weakness, incident, external intelligence or control effectiveness is claimed. Existing controls are adopted plans. No source conflict was established. Risk appetite, impact valuations, scoring, implementation evidence, closed-pilot admission and inference policy remain gaps; no numerical or qualitative risk ranking was invented.
