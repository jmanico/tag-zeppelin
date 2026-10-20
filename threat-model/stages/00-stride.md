# THREAT_MODEL_FRAGMENT

## Model
```json
{
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
  },
  "evidence": [
    {
      "id": "S00-E1",
      "file": "REQUIREMENTS.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    },
    {
      "id": "S00-E2",
      "file": "ARCHITECTURE.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    },
    {
      "id": "S00-E3",
      "file": "SECURITY.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
    },
    {
      "id": "S00-E4",
      "file": "DESIGN.md",
      "locator": "entire file",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification; no implementation or verification evidence"
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
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-A2",
        "name": "Local catalog, proposals, approvals and operation state",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-A3",
        "name": "Service accounts, sessions and release memberships",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-A4",
        "name": "Native desktop and recommendation API availability",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ],
    "actors": [
      {
        "id": "S00-U1",
        "name": "Current desktop user",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-U2",
        "name": "Participating service user",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-U3",
        "name": "Recommendation-service Admin",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-U4",
        "name": "Operator",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ],
    "data": [
      {
        "id": "S00-D1",
        "name": "Audio, editable metadata, identifiers, paths and images",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-D2",
        "name": "Username, password and session secret",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-D3",
        "name": "Shared release identifiers and account memberships",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-D4",
        "name": "Operation type, result, time and correlation ID security logs",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ],
    "zones": [
      {
        "id": "S00-Z1",
        "name": "Native desktop process",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-Z2",
        "name": "User filesystem",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-Z3",
        "name": "Recommendation service host",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-Z4",
        "name": "External MusicBrainz and browser Bandcamp services",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ],
    "boundaries": [
      {
        "id": "S00-B1",
        "name": "Filesystem to desktop media adapter",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-B2",
        "name": "Desktop to external services",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-B3",
        "name": "Desktop to authenticated recommendation API",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-B4",
        "name": "API handler to service domain authorization",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ],
    "flows": [
      {
        "id": "S00-F1",
        "name": "Import/query: presentation to local services to media/catalog and results",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-F2",
        "name": "Review/save/restore: local domain to filesystem and catalog",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-F3",
        "name": "Discovery: catalog to adapter to MusicBrainz to local domain/presentation",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-F4",
        "name": "Sharing/recommendations: desktop to API to domain to service store and results",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-F5",
        "name": "Purchase search: desktop adapter to OS browser and Bandcamp",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-F6",
        "name": "API operations to operator security logs",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ],
    "entry_points": [
      {
        "id": "S00-P1",
        "name": "Selected media, folders and JPEG/PNG cover art",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-P2",
        "name": "MusicBrainz responses and native metadata rendering",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-P3",
        "name": "Public registration and sign-in HTTPS JSON",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-P4",
        "name": "Protected account, library and recommendation HTTPS JSON",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      },
      {
        "id": "S00-P5",
        "name": "Local operator initial Admin command",
        "evidence_ids": [
          "S00-E1",
          "S00-E2",
          "S00-E3"
        ],
        "status": "specified"
      }
    ]
  },
  "methods": [
    {
      "id": "S00-M",
      "name": "STRIDE"
    }
  ],
  "threats": [
    {
      "id": "S00-T1",
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
        "S00-C1",
        "S00-C5",
        "S00-C6"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S00-T2",
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
        "S00-C2",
        "S00-C3"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S00-T3",
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
        "S00-C2"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S00-T4",
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
        "S00-C1",
        "S00-C4",
        "S00-C8"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S00-T5",
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
        "S00-C1",
        "S00-C2",
        "S00-C5",
        "S00-C7"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    },
    {
      "id": "S00-T6",
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
        "S00-C4",
        "S00-C5",
        "S00-C8"
      ],
      "assumptions": [],
      "risk_ids": [],
      "status": "design threat; not an observed vulnerability"
    }
  ],
  "controls": [
    {
      "id": "S00-C1",
      "source_id": "SC-001",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-001",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C2",
      "source_id": "SC-002",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-002",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C3",
      "source_id": "SC-003",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-003",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C4",
      "source_id": "SC-004",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-004",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C5",
      "source_id": "SC-005",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-005",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C6",
      "source_id": "SC-006",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-006",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C7",
      "source_id": "SC-007",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-007",
      "status": "adopted, unimplemented and unverified"
    },
    {
      "id": "S00-C8",
      "source_id": "SC-008",
      "evidence_ids": [
        "S00-E3"
      ],
      "locator": "SECURITY.md SC-008",
      "status": "adopted, unimplemented and unverified"
    }
  ],
  "requirements": [],
  "risks": [],
  "attack_trees": [],
  "attack_paths": [],
  "visualizations": [],
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
            "S00-T2"
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
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
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
            "S00-T2"
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
      ]
    },
    {
      "id": "S00-CV3",
      "element_id": "S00-A3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
          ]
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T6"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T4"
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
      ]
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
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
      ]
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
      ]
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
      ]
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
      ]
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
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
    },
    {
      "id": "S00-CV10",
      "element_id": "S00-D2",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
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
      ]
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
            "S00-T6"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T4"
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
      ]
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
      ]
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
      ]
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
      ]
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
      ]
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
      ]
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
            "S00-T2"
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
    },
    {
      "id": "S00-CV19",
      "element_id": "S00-B3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
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
            "S00-T4"
          ]
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T5"
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
      ]
    },
    {
      "id": "S00-CV20",
      "element_id": "S00-B4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
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
      ]
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
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
            "S00-T2"
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
      ]
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
    },
    {
      "id": "S00-CV24",
      "element_id": "S00-F4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
          ]
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T6"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T4"
          ]
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T5"
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
      ]
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
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
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
      ]
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
            "S00-T2"
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
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
            "S00-T5"
          ]
        },
        "Elevation of Privilege": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T3"
          ]
        }
      },
      "evidence_ids": [
        "S00-E1",
        "S00-E2",
        "S00-E3",
        "S00-E4"
      ]
    },
    {
      "id": "S00-CV29",
      "element_id": "S00-P3",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
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
            "S00-T5"
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
      ]
    },
    {
      "id": "S00-CV30",
      "element_id": "S00-P4",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
          ]
        },
        "Tampering": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T6"
          ]
        },
        "Repudiation": {
          "status": "assessed: no separate evidenced scenario",
          "threat_ids": []
        },
        "Information Disclosure": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T4"
          ]
        },
        "Denial of Service": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T5"
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
      ]
    },
    {
      "id": "S00-CV31",
      "element_id": "S00-P5",
      "method_id": "S00-M",
      "dispositions": {
        "Spoofing": {
          "status": "assessed: evidenced design scenario",
          "threat_ids": [
            "S00-T1"
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
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
      "status": "missing evidence, not demonstrated defect"
    }
  ]
}
```

## Summary
Scope is the native local editor and closed recommendation pilot; exclusions are preserved in the model. The system crosses filesystem, external-service and recommendation API boundaries. All four specifications were assessed; adopted controls are unimplemented and unverified.

| STRIDE category | Coverage |
| --- | --- |
| Spoofing | S00-T1 |
| Tampering | S00-T2, S00-T6 |
| Repudiation | Assessed; no separate evidenced scenario |
| Information Disclosure | S00-T4 |
| Denial of Service | S00-T5 |
| Elevation of Privilege | S00-T3 |

Per-element dispositions are in coverage. Six design threats retain their existing control references; none is a demonstrated exploit. No source conflicts were established. Gaps concern verification, recommendation inference policy, resource/admission bounds, and absent risk scoring; threats remain unrated.
