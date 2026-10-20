# Secure Coding

## Scope and authority

REQUIREMENTS.md owns behavior and privacy scope; DESIGN.md owns native interaction; ARCHITECTURE.md owns implementation decisions. This document supplies project security controls for the native Qt desktop application and HTTPS recommendation API. The project maintainer owns review and release evidence. Rules below are adopted requirements, not claims of passing implementation tests.

Local services enforce approval, recovery, and filesystem access. The API independently enforces authentication, ownership, roles, and release-only sharing. Admin status never grants access to desktop files. Bandcamp links open in the system browser; no browser renderer or mobile application is included.

## Security guidance selection

Use the project controls below with the adopted Node.js 24 / Fastify 5 / JavaScript ES2022 and Qt 6.8 / C++17 baselines. No version-specific pack from the previously reviewed external `aegis/secure-coding-knowledge` corpus is selected. The candidate composition required different language/framework versions; selecting it would misrepresent applicability. These project controls stand independently of that corpus and do not claim its provenance.

| Former decision | Adopted resolution |
| --- | --- |
| OD-001: server roles and versions | Node.js 24 LTS runtime, Fastify 5 API framework; reject the candidate Node.js 26 composition. |
| OD-002: native baseline | Qt 6.8 Widgets, C++17, explicit modules and platform toolchains in ARCHITECTURE.md; reject the Qt 6.11 / C++23 pack. |
| OD-003: server language | JavaScript ES2022 modules; no TypeScript. ES2026 and TypeScript 7 packs do not apply. |
| OD-004: policy engine | No OPA or Rego; authorization is enforced and tested in the service domain. |
| OD-005: deployment | Ubuntu host, systemd, dedicated service user, no containers; Dockerfile pack does not apply. |
| OD-006: credentials and transport | Adopt SC-005 below, including native credential storage and revocable sessions. |
| OD-007: media and persistence | TagLib 2.x and separate SQLite 3.x stores; patch pins, preservation tests, and workload gates are mandatory before release. |
| OD-008: obligations | Adopt the privacy controls and release-eligibility review in REQUIREMENTS.md and SC-008. Do not infer legal exemption or certification. |
| OD-009: contradictory Fastify source record | Reject the candidate 5.12 pack and its inconsistent 5.12.5 floor as project authority. Use the chosen Fastify 5 patch’s upstream advisories and release evidence; the external corpus is not modified by this decision. |

## Secure-coding rules

### SC-001 — Service boundary controls

- The API MUST validate bounded JSON request schemas, reject extra properties, and validate MusicBrainz release identifiers as UUIDs before domain processing. Schemas are application-owned, never client-supplied executable definitions.
- Every protected operation MUST authenticate and recheck account status. Derive ownership from the session; deny cross-account access and require the Admin role for suspension/restoration. Parameterize SQL and authorize before mutation.
- Enforce the payload, account, membership, pagination, and deadline limits in ARCHITECTURE.md. Return 400 for invalid payloads, 401 for absent/invalid sessions, 403 for forbidden operations, 413 for oversized bodies, and 429 with Retry-After for rate/capacity limits. Reject atomically without partial updates.
- Permit at most 60 authenticated requests per minute per account and 10 sign-in attempts per minute per source IP and normalized username, tracked independently. Return generic authentication failures. Bound queued work and return 503 when saturated.
- Verification: test missing, forged, expired, suspended, non-owner, and non-Admin sessions; malformed/oversized requests; injection strings; capacity boundaries; and response schemas that exclude other users’ identities and complete libraries. Trace: FR-4.3, FR-4.10–FR-4.15, DR-4–DR-5.

### SC-002 — Native input and rendering

- Treat imported files, metadata, cover images, and network responses as untrusted. Render metadata as plain text; do not interpret HTML, scripts, shell fragments, or format strings.
- Validate numbers, dates, image type, decoded dimensions, and allocation sizes before use. Limit cover inputs to 20 MiB encoded and 40 million decoded pixels; reject oversized covers with a per-file error. Use checked arithmetic and RAII; fuzz media adapters and run address/undefined-behavior sanitizers in supported test builds.
- Import only selected regular files or regular files beneath selected directories; do not recursively follow symlinks, junctions, or reparse points. Report skipped links. Check identity again before write and fail on path substitution or source changes.
- Generate only HTTPS Bandcamp search URLs with encoded artist/title parameters and an allowlisted host. Hand them to the OS URL opener without a shell. Do not execute URLs or commands supplied by metadata.
- Verification: malformed media, decompression/allocation limits, link traversal, swapped files, hostile text/URLs, keyboard access, and 200% text scaling on each acceptance platform. Trace: FR-1.20–FR-1.22, FR-3.5–FR-3.6, DESIGN.md.

### SC-003 — Approved writes and recovery integrity

