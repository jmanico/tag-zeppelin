# Security posture and controls

[REQUIREMENTS.md](REQUIREMENTS.md) owns externally observable behavior; [DESIGN.md](DESIGN.md) owns interaction and rendering presentation; [ARCHITECTURE.md](ARCHITECTURE.md) owns components and technology. All security controls are authored here. The project maintainer owns security review and release evidence; controls are adopted, not claims of passing tests.

## Guidance and resolved decisions

No version-specific pack from the previously reviewed external `aegis/secure-coding-knowledge` corpus is selected: its candidate language/framework composition differs from the adopted architecture. These project controls stand independently and do not claim that corpus's provenance. Technology decisions OD-001–OD-005 and OD-007 are defined in [ARCHITECTURE.md](ARCHITECTURE.md).

| ID | Adopted resolution |
| --- | --- |
| OD-006 | Credential and transport controls are defined in SC-005. |
| OD-008 | Privacy controls and release-eligibility review are defined in SC-008; no legal exemption or certification is inferred. |
| OD-009 | Reject the candidate Fastify 5.12 pack and its inconsistent 5.12.5 floor as project authority. Use upstream advisories and release evidence for the adopted patch; this decision does not modify the external corpus. |

## Secure-coding rules

### SC-001 — Service boundary controls

- The API MUST validate bounded JSON request schemas, reject extra properties, and validate MusicBrainz release identifiers as UUIDs before domain processing. Schemas are application-owned, never client-supplied executable definitions.
- Every protected operation MUST authenticate and recheck account status. Derive ownership from the session; deny cross-account access and require the Admin role for suspension/restoration. Parameterize SQL and authorize before mutation.
- Enforce a pilot capacity of 100 accounts and 10,000 distinct release identifiers per account; library bodies are limited to 512 KiB and other request bodies to 16 KiB. Limit recommendation pages to 200 results and 64 KiB. Enforce a 15-second API request deadline and a 10-second outbound lookup deadline. Failure responses follow FR-4.23–FR-4.25 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Permit at most 60 authenticated requests per minute per account and 10 sign-in attempts per minute per source IP and normalized username, tracked independently. Bound queued work; observable rejection behavior is defined in FR-4.18 and FR-4.24 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Verification: test missing, forged, expired, suspended, non-owner, and non-Admin sessions; malformed/oversized requests; injection strings; capacity boundaries; and response schemas that exclude other users’ identities and complete libraries. Trace: FR-4.3, FR-4.10–FR-4.15, DR-4–DR-5.

### SC-002 — Native input and rendering

- Treat imported files, metadata, cover images, and network responses as untrusted. Prevent interpretation of metadata as HTML, scripts, shell fragments, or format strings; presentation follows the rendering convention in [DESIGN.md](DESIGN.md).
- Validate numbers, dates, image type, decoded dimensions, and allocation sizes in the local domain before use; field validity is defined in FR-1.20–FR-1.22 in [REQUIREMENTS.md](REQUIREMENTS.md). Limit cover inputs to 20 MiB encoded and 40 million decoded pixels; observable rejection is defined in FR-1.39 in [REQUIREMENTS.md](REQUIREMENTS.md). Use checked arithmetic and RAII; fuzz media adapters and run address/undefined-behavior sanitizers in supported test builds.
- Import only selected regular files or regular files beneath selected directories; do not recursively follow symlinks, junctions, or reparse points. Check identity again before write; observable link and source-change behavior is defined in FR-1.37–FR-1.40 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Generate only HTTPS Bandcamp search URLs with encoded artist/title parameters and an allowlisted host. Hand them to the OS URL opener without a shell. Do not execute URLs or commands supplied by metadata.
- Apply the existing cover byte/pixel limits to embedded artwork as well as separately selected images, before unbounded decoding or allocation. Verify remote response structure before domain use. Additional resource budgets depend on SC-011. Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).
- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, and the keyboard/scaling acceptance targets in [DESIGN.md](DESIGN.md) on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.

### SC-003 — Approved writes and recovery integrity

