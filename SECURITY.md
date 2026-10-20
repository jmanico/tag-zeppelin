# Secure Coding

## Secure-Coding Inputs

- Read: `REQUIREMENTS.md`, `DESIGN.md`, and `ARCHITECTURE.md`. Existing `SECURITY.md`: absent; no prior SC or OD identifiers to preserve. Security notes: none supplied.
- Authority: requirements own behavior, data, integrations, and obligations; design owns interaction and rendering; architecture owns components, interfaces, flows, and boundaries. Corpus guidance does not establish project facts.
- Confirmed scope: a desktop music-tagging application with local file import, metadata review, explicit approval, recovery copies, MusicBrainz lookup, and Bandcamp search links. Local functions work without an account or network (`REQUIREMENTS.md`, FR-1.1–FR-1.35, FR-3.5–FR-3.6, FR-4.1, NFR-2.1).
- Confirmed service scope: signed-in shared-library submissions and recommendations; optional sharing of release identifiers only; owner/Admin restrictions; withdrawal, account deletion, suspension, and protection of other users' identities and complete libraries (`REQUIREMENTS.md`, FR-4.2–FR-4.15).
- Confirmed enforcement points: local application/domain services enforce approval and recovery; media and network adapters receive untrusted input; the recommendation API repeats validation, authentication, ownership, and role checks. The service has no access path to local media or catalog (`ARCHITECTURE.md`, “Components and Flows,” “Main flows and trust boundaries,” DR-1–DR-6).
- Confirmed presentation: current/proposed values and cover previews, explicit approval and recovery confirmation, sharing preview, separate Admin controls, and visible per-file results (`DESIGN.md`, “Components”). Browser handoff is for Bandcamp search links (`ARCHITECTURE.md`, “APIs and integrations”); an application browser renderer is not confirmed.
- Technology names supplied in `ARCHITECTURE.md`, “Required Architecture Inputs”: Node.js, Fastify, and QT. Versions are `UNKNOWN`. Runtime/framework labels conflict; the corrected interpretation is explicitly `PROPOSED`, not confirmed (OD-001).
- C++, Qt Widgets, SQLite, TagLib, HTTPS JSON, password credentials, and opaque sessions are proposals, not adopted selections. Language versions, modules, plugins, toolchains, hosting, scale, and detailed security configuration are `UNKNOWN`. OPA and Docker adoption are `UNKNOWN` (OD-002–OD-007).
- Applicable legal obligations are explicitly `UNKNOWN` (`REQUIREMENTS.md`, “Required Requirement Inputs”). Product privacy requirements are confirmed independently (OD-008).
- `ARCHITECTURE.md`, “Open Questions,” retains unknowns and proposed decisions despite saying no questions remain. That wording does not confirm them. No requirements/design conflict was identified; the technology-label conflict remains unresolved here.

## Selected Prompts

Corpus root: `/Users/jmanico/Dropbox/github/aegis/secure-coding-knowledge`. All corpus paths below are relative to this root. Candidate manifests, prompt text, source records, shared preamble, and resolver output were inspected. Corpus review versions describe the corpus, not this project or independently verified current releases.

Direct selection evidence:

- `js/nodejs/26` — **TO BE DECIDED**, not selected. Node.js is named, but its role conflicts and version is `UNKNOWN` (`ARCHITECTURE.md`, “Required Architecture Inputs,” “Technology interpretation and scope”; OD-001).
- `native/qt/6.11` — **TO BE DECIDED**, not selected. QT is named; version is `UNKNOWN`, and C++/Widgets are proposed (same architecture sections; OD-002).
- `js/fastify/5.12` — **TO BE DECIDED**, not selected. Fastify is named; version is `UNKNOWN`, and the role interpretation remains proposed (same architecture sections; OD-001).
- `policy/open-policy-agent/1.20` — **TO BE DECIDED**, not selected. No authoritative document confirms OPA, Rego, or a policy gateway. Its general-sounding candidate label does not make this an application-independent baseline (OD-004).
- `infra/dockerfile/1` — **TO BE DECIDED**, not selected. Hosting is `UNKNOWN`; Dockerfile syntax 1, BuildKit, and Linux containers are not confirmed (`ARCHITECTURE.md`, “Required Architecture Inputs”; OD-005).

Eligible ordered composition: **empty**. No direct or transitive pack is `SELECTED`. Unconfirmed parent versions cannot supply active rules independently of their blocked children.

Preamble, listed separately: `content/preamble.md`, “Applying these prompts.” It provides application and verification guidance, not technology eligibility or substantive project controls. Its conflict-resolution guidance does not override the instruction to record unresolved conflicts. It is not used to manufacture implementation rules from ineligible packs.

Resolved candidate composition below is a dependency audit only, **not an adopted composition**. Running `scripts/resolve_prompt.py` with the five candidates in their supplied order yields:

1. **Transitive** `js/javascript/ES2026`: `content/js/javascript/ES2026/prompt.md`; `content/js/javascript/ES2026/sources.md`. Included by Node.js 26, Node.js 24, and TypeScript 7. ES2026 scope is unconfirmed (OD-003).
2. **Direct** `js/nodejs/26`: `content/js/nodejs/26/prompt.md`; `content/js/nodejs/26/sources.md`. Declares ES2026. Project runtime version is unconfirmed (OD-001).
3. **Transitive** `native/cpp/C++23`: `content/native/cpp/C++23/prompt.md`; `content/native/cpp/C++23/sources.md`. Included by Qt 6.11. C++ is proposed and C++23/toolchain adoption is unconfirmed (OD-002).
4. **Direct** `native/qt/6.11`: `content/native/qt/6.11/prompt.md`; `content/native/qt/6.11/sources.md`. Declares C++23. The sources distinguish this application baseline from Qt's own language requirement; neither establishes project adoption (OD-002).
5. **Transitive** `js/typescript/7`: `content/js/typescript/7/prompt.md`; `content/js/typescript/7/sources.md`. Included by Fastify 5.12; declares ES2026. TypeScript use and version are unconfirmed (OD-003).
6. **Direct** `js/fastify/5.12`: `content/js/fastify/5.12/prompt.md`; `content/js/fastify/5.12/sources.md`. Declares Node.js 24 and TypeScript 7; project applicability is unresolved (OD-001, OD-003).
7. **Direct** `policy/open-policy-agent/1.20`: `content/policy/open-policy-agent/1.20/prompt.md`; `content/policy/open-policy-agent/1.20/sources.md`. No parents; scope is OPA 1.20 and Rego v1, not generic authorization (OD-004).
8. **Direct** `infra/dockerfile/1`: `content/infra/dockerfile/1/prompt.md`; `content/infra/dockerfile/1/sources.md`. No parents; scope is Dockerfile syntax 1 with BuildKit for Linux containers (OD-005).

Additional transitive dependency inspected: `js/nodejs/24`, with `content/js/nodejs/24/prompt.md` and `content/js/nodejs/24/sources.md`; it declares ES2026. Fastify's standalone dependency order is ES2026 → Node.js 24 → TypeScript 7 → Fastify 5.12. The combined candidate resolver substitutes directly requested Node.js 26 for Node.js 24. This mechanical precedence is not evidence of project compatibility or approval; the mismatch remains **TO BE DECIDED** (OD-001). Each pack's include provenance is its adjacent `manifest.json`.

Source inconsistency: the Fastify source introduction states a 5.12.5 security floor, while a later paragraph records removing that floor. No floor is adopted here (OD-009).

## Secure-Coding Rules

No active rules have eligible substantive prompt provenance yet. Confirmed project requirements remain authoritative; these blocked coverage entries neither suspend those requirements nor introduce implementation instructions. Each entry awaits the identified facts and an eligible, applicable source before receiving an active rule and pass/fail verification.

**SC-001 — Service boundary controls**
- **Status:** BLOCKED
- **Dependency:** Confirmed server roles, versions, language scope, and eligible composition (OD-001, OD-003). Coverage: service-side validation, authentication, ownership/Admin enforcement, and private recommendation responses. Grounding: `REQUIREMENTS.md`, FR-4.3, FR-4.10–FR-4.15; `ARCHITECTURE.md`, “Main flows and trust boundaries,” DR-4–DR-5.

**SC-002 — Desktop input and rendering controls**
- **Status:** BLOCKED
- **Dependency:** Confirmed Qt version, language/toolchain, modules, and eligible native prompts (OD-002). Coverage: media and network input validation, metadata/cover rendering, and browser link handoff. Grounding: `REQUIREMENTS.md`, FR-1.20–FR-1.22, FR-3.5–FR-3.6; `DESIGN.md`, “Components”; `ARCHITECTURE.md`, “APIs and integrations,” “Main flows and trust boundaries.”

**SC-003 — Approved writes and recovery integrity**
- **Status:** BLOCKED
- **Dependency:** Eligible native sources and adopted media/persistence mechanisms with compatibility evidence (OD-002, OD-007). Coverage: approval enforcement, complete recovery copies, preservation of audio/unapproved tags, restoration confirmation, and interrupted writes. Grounding: `REQUIREMENTS.md`, FR-1.5, FR-1.23–FR-1.34; `ARCHITECTURE.md`, “Persistence and file integrity,” DR-3.

**SC-004 — Sharing and deletion controls**
- **Status:** BLOCKED
- **Dependency:** Eligible client/service composition and adopted persistence interfaces (OD-001, OD-002, OD-003, OD-007). Coverage: confirmed release-only submissions, no automatic sharing, deletion before success, and exclusion of withdrawn/suspended libraries. Grounding: `REQUIREMENTS.md`, FR-4.4–FR-4.9, FR-4.13–FR-4.14; `ARCHITECTURE.md`, “Authentication, privacy, and recommendation rules,” DR-6.

**SC-005 — Credentials, sessions, and transport**
- **Status:** BLOCKED
- **Dependency:** Adopted authentication/session/transport design and eligible version-specific sources (OD-001, OD-002, OD-006). Grounding: `REQUIREMENTS.md`, FR-4.2–FR-4.3; proposed mechanisms in `ARCHITECTURE.md`, “Authentication, privacy, and recommendation rules,” and “Required Architecture Inputs.”

