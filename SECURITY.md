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
- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, and the keyboard/scaling acceptance targets in [DESIGN.md](DESIGN.md) on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.

### SC-003 — Approved writes and recovery integrity

- The local domain MUST bind approval to the reviewed file identity, original content fingerprint, and exact field changes. Serialize writes per file and enforce the sequence referenced by DR-3 in [ARCHITECTURE.md](ARCHITECTURE.md) in local services: validation, approval binding, recovery creation, then write. No view or adapter may bypass it; source-change behavior is defined in FR-1.37 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Create and flush a complete recovery copy with owner-only permissions before modifying the original. Stage on the same filesystem as the original, verify audio and unapproved metadata preservation, and use the platform’s atomic replacement operation. Fail safely when replacement cannot preserve required permissions or integrity.
- Persist operation state before replacement and reconcile interrupted operations from actual file contents on restart. Result and retry behavior is defined in FR-1.34, FR-1.36, and FR-1.41 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Restore only an application-recorded recovery copy to its associated path; reject path substitution. Confirmation, retention, and recovery-copy failure behavior is defined in FR-1.30–FR-1.32 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Verification: each supported format and stored field, disk-full/read-only conditions, crash injection before/after replacement, concurrent edits, retained copies, and restoration. Release requires unchanged audio and unapproved-field evidence for every supported format. Trace: FR-1.5, FR-1.23–FR-1.34, DR-3.

### SC-004 — Sharing and deletion

- Construct an immutable previewed identifier set bound to the confirmation required by FR-4.4–FR-4.6 in [REQUIREMENTS.md](REQUIREMENTS.md). Allow only release identifiers in the shared-library payload, separate from authentication/protocol context; reject extra fields. No import, save, refresh, retry loop, or background task may silently submit a changed library.
- Library replacement, withdrawal, and account deletion MUST be transactional. Completion behavior is defined in FR-4.22 and FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md). Session revocation is defined in SC-005; recommendation eligibility is defined in FR-4.13 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Do not cache recommendations or persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.
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
- Log operation type, result, time, and correlation ID; exclude passwords, bearer tokens, payload bodies, local paths, and complete libraries. Retain service security logs for 30 days and restrict access to operators. Alert on repeated authentication throttling (20 events in 5 minutes), failed deletion transactions, or certificate renewal failures through operator monitoring.
- The closed pilot uses no persistent service database backups (recommendation snapshot restrictions are defined in SC-004), so committed account/library deletion leaves no application-managed backup copy. Enable SQLite secure deletion and checkpoint/truncate WAL after deletion before reporting success; on checkpoint failure retry cleanup; user-visible status is defined in FR-4.22 in [REQUIREMENTS.md](REQUIREMENTS.md). This is logical application deletion, not a promise of forensic erasure on storage hardware. Do not enable provider snapshots without an adopted deletion/retention design. Local recovery retention is defined in FR-1.31 in [REQUIREMENTS.md](REQUIREMENTS.md).
- Before public launch, the maintainer MUST record deployment jurisdiction, processing basis, user notice, retention/deletion handling, and dependency-license obligations in the release evidence. This gate does not assert a legal determination or waive obligations during the pilot.
- Verification: payload/log inspection, timed retention cleanup, account/library deletion including WAL cleanup, local recovery retention, and a completed release review. Trace: [REQUIREMENTS.md](REQUIREMENTS.md) release scope, FR-1.31, FR-4.7–FR-4.9, FR-4.14.
