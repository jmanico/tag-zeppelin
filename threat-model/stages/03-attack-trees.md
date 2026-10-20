# THREAT_MODEL_FRAGMENT

## Model

```json
{
  "scope": [
    {
      "id": "S03-SCOPE",
      "description": "Specification-only analysis of native desktop and closed recommendation pilot; all four supplied specifications read independently for this method. No implementation or operational effectiveness claimed.",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a"
    }
  ],
  "evidence": [
    {
      "id": "S03-E1",
      "source": "REQUIREMENTS.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    },
    {
      "id": "S03-E2",
      "source": "ARCHITECTURE.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    },
    {
      "id": "S03-E3",
      "source": "SECURITY.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    },
    {
      "id": "S03-E4",
      "source": "DESIGN.md",
      "locator": "entire document",
      "revision": "e346ef231f549b15ead023bcfbea44ac4e69e59a",
      "status": "adopted specification, not implementation evidence"
    }
  ],
  "methods": [
    {
      "id": "S03-M1",
      "name": "Attack trees",
      "rating_method": "Not supplied; scenarios unranked; no likelihood, severity, cost, owner, deadline or residual-risk score inferred."
    }
  ],
  "threats": [
    {
      "id": "S03-T1",
      "title": "Unauthorized music-file change",
      "tree_id": "S03-AT1",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-1.5, FR-1.23\u2013FR-1.43; SC-002\u2013SC-003",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "S03-C2",
        "S03-C3"
      ]
    },
    {
      "id": "S03-T2",
      "title": "Unauthorized account or shared-library change",
      "tree_id": "S03-AT2",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-4.3, FR-4.11\u2013FR-4.26; DR-5; SC-001, SC-005\u2013SC-006",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "S03-C1",
        "S03-C5",
        "S03-C6"
      ]
    },
    {
      "id": "S03-T3",
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
        "S03-C4",
        "S03-C5"
      ]
    },
    {
      "id": "S03-T4",
      "title": "Unconfirmed library disclosure",
      "tree_id": "S03-AT4",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-4.4\u2013FR-4.7; SC-004; DESIGN.md Accounts and sharing",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "S03-C4"
      ]
    },
    {
      "id": "S03-T5",
      "title": "Service exhaustion prevents recommendation access",
      "tree_id": "S03-AT5",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-4.2, FR-4.23\u2013FR-4.24; NFR-3.1; SC-001",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "S03-C1",
        "S03-C7"
      ]
    },
    {
      "id": "S03-T6",
      "title": "Hostile content controls native rendering or browser handoff",
      "tree_id": "S03-AT6",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ],
      "locator": "FR-3.5\u2013FR-3.6, FR-3.17; SC-002; DESIGN.md Rendering",
      "status": "supported adverse objective; exploitation not demonstrated",
      "control_ids": [
        "S03-C2"
      ]
    }
  ],
  "controls": [
    {
      "id": "S03-C1",
      "specification_id": "SC-001",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C2",
      "specification_id": "SC-002",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C3",
      "specification_id": "SC-003",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C4",
      "specification_id": "SC-004",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C5",
      "specification_id": "SC-005",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C6",
      "specification_id": "SC-006",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C7",
      "specification_id": "SC-007",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    },
    {
      "id": "S03-C8",
      "specification_id": "SC-008",
      "evidence_ids": [
        "S03-E3"
      ],
      "status": "adopted planned control; unimplemented and untested"
    }
  ],
  "requirements": [],
  "risks": [],
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
            "S03-A1"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C2",
            "S03-C3"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N11",
          "name": "Attacker-controlled input reaches a selected file or review proposal",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A1"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C2",
            "S03-C3"
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
            "S03-A1"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C2",
            "S03-C3"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ]
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
            "S03-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C1",
            "S03-C5",
            "S03-C6"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N21",
          "name": "Unauthenticated, non-owner, suspended or non-Admin request reaches a service operation",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C1",
            "S03-C5",
            "S03-C6"
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
            "S03-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C1",
            "S03-C5",
            "S03-C6"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ]
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
            "S03-C4",
            "S03-C5"
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
            "S03-C4",
            "S03-C5"
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
            "S03-C4",
            "S03-C5"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ]
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
            "S03-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C4"
          ],
          "assumptions": []
        },
        {
          "id": "S03-N41",
          "name": "Previewed set changes before submission without renewed confirmation",
          "operator": "leaf",
          "children": [],
          "affected_ids": [
            "S03-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C4"
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
            "S03-A3"
          ],
          "evidence_ids": [
            "S03-E1",
            "S03-E3"
          ],
          "control_ids": [
            "S03-C4"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ]
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
            "S03-C1",
            "S03-C7"
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
            "S03-C1",
            "S03-C7"
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
            "S03-C1",
            "S03-C7"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ]
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
            "S03-C2"
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
            "S03-C2"
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
            "S03-C2"
          ],
          "assumptions": [
            "Control-failure branch is conditional and not demonstrated; specification-only evidence."
          ]
        }
      ]
    }
  ],
  "attack_paths": [
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
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
      "rationale": "All AND prerequisites required; OR alternatives independent. No comparative ranking."
    }
  ],
  "visualizations": [],
  "coverage": [
    {
      "id": "S03-CV1",
      "status": "assessed",
      "description": "Six roots cover file integrity, access control, sharing privacy, native content, and availability. Each node reachable; child references resolve. Control IDs are shared defenses across roots; no leaf is duplicated across trees. No supplied authoritative CAPEC material; identifiers omitted.",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ]
    }
  ],
  "conflicts": [],
  "gaps": [
    {
      "id": "S03-G1",
      "description": "No runtime, failure history, verification results, or supplied risk prioritization method; this is not proof controls fail.",
      "evidence_ids": [
        "S03-E1",
        "S03-E2",
        "S03-E3",
        "S03-E4"
      ]
    },
    {
      "id": "S03-G2",
      "description": "Registration exists and password hashing is resource-intensive under SC-005, but SC-001 specifies sign-in and authenticated limits only. Registration admission/rate budget and closed-pilot enrollment mechanism are not specified; no exploit is demonstrated.",
      "evidence_ids": [
        "S03-E1",
        "S03-E3"
      ]
    }
  ],
  "system": {
    "assets": [
      {
        "id": "S03-A1",
        "name": "Music files and recovery copies",
        "locator": "FR-1.26\u2013FR-1.43",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4"
        ]
      },
      {
        "id": "S03-A2",
        "name": "Local review and catalog state",
        "locator": "Interfaces and persistence",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4"
        ]
      },
      {
        "id": "S03-A3",
        "name": "Accounts, sessions and memberships",
        "locator": "FR-4.1\u2013FR-4.27",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4"
        ]
      },
      {
        "id": "S03-A4",
        "name": "Recommendation results",
        "locator": "FR-3.2\u2013FR-3.16",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4"
        ]
      },
      {
        "id": "S03-A5",
        "name": "Desktop presentation",
        "locator": "Components",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4"
        ]
      },
      {
        "id": "S03-A6",
        "name": "Service availability",
        "locator": "NFR-3.1",
        "evidence_ids": [
          "S03-E1",
          "S03-E2",
          "S03-E4"
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

Scope: desktop and recommendation pilot; six conditional adverse goals, not demonstrated vulnerabilities. All controls are adopted plans. No conflicts identified. No ranking method or implementation evidence exists.

```text
1. Unauthorized music-file change [AND]
   Attacker-controlled input reaches a selected file or review proposal
   Approval binding, identity checking, or mandatory write sequence fails
2. Unauthorized account or shared-library change [AND]
   Unauthenticated, non-owner, suspended or non-Admin request reaches a service operation
   Authentication or domain authorization fails
3. Disclosure of a withdrawn or suspended library through a stale result [AND]
   Membership eligibility changes during paginated calculation
   Cursor revision or per-page eligibility checks fail
4. Unconfirmed library disclosure [OR]
   Previewed set changes before submission without renewed confirmation
   A retry or background action submits unconfirmed local changes
5. Service exhaustion prevents recommendation access [OR]
   Request, queue or capacity bounds fail
   Expensive unauthenticated registration work is admitted without an evidenced admission budget
6. Hostile content controls native rendering or browser handoff [OR]
   Imported or returned metadata is interpreted rather than displayed as text
   Untrusted metadata supplies an executable URL or shell command to link opening
```

AND paths require both leaves; OR leaves are alternatives. Paths are conditional on unverified control failure. Shared defenses are input validation (SC-002), session/authentication and authorization (SC-001/005/006), and immutable sharing/revision handling (SC-004). Registration admission is an explicit specification gap. No practical exploit instructions or CAPEC identifiers are asserted.
