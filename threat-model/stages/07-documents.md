# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": {
    "id": "S07-SCOPE",
    "baseline": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
    "status": "Pre-implementation; adopted specifications are plans, not implemented or tested controls"
  },
  "evidence": [
    {
      "id": "S07-E01",
      "source": "REQUIREMENTS.md",
      "sections": "Entire document read",
      "type": "Product requirements",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha"
    },
    {
      "id": "S07-E02",
      "source": "ARCHITECTURE.md",
      "sections": "Entire document read",
      "type": "Adopted architecture",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha"
    },
    {
      "id": "S07-E03",
      "source": "SECURITY.md",
      "sections": "Entire document read",
      "type": "Adopted controls",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha"
    },
    {
      "id": "S07-E04",
      "source": "DESIGN.md",
      "sections": "Entire document read",
      "type": "Presentation targets",
      "date": "not supplied",
      "author": "not supplied",
      "currency": "unknown",
      "status": "adopted specification; no implementation/effectiveness evidence; DESIGN front matter alpha"
    }
  ],
  "system": {
    "assets": [
      {
        "id": "S07-A01",
        "name": "Native desktop presentation",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A02",
        "name": "Local application/domain services",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A03",
        "name": "Persistence/media adapters",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A04",
        "name": "Desktop discovery/sharing adapters",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A05",
        "name": "Service account/sharing domain",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A06",
        "name": "Recommendation calculation",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A07",
        "name": "Local SQLite catalog",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A08",
        "name": "Music files and recovery storage",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A09",
        "name": "Service SQLite store",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A10",
        "name": "MusicBrainz",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A11",
        "name": "OS browser/Bandcamp",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-A12",
        "name": "Fastify API",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      }
    ],
    "actors": [
      {
        "id": "S07-ACT01",
        "name": "Current local user",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      },
      {
        "id": "S07-ACT02",
        "name": "Participating service user",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      },
      {
        "id": "S07-ACT03",
        "name": "Recommendation-service Admin",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      },
      {
        "id": "S07-ACT04",
        "name": "Operator",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned"
      },
      {
        "id": "S07-ACT05",
        "name": "Project maintainer",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned"
      }
    ],
    "data": [
      {
        "id": "S07-D01",
        "name": "Audio, saved metadata and file paths",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      },
      {
        "id": "S07-D02",
        "name": "Pending proposals, approvals and recovery references",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-D03",
        "name": "Account identifiers, release memberships and security logs: personal data",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned"
      },
      {
        "id": "S07-D04",
        "name": "Password hashes and opaque-session digests; client credential-store token",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned"
      },
      {
        "id": "S07-D05",
        "name": "Previewed release identifier set",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      }
    ],
    "zones": [
      {
        "id": "S07-Z01",
        "name": "User desktop",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-Z02",
        "name": "Recommendation service",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-Z03",
        "name": "External MusicBrainz and OS browser/Bandcamp",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      }
    ],
    "boundaries": [
      {
        "id": "S07-B01",
        "name": "Desktop filesystem input and write boundary",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-B02",
        "name": "Desktop to recommendation API",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-B03",
        "name": "Desktop to external network services",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      }
    ],
    "flows": [
      {
        "id": "S07-F01",
        "name": "Presentation to local services to media/catalog and results",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-F02",
        "name": "Reviewed save/restore through local domain to filesystem/catalog",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-F03",
        "name": "Catalog to integration adapter to MusicBrainz to presentation",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-F04",
        "name": "Desktop to HTTPS JSON API to service domain/store and results",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-F05",
        "name": "Generated purchase search URL to OS browser",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      }
    ],
    "entry_points": [
      {
        "id": "S07-EP01",
        "name": "Selected files/folders and JPEG/PNG artwork",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP02",
        "name": "Metadata manual entry and match selection",
        "evidence_ids": [
          "S07-E01"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP03",
        "name": "HTTPS JSON registration, sign-in/out, replacement/withdrawal, recommendation, deletion, suspension/restoration",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP04",
        "name": "MusicBrainz response ingress",
        "evidence_ids": [
          "S07-E02"
        ],
        "status": "planned"
      },
      {
        "id": "S07-EP05",
        "name": "Local operator initial-Admin provisioning command",
        "evidence_ids": [
          "S07-E03"
        ],
        "status": "planned"
      }
    ]
  },
  "methods": [
    {
      "id": "S07-METHOD",
      "name": "document analysis"
    }
  ],
  "threats": [],
  "controls": [
    {
      "id": "S07-C01",
      "source_id": "SC-001",
      "name": "Service boundary controls",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-001",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C02",
      "source_id": "SC-002",
      "name": "Native input and rendering",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-002",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C03",
      "source_id": "SC-003",
      "name": "Approved writes and recovery integrity",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-003",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C04",
      "source_id": "SC-004",
      "name": "Sharing and deletion",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-004",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C05",
      "source_id": "SC-005",
      "name": "Credentials, sessions, and transport",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-005",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C06",
      "source_id": "SC-006",
      "name": "Domain authorization",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-006",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C07",
      "source_id": "SC-007",
      "name": "Build and host controls",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-007",
      "status": "adopted plan; not implemented or tested"
    },
    {
      "id": "S07-C08",
      "source_id": "SC-008",
      "name": "Privacy and operational evidence",
      "evidence_ids": [
        "S07-E03"
      ],
      "source_section": "SECURITY.md SC-008",
      "status": "adopted plan; not implemented or tested"
    }
  ],
  "requirements": [
    {
      "id": "S07-R01",
      "source": "REQUIREMENTS.md FR-1.1\u2013FR-4.27 and NFR-1.1\u2013NFR-3.1",
      "authority": "project specification",
      "edition": "not supplied",
      "status": "required product behavior; unverified",
      "applicability": "first release local native desktop and closed recommendation pilot",
      "evidence_ids": [
        "S07-E01"
      ]
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
      ]
    }
  ],
  "risks": [],
  "attack_trees": [],
  "attack_paths": [],
  "visualizations": [
    {
      "id": "S07-V01",
      "source": "ARCHITECTURE.md Data flow and trust boundaries",
      "type": "Mermaid flowchart",
      "status": "planned logical architecture; calls/access arrows with implicit response direction",
      "evidence_ids": [
        "S07-E02"
      ]
    }
  ],
  "coverage": [
    {
      "id": "S07-COV01",
      "category": "Assets",
      "documents": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ],
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; existing threat catalog and supplied numerical risk ratings absent"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
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
      "disposition": "Reviewed; extracted where supported; absent detail recorded as gaps"
    }
  ],
  "conflicts": [],
  "gaps": [
    {
      "id": "S07-G01",
      "description": "Document dates and authors not supplied; no runtime or test evidence. Component responsibilities exist, but individual component owners not supplied. Currency unknown, not stale.",
      "evidence_ids": [
        "S07-E01",
        "S07-E02",
        "S07-E03",
        "S07-E04"
      ]
    },
    {
      "id": "S07-G02",
      "description": "Concrete HTTP methods/paths, schema versions, pagination cursor integrity format, and normalization rules for usernames are not defined. Authentication and authorization intent is defined; absent detail is not proof of a bypass.",
      "evidence_ids": [
        "S07-E02",
        "S07-E03"
      ]
    },
    {
      "id": "S07-G03",
      "description": "Queued-work bound lacks a chosen capacity; registration has no explicit unauthenticated throttle; outbound response/metadata/parser work bounds beyond image limits and deadlines are not specified. Existing capacity, body, page and rate limits remain adopted.",
      "evidence_ids": [
        "S07-E03"
      ]
    },
    {
      "id": "S07-G04",
      "description": "Public-launch jurisdiction, processing basis, notice and license evidence is required by SC-008 but values are absent; pilot obligations are explicitly not waived.",
      "evidence_ids": [
        "S07-E03"
      ]
    },
    {
      "id": "S07-G05",
      "description": "Exact ranked identifiers/counts and repeated user-controlled library submissions are specified, but privacy inference resistance and accepted residual disclosure are not settled. No direct identity/full-library endpoint is allowed.",
      "evidence_ids": [
        "S07-E01",
        "S07-E02",
        "S07-E03"
      ]
    },
    {
      "id": "S07-G06",
      "description": "Owner-only recovery copies, file identity binding, and atomic replacement are specified; hard-link aliases, cross-process serialization, precise platform identity strategy, and crash-safe deletion-completion coordination are not detailed. No actual race is demonstrated.",
      "evidence_ids": [
        "S07-E01",
        "S07-E02",
        "S07-E03"
      ]
    }
  ]
}
```

## Summary

All four supplied documents were read completely and processed through all ten extraction categories. REQUIREMENTS.md supplies actors, data, operations, exclusions and acceptance scope; ARCHITECTURE.md supplies logical modules, adopted technologies, directional calls, storage and dependency constraints; SECURITY.md supplies eight adopted control groups and release gates; DESIGN.md supplies native interaction, review, confirmation, accessibility and plain-text rendering targets. Dates and authors are absent; DESIGN has alpha front matter. None proves runtime enforcement.

No material direct contradiction was established. File-identity safety and per-file serialization are specified, while alias/concurrency mechanics remain unspecified; this is a gap, not a contradiction. No external standard mapping, risk rating, legal conclusion or implementation vulnerability was inferred.

Additional decision documentation is needed for concrete API contracts/normalization, resource budgets beyond stated limits, recommendation inference expectations, platform file-identity coordination and deletion completion, and the release-eligibility evidence already required by SC-008. Exact dependencies, test and operational evidence belong to future implementation/release verification. All eight existing control groups remain adopted plans.