- The local domain MUST bind approval to the reviewed file identity, original content fingerprint, and exact field changes. Serialize writes per file and enforce the sequence referenced by DR-3 in [ARCHITECTURE.md](ARCHITECTURE.md) in local services: validation, approval binding, recovery creation, then write. No view or adapter may bypass it; source-change behavior is defined in FR-1.37 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Create and flush a complete recovery copy with owner-only permissions before modifying the original. Stage on the same filesystem as the original, verify audio and unapproved metadata preservation, and use the platform’s atomic replacement operation. Fail safely when replacement cannot preserve required permissions or integrity.
- Persist operation state before replacement and reconcile interrupted operations from actual file contents on restart. Result and retry behavior is defined in FR-1.34, FR-1.36, and FR-1.41 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Restore only an application-recorded recovery copy to its associated path; reject path substitution. Confirmation, retention, and recovery-copy failure behavior is defined in FR-1.30–FR-1.32 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Record recovery-content integrity when creating the complete recovery copy and verify it again before restoration. Bind restoration to the selected recorded copy and recheck the destination under the existing identity/substitution rules immediately before mutation. Recovery creation before restoration is governed by SC-013 and FR-1.46. Rejection behavior is FR-1.44 in [REQUIREMENTS.md](REQUIREMENTS.md). Threat: [T-020](THREAT_MODEL.md#t-020).
- Verification: each supported format and stored field, disk-full/read-only conditions, crash injection before/after replacement, concurrent edits, retained copies, and restoration. Release requires unchanged audio and unapproved-field evidence for every supported format. Trace: FR-1.5, FR-1.23–FR-1.34, DR-3.

### SC-004 — Sharing and deletion

- Construct an immutable previewed identifier set bound to the confirmation required by FR-4.4–FR-4.6 in [REQUIREMENTS.md](REQUIREMENTS.md). Allow only release identifiers in the shared-library payload, separate from authentication/protocol context; reject extra fields. No import, save, refresh, retry loop, or background task may silently submit a changed library.
- Library replacement, withdrawal, and account deletion MUST be transactional. Completion behavior is defined in FR-4.22 and FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md). Session revocation is defined in SC-005; recommendation eligibility is defined in FR-4.13 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Do not cache recommendations or persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.
- Treat pagination cursors as untrusted input; validate their binding to the authenticated requester and membership revision on every page. The desktop must discard an invalidated accumulation under FR-3.19 in [REQUIREMENTS.md](REQUIREMENTS.md). Verify requester substitution and revision changes without treating a cursor as authorization. Threats: [T-006](THREAT_MODEL.md#t-006), [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023).
- Verification: exact preview/submission equality, extra-field rejection, transaction rollback, concurrent withdrawal/suspension during pagination, and immediate session revocation. Trace: FR-4.4–FR-4.9, FR-4.13–FR-4.14, DR-6.

### SC-005 — Credentials, sessions, and transport

- Hash passwords with Argon2id using at least 19 MiB memory, two iterations, parallelism one, and a unique random salt. Password acceptance is defined in FR-4.17 in [REQUIREMENTS.md](REQUIREMENTS.md); never store or log plaintext passwords. These hashing minima follow the [OWASP password-storage guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
- Generate opaque session secrets from 32 cryptographically random bytes and store only their SHA-256 digests server-side. Send bearer tokens only in Authorization headers, never URLs. Expire sessions after 30 minutes idle or 24 hours absolute, whichever occurs first; sign-out, suspension, and deletion revoke them immediately. These lifetimes are project decisions informed by [OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
- Store client tokens in Windows Credential Manager, macOS Keychain, or Linux Secret Service. If secure storage is unavailable, keep the token in memory only (restart behavior is defined in FR-4.20 in [REQUIREMENTS.md](REQUIREMENTS.md)). Never persist passwords. Provision the initial Admin through a local operator command; role-setting rejection is defined in FR-4.21 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Require TLS 1.2 or newer with certificate/hostname verification for service and metadata calls. Never disable verification or downgrade to plaintext. The operator owns API certificate renewal; failed verification ends the request. Do not forward credentials across redirects or origins.
- Verification: stored hash inspection, invalid certificates, expired/revoked sessions, credential-store failure, restart behavior, role escalation, and secret-free logs. Trace: FR-4.2–FR-4.3, FR-4.16–FR-4.21, OD-006.

### SC-006 — Domain authorization

Technology selection is recorded in OD-004 in [ARCHITECTURE.md](ARCHITECTURE.md). Implement deny-by-default owner/Admin checks in the service domain, including direct invocation paths outside HTTP handlers. Test every role/operation pair and ensure a hidden desktop control is never treated as an authorization decision. Trace: FR-4.11–FR-4.15, DR-5.

### SC-007 — Build and host controls

Deployment selection is recorded in OD-005 in [ARCHITECTURE.md](ARCHITECTURE.md). Run the API as a dedicated non-root systemd user with write access only to its service database/state directory. Restrict inbound traffic to the HTTPS API. Pin exact compiler, SDK, Qt, TagLib, SQLite, Node.js, and Fastify patches in reproducible lockfiles/build manifests; version-line choices do not permit floating dependencies. Require the same acceptance checks for dependency updates. Sign Windows and macOS artifacts and publish authenticated Linux package checksums. Verify artifact integrity, scan dependencies against upstream advisories, and record an SBOM. The operator provisions the TLS certificate. Block release for unmitigated applicable high/critical vulnerabilities. Test clean installation, upgrades, and rollback on each acceptance platform; verify package signatures/checksums and service filesystem restrictions. Trace: OD-001–OD-003, OD-005, OD-007 in [ARCHITECTURE.md](ARCHITECTURE.md).

### SC-008 — Privacy and operational evidence

- Treat account identifiers, release memberships, and security logs as personal data. Shared-library content restrictions are defined in FR-4.7 in [REQUIREMENTS.md](REQUIREMENTS.md). Local catalog and recovery files use owner-only permissions.
- Log operation type, result, time, and correlation ID; exclude passwords, bearer tokens, invitation secrets, payload bodies, local paths, and complete libraries. Retain service security logs for 30 days and restrict access to operators. Alert on repeated authentication throttling (20 events in 5 minutes), failed deletion transactions, or certificate renewal failures through operator monitoring. Invitation-secret exclusion traces to [T-009](THREAT_MODEL.md#t-009).
- The closed pilot uses no persistent service database backups (recommendation snapshot restrictions are defined in SC-004), so committed account/library deletion leaves no application-managed backup copy. Enable SQLite secure deletion and checkpoint/truncate WAL after deletion before reporting success; on checkpoint failure retry cleanup; user-visible status is defined in FR-4.22 in [REQUIREMENTS.md](REQUIREMENTS.md). This is logical application deletion, not a promise of forensic erasure on storage hardware. Do not enable provider snapshots without an adopted deletion/retention design. Local recovery retention is defined in FR-1.31 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Before public launch, the maintainer MUST record deployment jurisdiction, processing basis, user notice, retention/deletion handling, and dependency-license obligations in the release evidence. This gate does not assert a legal determination or waive obligations during the pilot.
- Verification: payload/log inspection, timed retention cleanup, account/library deletion including WAL cleanup, local recovery retention, and a completed release review. Trace: [REQUIREMENTS.md](REQUIREMENTS.md) release scope, FR-1.31, FR-4.7–FR-4.9, FR-4.14.

## Threat-model decision resolutions

OD-010–OD-019 are adopted resolutions under the user's authorization to resolve remaining decisions using best judgment. `ACTIVE` means a complete adopted rule, not implemented or verified protection. Required implementation, workload, privacy-review and release evidence remains outstanding. Product behavior is owned by REQUIREMENTS.md; the table references its resolved values rather than redefining them.

| ID | Adopted resolution | Rule / threats |
| --- | --- | --- |
| OD-010 | Apply the qualifying-cohort, contributor, ranking and disclosure requirements in FR-3.20–FR-3.23, with bounded query/replacement access and adversarial privacy verification in SC-009. | SC-009; T-004, T-008, T-010 |
| OD-011 | Require the single-use operator invitation in FR-4.29; generate and consume it under SC-010. | SC-010; T-009, T-017 |
| OD-012 | Enforce the registration admission budgets in SC-010 before expensive account creation. | SC-010; T-005, T-009, T-017 |
| OD-013 | Enforce the API and password-hashing concurrency/queue budgets in SC-011 within the existing request deadline. | SC-011; T-005, T-017, T-025 |
| OD-014 | Enforce the response, metadata and parser budgets in SC-011; failure behavior is FR-1.45 and FR-3.24. | SC-011; T-003, T-005, T-021 |
| OD-015 | Apply FR-4.30 account-name acceptance and canonical equivalence consistently through SC-012. | SC-012; T-001, T-009 |
| OD-016 | Require a verified recovery copy before restoration under FR-1.46 and SC-013. | SC-013; T-020 |
| OD-017 | Use FR-4.31's empty-service reprovisioning outcome after store loss; retain the no-backup policy and verify recovery under SC-014. | SC-014; T-025 |
| OD-018 | Use the prospective pilot location in ARCHITECTURE.md and participant scope in FR-4.34; substantiate actual deployment and eligibility before pilot collection under SC-015. | SC-015; T-010, T-011, T-012 |
| OD-019 | Adopt the operation-specific processing plan and pre-pilot notice/review gate in SC-015. Its legal and operational evidence must substantiate the plan before collection; no legal conclusion is asserted. | SC-015; T-010, T-011, T-012 |

### SC-009 — Recommendation inference protection — ACTIVE

- Enforce FR-3.20–FR-3.23 in the service domain before pagination. Compute exact ranking only over qualifying releases; prevent identity, candidate-support count and cohort-size disclosure in response bodies, cursor contents and errors. Present only the required generic aggregate reason. Existing SC-001/SC-004/SC-008 and FR-4.10 remain mandatory.
- Limit each account to two admitted library replacements in any rolling 24 hours and five admitted recommendation queries in any rolling hour. Count admission atomically before calculation or mutation; rejected validation/authentication attempts remain subject to SC-001. Each cursor chain belongs to one admitted query; its page requests do not consume further query admissions, but all page requests remain subject to SC-001's authenticated-request limit. A fresh query after revision invalidation consumes a new admission. Preserve withdrawal and account deletion access; they are not library replacements. Rate-limit failure and explicit-retry behavior follow FR-4.24–FR-4.25 and FR-4.32 in REQUIREMENTS.md.
- Do not claim that cohort thresholds, omitted counts or invitations provide anonymity or eliminate inference. Prior knowledge, collusion and comparisons over time remain residual threats. Release requires adversarial tests for fewer-than-required cohorts/contributors, contributor removal at thresholds, repeated replacements, colluding invited accounts, cross-page revision changes, and differential outputs. Verify that the specified minimums, output restrictions and limits hold and that tested recommendation functions do not disclose identities or complete libraries contrary to FR-4.10. A demonstrated violation blocks service release; record test limitations and remaining inference risk in release evidence.
- Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).

### SC-010 — Pilot enrollment and registration admission — ACTIVE

- Implement FR-4.29 through the local operator provisioning path described in ARCHITECTURE.md. Generate invitation secrets from 32 cryptographically random bytes, store only their SHA-256 digests, and expire unused invitations seven days after generation. Do not log secrets or place them in URLs. No service Admin invitation API is introduced.
- Validate invitation validity and registration admission before password hashing. Limit registration attempts to three per rolling hour per source IP and 30 per rolling hour service-wide, counting failed invitations as attempts. Enforce both counters atomically. Return generic invalid-invitation rejection without indicating whether a secret was used, expired or unknown; use existing FR-4.24 responses for rate/capacity rejection.
- Recheck invitation validity, account capacity and canonical name uniqueness when committing account creation; consume the invitation in the same transaction. Failed creation must not leave a partial account or consume the invitation. Preserve the 100-account cap and existing sign-in/authenticated limits.
- Rate counters used by SC-001, SC-009 and SC-010 MUST remain effective across service restarts, retain only the minimum enforcement identity/key, count and window state, and expire when their limiting windows end. Account-deletion cleanup under SC-008 remains required. Verify restart behavior and expiry as well as atomic admission.
- Verify invalid, expired and replayed invitations, concurrent redemption, capacity and counter boundaries, transaction rollback, and rejection before hashing. Threats: [T-005](THREAT_MODEL.md#t-005), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).

### SC-011 — Complete resource budgets — ACTIVE

- Admit at most ten active API requests and 20 queued requests service-wide. The existing 15-second request deadline starts at admission and includes queue time. Saturation follows FR-4.24. Bound password hashing to two concurrent operations and eight waiting operations; hashing requests remain inside the API active/queued bounds and deadline, not an additional unbounded work pool. Expired/cancelled requests must not retain queued work; mutation completion must still satisfy the transactional requirements.
- Limit each outbound lookup response to 8 MiB and 1,000 records before domain processing, enforcing the byte bound while receiving and decoding. Existing smaller recommendation-page bounds and the ten-second outbound deadline remain in force. Limit non-cover metadata to 64 KiB of UTF-8 per field and 1 MiB total per file. Bound transient parser allocations to 256 MiB and parser processing to ten seconds per file. Existing cover encoded-byte/decoded-pixel limits remain unchanged and must be enforced before allocation.
- Fail closed without truncating accepted values or partially applying rejected operations. Per-file and lookup limit behavior is owned by FR-1.45 and FR-3.24. Preserve unapproved fields and audio under SC-003. Existing SC-001/SC-002 controls and NFR-3.1 cannot be relaxed to satisfy these budgets.
- Verify each boundary, oversized/decompressed responses, aggregate metadata, parser time/allocation exhaustion, queue cancellation and hash saturation. Measure the prescribed bounded workload on the prescribed host; chosen budgets are adopted design limits, not evidence of capacity. A failed workload or inability to enforce parser limits blocks the corresponding release acceptance.
- Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-017](THREAT_MODEL.md#t-017), [T-021](THREAT_MODEL.md#t-021), [T-025](THREAT_MODEL.md#t-025).

### SC-012 — Consistent account-name identity — ACTIVE

Apply FR-4.30's accepted spelling and lowercase canonical identity consistently to registration uniqueness, sign-in lookup and the normalized-username throttle required by SC-001. Enforce canonical uniqueness transactionally. Reject invalid spellings rather than silently removing characters. Verify case variants cannot obtain separate throttle identities or ambiguous account ownership, including concurrent registration. This policy does not normalize, truncate or restrict passwords beyond FR-4.17. Threats: [T-001](THREAT_MODEL.md#t-001), [T-009](THREAT_MODEL.md#t-009).

### SC-013 — Recovery-before-restore policy — ACTIVE

Implement FR-1.46 through the existing SC-003 sequence: verify the selected recovery copy and current destination identity, create and flush a complete integrity-recorded recovery copy of the destination, then perform verified replacement and catalog reconciliation. Failure before replacement leaves the destination unchanged; retain the selected and newly created recovery copies until explicit deletion under FR-1.31. Preserve renewed review, source-change rejection, owner-only permissions, atomic replacement, operation-state persistence and FR-1.44 integrity failure behavior. Verify disk-full/copy failures, changed sources, corrupted copies and interruption before/after replacement; do not report restoration complete until reconciliation. Threat: [T-020](THREAT_MODEL.md#t-020).

### SC-014 — Service recovery objectives — ACTIVE

Implement FR-4.31's best-effort empty-service reprovisioning after loss of the single service store. Do not introduce snapshots or persistent database backups prohibited by SC-008. Reprovision host restrictions, TLS, initial Admin and invitation generation before renewed enrollment; lost sessions are invalid and previous memberships cannot be reconstructed from logs. Record a store-loss recovery exercise and clean migration/rollback evidence before pilot release. Recovery must not revive deleted memberships or silently resubmit desktop libraries. No data-recovery guarantee or recovery-time deadline is promised. Threat: [T-025](THREAT_MODEL.md#t-025).

### SC-015 — Privacy release-context evidence — ACTIVE

- Verify the prospective pilot hosting location defined in ARCHITECTURE.md and the participant eligibility defined in FR-4.34 before pilot collection. Record the actual deployment and eligibility evidence; the adopted scope is not proof that a host or participants already exist. The operator's invitation workflow must confirm eligibility without collecting identity-document copies or adding service profile fields.
- Adopt a processing plan of consent for voluntary library sharing, contractual necessity for account/service operation, and legitimate interests for the limited security logging in SC-008. These are intended bases for review, not established legal conclusions. Before any pilot personal-data collection, the maintainer must record the applicable review and evidence substantiating each operation's basis, scope, necessity, and applicable safeguards; record the logging interest/balancing assessment and consent/withdrawal design. If the review does not substantiate the plan, collection and pilot release must not begin; a reviewed specification amendment is required before using another plan.
- Before enrollment, publish a notice with the actual operator identity/contact, processing purposes and data categories, intended bases, recipients/external services, account/library deletion, 30-day security-log retention, no persistent service backups, recommendation inference risks, applicable rights/contact route and withdrawal process. Explain that sharing withdrawal ends sharing, account deletion ends account operation, and the disclosed security-log retention is governed separately under the reviewed logging basis. Show external lookup disclosure under FR-3.18. The actual notice and review records are release evidence, not invented contents in this specification.
- Verify notice delivery and the specified consent, withdrawal, deletion and retention behavior before pilot release. Preserve SC-008's broader public-launch review, including dependency-license obligations. Required evidence is outstanding; no compliance, anonymity or implemented-control claim follows from this ACTIVE rule. Threats: [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012).