**SC-006 — Policy-engine controls**
- **Status:** BLOCKED
- **Dependency:** Evidence of OPA adoption, version, and enforcement integration (OD-004). No confirmed project policy-engine component exists to enforce this candidate coverage.

**SC-007 — Container build controls**
- **Status:** BLOCKED
- **Dependency:** Confirmed container/build platform and applicable versions (OD-005). Hosting is `UNKNOWN`; desktop Linux support does not establish Linux container deployment.

**SC-008 — Obligation-specific data controls**
- **Status:** BLOCKED
- **Dependency:** Documented applicable obligations and affected data, plus eligible supporting sources (OD-008). Grounding: `REQUIREMENTS.md`, “Required Requirement Inputs.” No legal retention period or assurance requirement is inferred.

## Open Security Decisions

**OD-001 — Server roles, versions, and parent mismatch**
- **Unresolved:** Role-label conflict is **TO BE DECIDED**; Node.js/Fastify versions are `UNKNOWN`. Evidence needed: authoritative confirmation of roles and versions, then source-backed applicability review of Fastify's Node.js 24 baseline versus candidate Node.js 26. Resolver precedence alone cannot resolve this.
- **Affected:** SC-001, SC-004, SC-005; `js/nodejs/26`, `js/fastify/5.12`, transitive `js/nodejs/24`.
- **Owner:** UNKNOWN.

**OD-002 — Desktop framework and native baseline**
- **Unresolved:** Qt version, language standard, toolchain, and modules are `UNKNOWN`; proposed C++/Widgets adoption is **TO BE DECIDED**. Evidence needed: authoritative selections and compatibility evidence for the documented Windows, macOS, and Ubuntu acceptance platforms. Optional Qt modules cannot be inferred.
- **Affected:** SC-002–SC-005; `native/qt/6.11`, `native/cpp/C++23`.
- **Owner:** UNKNOWN.

**OD-003 — JavaScript and TypeScript applicability**
- **Unresolved:** ES2026 target and TypeScript use/version are `UNKNOWN`. Evidence needed: authoritative server language/build selections and compatibility review. A manifest include is not confirmation that this project uses TypeScript 7.
- **Affected:** SC-001, SC-004; `js/javascript/ES2026`, `js/typescript/7`, and Fastify composition eligibility.
- **Owner:** UNKNOWN.

**OD-004 — Policy engine applicability**
- **Unresolved:** OPA/Rego adoption and version are `UNKNOWN`; selection is **TO BE DECIDED**. Evidence needed: an authoritative decision establishing applicability or non-applicability, and, if adopted, the policy interface and enforcement component. Existing owner/Admin requirements do not imply OPA.
- **Affected:** SC-006; `policy/open-policy-agent/1.20`.
- **Owner:** UNKNOWN.

**OD-005 — Build and hosting applicability**
- **Unresolved:** Hosting, containers, Dockerfile syntax, builder, and runtime versions are `UNKNOWN`. Evidence needed: authoritative deployment/build decisions establishing applicability or non-applicability and the platform scope for any selected container pack.
- **Affected:** SC-007; `infra/dockerfile/1`.
- **Owner:** UNKNOWN.

**OD-006 — Authentication and transport mechanisms**
- **Unresolved:** Passwords, opaque sessions, operating-system credential storage, and HTTPS JSON remain proposed; detailed controls are **TO BE DECIDED**. Evidence needed: adopted credential/session lifecycle, Admin provisioning, transport ownership, and interface contracts, with configuration requirements sufficient for testable controls. Limits and algorithms are not supplied here.
- **Affected:** SC-005; credential, session, transport, and request-resource coverage in otherwise eligible client/server packs.
- **Owner:** UNKNOWN.

**OD-007 — Media and persistence mechanisms**
- **Unresolved:** SQLite and TagLib adoption is **TO BE DECIDED**; versions and adapter compatibility are `UNKNOWN`. Evidence needed: adopted adapters/storage interfaces, supported-format preservation results, and recovery/interruption semantics sufficient to define observable checks. Account scale and response-size targets also remain `UNKNOWN`.
- **Affected:** SC-003, SC-004; file, database, deletion, and resource-bound coverage. No additional technology pack is selected by inference.
- **Owner:** UNKNOWN.

**OD-008 — Applicable obligations**
- **Unresolved:** Legal obligations are `UNKNOWN`. Evidence needed: requirements-level identification of applicable obligations and their data scope, or a documented determination that no additional obligations apply. Release-only sharing and explicit recovery-copy deletion already remain product requirements.
- **Affected:** SC-008; obligation-specific retention, deletion, and assurance coverage.
- **Owner:** UNKNOWN.

**OD-009 — Fastify source-record inconsistency**
- **Unresolved:** `content/js/fastify/5.12/sources.md` both asserts and records removal of a 5.12.5 floor. Resolution is **TO BE DECIDED**. Evidence needed: reconciled corpus provenance and verified supporting documentation for any eventual patch-dependent rule, after project version confirmation.
- **Affected:** SC-001, SC-005; Fastify patch-specific coverage. This does not establish any project version.
- **Owner:** UNKNOWN.