- The local domain MUST bind approval to the reviewed file identity, original content fingerprint, and exact field changes. Serialize writes per file and require renewed review after a source change.
- Create and flush a complete recovery copy with owner-only permissions before modifying the original. Stage on the same filesystem as the original, verify audio and unapproved metadata preservation, and use the platform’s atomic replacement operation. Fail safely when replacement cannot preserve required permissions or integrity.
- Persist operation state before replacement and reconcile interrupted operations from actual file contents on restart. Never report success before file and catalog reconciliation. Failed changes remain available for retry.
- Restore only a confirmed, application-recorded recovery copy to its associated path; reject path substitution. Retain copies until explicit deletion. Recovery-copy failure cancels the write.
- Verification: each supported format and stored field, disk-full/read-only conditions, crash injection before/after replacement, concurrent edits, retained copies, and restoration. Release requires unchanged audio and unapproved-field evidence for every supported format. Trace: FR-1.5, FR-1.23–FR-1.34, DR-3.

### SC-004 — Sharing and deletion

- Sharing MUST start disabled. Construct an immutable previewed identifier set and submit only after explicit confirmation. No import, save, refresh, retry loop, or background task may silently submit a changed library.
- Library replacement, withdrawal, and account deletion MUST be transactional. Report success only after commit. Deletion also revokes sessions; suspension revokes sessions and immediately excludes the account from recommendations.
- Do not persist recommendation snapshots. Bind pagination to requester and membership revision, invalidate changed revisions, and recheck eligibility on each page. Never return withdrawn/suspended memberships through stale cursors.
- Verification: exact preview/submission equality, extra-field rejection, transaction rollback, concurrent withdrawal/suspension during pagination, and immediate session revocation. Trace: FR-4.4–FR-4.9, FR-4.13–FR-4.14, DR-6.

### SC-005 — Credentials, sessions, and transport

- Hash passwords with Argon2id using at least 19 MiB memory, two iterations, parallelism one, and a unique random salt. Accept 15–128 Unicode characters without silent truncation; never store or log plaintext passwords. These hashing minima follow the [OWASP password-storage guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
- Generate opaque session secrets from 32 cryptographically random bytes and store only their SHA-256 digests server-side. Send bearer tokens only in Authorization headers, never URLs. Expire sessions after 30 minutes idle or 24 hours absolute, whichever occurs first; sign-out, suspension, and deletion revoke them immediately. These lifetimes are project decisions informed by [OWASP session guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
- Store client tokens in Windows Credential Manager, macOS Keychain, or Linux Secret Service. If secure storage is unavailable, keep the token in memory only and require sign-in after restart. Never persist passwords. Provision the initial Admin through a local operator command; public registration cannot set roles.
- Require TLS 1.2 or newer with certificate/hostname verification for service and metadata calls. Never disable verification or downgrade to plaintext. The operator owns API certificate renewal; failed verification ends the request. Do not forward credentials across redirects or origins.
- Verification: stored hash inspection, invalid certificates, expired/revoked sessions, credential-store failure, restart behavior, role escalation, and secret-free logs. Trace: FR-4.2–FR-4.3 and ARCHITECTURE.md authentication decisions.

### SC-006 — Domain authorization

OPA is not applicable. Implement deny-by-default owner/Admin checks in the service domain, including direct invocation paths outside HTTP handlers. Test every role/operation pair and ensure a hidden desktop control is never treated as an authorization decision. Trace: FR-4.11–FR-4.15, DR-5.

### SC-007 — Build and host controls

Container-specific controls are not applicable. Run the API as a dedicated non-root systemd user with write access only to its service database/state directory. Restrict inbound traffic to the HTTPS API. Pin dependencies and toolchains, verify artifact integrity, scan dependencies against upstream advisories, and record an SBOM. Block release for unmitigated applicable high/critical vulnerabilities. Test clean installation, upgrades, and rollback on each acceptance platform; verify package signatures/checksums and service filesystem restrictions. Trace: ARCHITECTURE.md build and deployment decisions.

### SC-008 — Privacy and operational evidence

- Treat account identifiers, release memberships, and security logs as personal data. Never upload audio, local paths, images, or unapproved metadata. Local catalog and recovery files use owner-only permissions.
- Log operation type, result, time, and correlation ID; exclude passwords, bearer tokens, payload bodies, local paths, and complete libraries. Retain service security logs for 30 days and restrict access to operators. Alert on repeated authentication throttling (20 events in 5 minutes), failed deletion transactions, or certificate renewal failures through operator monitoring.
- The closed pilot uses no persistent service database backups or recommendation caches, so committed account/library deletion leaves no application-managed backup copy. Enable SQLite secure deletion and checkpoint/truncate WAL after deletion before reporting success; on checkpoint failure report pending deletion and retry cleanup. This is logical application deletion, not a promise of forensic erasure on storage hardware. Do not enable provider snapshots without an adopted deletion/retention design. Local music recovery copies remain until explicit user deletion.
- Before public launch, the maintainer MUST record deployment jurisdiction, processing basis, user notice, retention/deletion handling, and dependency-license obligations in the release evidence. This gate does not assert a legal determination or waive obligations during the pilot.
- Verification: payload/log inspection, timed retention cleanup, account/library deletion including WAL cleanup, local recovery retention, and a completed release review. Trace: REQUIREMENTS.md privacy scope, FR-1.31, FR-4.7–FR-4.9, FR-4.14.
