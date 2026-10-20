# Music Tagging Application Requirements

Tag a local music collection, review metadata changes, and discover music to buy. Actors are the current user, recommendation-service Admins, and participating users. The release covers local desktop distribution and an operator-run closed recommendation-service pilot.

[DESIGN.md](DESIGN.md) owns presentation and accessibility targets; [ARCHITECTURE.md](ARCHITECTURE.md) owns implementation; [SECURITY.md](SECURITY.md) owns controls and privacy/release eligibility.

## Functional Requirements

### Music Files and Metadata

Supported formats are FLAC, MP3, AAC audio in M4A files, Ogg Vorbis, Ogg Opus, and AIFF. Other formats are outside the first release. File renaming, moving, transcoding, and automatic cover art retrieval are outside the first release.

Editable fields are title, artist, album, album artist, track number, track total, disc number, disc total, release date, genre, and front cover art. MusicBrainz recording and release identifiers are also stored fields. A date has the form YYYY, YYYY-MM, or YYYY-MM-DD.

- **FR-1.1** The system MUST read metadata from FLAC files selected by the current user.
- **FR-1.2** The system MUST read metadata from MP3 files selected by the current user.
- **FR-1.3** The system MUST use MusicBrainz as the source of proposed text metadata and MusicBrainz identifiers.
- **FR-1.4** The system MUST show the current and proposed values for each metadata change before approval, including image previews for cover art.
- **FR-1.5** The system MUST obtain approval from the current user for each metadata change before it writes that change to a music file.
- **FR-1.6** The system MUST let the current user manually edit each editable field.
- **FR-1.7** The system MUST read metadata from each additional supported format selected by the current user.
- **FR-1.8** The system MUST let the current user select individual files or folders for collection import.
- **FR-1.9** The system MUST include supported files in all subfolders of a selected folder during import, subject to the traversal policy in SC-002 in [SECURITY.md](SECURITY.md).
- **FR-1.10** The system MUST show an error for each unreadable or unsupported selected file.
- **FR-1.11** The system MUST continue import for other selected files after a file error.
- **FR-1.12** The system MUST keep only one collection entry for each absolute file path.
- **FR-1.13** The system MUST show MusicBrainz candidates for a search by artist and track title or by artist and album title.
- **FR-1.14** The system MUST require the current user to select a MusicBrainz release and recording before it proposes metadata from that match.
- **FR-1.15** The system MUST show a no-match result when a MusicBrainz search has no candidates.
- **FR-1.16** The system MUST let the current user change the search terms after a no-match result.
- **FR-1.17** The system MUST show a retry action when a MusicBrainz request fails.
- **FR-1.18** The system MUST keep existing field values when the selected MusicBrainz match has no value for those fields.
- **FR-1.19** The system MUST let the current user select a local JPEG or PNG image as front cover art.
- **FR-1.20** The system MUST reject a nonempty track number, track total, disc number, or disc total that is not a positive integer.
- **FR-1.21** The system MUST reject a nonempty release date that is not a valid date in one of the specified forms.
- **FR-1.22** The system MUST reject a cover art file that cannot be read as JPEG or PNG.
- **FR-1.23** The system MUST let the current user approve or reject each proposed field change for each file.
- **FR-1.24** The system MUST let the current user approve all displayed changes for a selected group of files in one action.
- **FR-1.25** The system MUST discard a rejected proposed change without changing the saved field value.
- **FR-1.26** The system MUST write approved stored fields into each supported music file at its existing path.
- **FR-1.27** The system MUST preserve audio content when it writes metadata.
- **FR-1.28** The system MUST preserve metadata fields outside the approved changes when it writes metadata.
- **FR-1.29** The system MUST create a complete recovery copy of a file before each metadata write.
- **FR-1.30** The system MUST cancel the write if it cannot create the recovery copy.
- **FR-1.31** The system MUST retain the recovery copy until the current user explicitly deletes it.
- **FR-1.32** The system MUST let the current user restore a file from a selected recovery copy after confirmation.
- **FR-1.33** The system MUST show a per-file failure result when a metadata write fails.
- **FR-1.34** The system MUST retain approved changes for retry after a failed write.
- **FR-1.35** The system MUST update the collection entry with the saved metadata after a successful write.
- **FR-1.36** The system MUST retain approved changes for retry across application restarts.
- **FR-1.37** The system MUST require renewed review when a source file changes after review.
- **FR-1.38** The system MUST report skipped filesystem links during import; traversal policy is defined in SC-002 in [SECURITY.md](SECURITY.md).
- **FR-1.39** The system MUST reject oversized cover inputs with a per-file error; size limits are defined in SC-002 in [SECURITY.md](SECURITY.md).
- **FR-1.40** The system MUST fail a write if the reviewed path has been substituted.
- **FR-1.41** The system MUST report save success only after the file and catalog have been reconciled.
- **FR-1.42** The system MUST refresh the collection entry after restoration.

- **FR-1.43** The system MUST keep files at distinct absolute paths as separate collection entries even when their contents match.

- **FR-1.44** The system MUST reject restoration when the selected recovery copy fails the integrity check defined in SC-003 in [SECURITY.md](SECURITY.md), leave the destination unchanged, and show a per-file failure. Threat: [T-020](THREAT_MODEL.md#t-020).

- **FR-1.45** The system MUST reject a file whose metadata processing exceeds the limits in SC-011 in [SECURITY.md](SECURITY.md), leave the source unchanged, show a per-file error, and continue processing other files without silently truncating metadata. Threats: [T-003](THREAT_MODEL.md#t-003), [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).
- **FR-1.46** Before restoration overwrites the current destination, the system MUST create and verify a complete recovery copy of that destination; failure MUST cancel restoration. All recovery copies remain subject to FR-1.31. Threat: [T-020](THREAT_MODEL.md#t-020).

### Collection Viewer and Filters

Playback and unspecified viewer functions are outside the first release.

- **FR-2.1** The system MUST show the current user's imported files with their stored fields, file paths, formats, and durations.
- **FR-2.2** The system MUST let the current user browse the collection by artist, album, or track.
- **FR-2.3** The system MUST let the current user search the collection by title, artist, or album text without regard to letter case.
- **FR-2.4** The system MUST let the current user filter files by front cover art presence, image type, or minimum image width and height in pixels.
- **FR-2.5** The system MUST let the current user filter files by artist, album, genre, release year, file format, or presence of a MusicBrainz release identifier.
- **FR-2.6** The system MUST return only files that satisfy every active filter.
- **FR-2.7** The system MUST let the current user clear all active filters in one action.
- **FR-2.8** The system MUST let the current user remove a collection entry without deleting its music file.
- **FR-2.9** The system MUST let the current user refresh an entry from its music file.

### Music Suggestions and Recommendations

Prices, checkout, payment collection, affiliate tracking, and revenue features are outside the first release.

A release is one MusicBrainz release identifier. A new release is a release absent from the current user's collection. Music tastes mean the collection's artists and genres; the first release has no separate taste profile.

- **FR-3.1** The system MUST show purchase suggestions for releases by collection artists that are absent from the collection, using MusicBrainz release identifiers for comparison.
- **FR-3.2** The system MUST show new-release recommendations from other participating users whose shared libraries have at least one release in common with the current user's shared library, subject to the privacy eligibility rules FR-3.20–FR-3.23. Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).
- **FR-3.3** The system MUST rank recommendations by the number of eligible other libraries that contain the release, with release identifier as the ascending tie breaker.
- **FR-3.4** The system MUST show the artist, release title, and suggestion reason for each purchase suggestion or recommendation.
- **FR-3.5** The system MUST show a Bandcamp search link based on artist and release title for each purchase suggestion.
- **FR-3.6** The system MUST label purchase links as searches with unverified availability.
- **FR-3.7** The system MUST show an empty result with a reason when no release satisfies the suggestion or recommendation rules.
- **FR-3.8** The system MUST exclude collection entries without MusicBrainz release identifiers from collection comparisons and shared-library recommendations.
- **FR-3.9** The system MUST show a retry action when a suggestion or recommendation request fails.
- **FR-3.10** The system MUST require explicit artist selection when MusicBrainz artist resolution for release discovery is ambiguous.
- **FR-3.11** The system MUST use the requester's last submitted library for shared-library overlap and exclude the requester's own library from eligible other libraries.
- **FR-3.12** The system MUST count a candidate release at most once per eligible other library and exclude releases in the requester's submitted library.
- **FR-3.13** The system MUST exclude releases in the current local collection from the completed recommendation ranking before displaying it, without submitting unshared local changes.
- **FR-3.14** The system MUST show an aggregate recommendation reason without identifying contributing users.
- **FR-3.15** The system MUST explain an empty recommendation result caused by no submitted overlap.
- **FR-3.16** The system MUST require a fresh recommendation query when a membership revision invalidates pagination.
- **FR-3.17** The system MUST open purchase search links in the system browser.

- **FR-3.18** Before an external lookup or purchase-search action sends data, the system MUST identify the receiving service and the search terms or release identifiers being sent, and explain that recommendation sharing being disabled does not disable these user-requested disclosures. This is informational context for the initiating workflow, not an additional confirmation gate for each lookup request. Threat: [T-011](THREAT_MODEL.md#t-011).
- **FR-3.19** The system MUST discard an incomplete recommendation result when its membership revision is invalidated and require the fresh query in FR-3.16 before displaying a completed ranking. Threats: [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023).

- **FR-3.20** The system MUST return shared-library recommendations only when at least five other eligible submitted libraries overlap the requester's submitted library. Withdrawn, suspended and requester-owned libraries MUST NOT count toward this minimum. Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).
- **FR-3.21** A recommended release MUST occur in at least three of those eligible other libraries. The system MUST apply this privacy eligibility rule before ranking qualifying releases exactly as FR-3.3 requires; FR-3.12–FR-3.13 still apply. Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).
- **FR-3.22** The API and desktop MUST NOT expose numerical contributor counts, contributing identities, or individual libraries with recommendations. The desktop MUST use a generic aggregate reason, such as Recommended from shared libraries. Internal counts remain necessary for FR-3.3. Threats: [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010).
- **FR-3.23** When privacy eligibility leaves no recommendations, the system MUST explain that there is insufficient shared information to show recommendations while protecting participants, without revealing cohort sizes or suppressed releases. Threats: [T-004](THREAT_MODEL.md#t-004), [T-010](THREAT_MODEL.md#t-010).
- **FR-3.24** The system MUST reject an external response that exceeds SC-011 limits, show request-failure feedback with an explicit retry action, and never present truncated data as a complete result. Threats: [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021).

MusicBrainz lookup sends the search terms needed for metadata and release discovery; FR-4.7 applies to recommendation-service sharing, not these lookups. There is no Bandcamp availability check or API integration in this release.

### Accounts, Sharing, and Access

- **FR-4.1** The system MUST permit local import, viewing, filtering, editing, recovery, and MusicBrainz lookup without an account.
- **FR-4.2** The system MUST let a user create an account, sign in, and sign out for the recommendation service.
- **FR-4.3** The system MUST reject shared-library submissions and recommendation requests from a user who is not signed in.
- **FR-4.4** The system MUST keep library sharing disabled until the current user explicitly enables it.
- **FR-4.5** The system MUST show the release identifiers to be shared before the current user confirms a submission.
- **FR-4.6** The system MUST replace the current user's shared library with the confirmed release identifiers only when that user submits an update.
- **FR-4.7** The system MUST exclude audio, file paths, cover art, and other metadata from shared-library submissions.
- **FR-4.8** The system MUST delete the current user's shared library before it reports successful withdrawal from sharing.
- **FR-4.9** The system MUST exclude a withdrawn library from subsequent recommendation calculations.
- **FR-4.10** The system MUST prevent users from viewing other users' identities or complete libraries through recommendation functions.
- **FR-4.11** The system MUST reject an attempt by a non-Admin user to change another user's account or shared data.
- **FR-4.12** The system MUST let an Admin suspend or restore an account's access to the recommendation service.
- **FR-4.13** The system MUST exclude suspended accounts' libraries from recommendation calculations.
- **FR-4.14** The system MUST let the current user delete their account and its shared library after confirmation.
- **FR-4.15** The system MUST deny Admin access to users' local music files through the recommendation service.
- **FR-4.16** The system MUST use username and password for account registration and sign-in.
- **FR-4.17** The system MUST accept passwords of 15–128 Unicode characters without silent truncation.
- **FR-4.18** The system MUST return generic authentication failures.
- **FR-4.19** The system MUST require a fresh sign-in after a suspended account is restored.
- **FR-4.20** The system MUST require sign-in after restart when secure client credential storage was unavailable.
- **FR-4.21** The system MUST reject public registration requests that attempt to set account roles.
- **FR-4.22** The system MUST report withdrawal or account deletion success only after committed deletion and required cleanup under SC-008 in [SECURITY.md](SECURITY.md); cleanup failure MUST report pending deletion.
- **FR-4.23** The system MUST reject invalid, forbidden, oversized, rate-limited, or over-capacity API operations without partial changes.
- **FR-4.24** The API MUST return 400 for invalid payloads, 401 for absent/invalid sessions, 403 for forbidden operations, 413 for oversized bodies, 429 with Retry-After for rate/capacity limits, and 503 for saturated work queues. Limits and validation controls are defined in SC-001 in [SECURITY.md](SECURITY.md).
- **FR-4.25** The system MUST require explicit retries for mutations.
- **FR-4.26** The system MUST deny suspended accounts access to the recommendation service.

- **FR-4.27** The system MUST report successful library replacement only after the replacement commits.

- **FR-4.28** The system MUST disclose before sharing that recommendations can reveal patterns about shared music despite privacy safeguards; it MUST NOT promise anonymity or protection from every inference. FR-4.10 remains required and service release requires SC-009 verification. Threats: [T-004](THREAT_MODEL.md#t-004), [T-010](THREAT_MODEL.md#t-010).
- **FR-4.29** Account registration MUST require a valid, unused, unexpired invitation token provisioned by the pilot operator. The service MUST consume it atomically with account creation; invalid invitations MUST receive generic rejection without creating an account. Threats: [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).
- **FR-4.30** Usernames MUST contain 3–32 ASCII letters, digits, or underscores. The service MUST use ASCII lowercase as the canonical account identity for uniqueness, sign-in and throttling. FR-4.17 password handling is unchanged. Threats: [T-001](THREAT_MODEL.md#t-001), [T-009](THREAT_MODEL.md#t-009).
- **FR-4.31** If the pilot service store is lost, the service MUST report unavailability until the operator reprovisions an empty service. Returning users MUST register with new invitations and explicitly resubmit libraries. The pilot promises neither recovery of lost service data nor a recovery deadline; local files and local workflows remain independent. Threat: [T-025](THREAT_MODEL.md#t-025).
- **FR-4.32** The system MUST report endpoint-specific admission and privacy rate limits using FR-4.24 and require an explicit user retry after rate limiting, including recommendation queries; no automatic rate-limit retry is permitted. FR-4.25 continues to govern all mutations. Numeric limits are owned by SC-009–SC-011 in [SECURITY.md](SECURITY.md). Threats: [T-005](THREAT_MODEL.md#t-005), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017).
- **FR-4.33** Before registration and before enabling sharing, the system MUST present the service notice required by SC-015 in [SECURITY.md](SECURITY.md). Sharing consent MUST remain separate, explicit and disabled by default. Threats: [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012).
- **FR-4.34** The closed pilot MUST admit only participants aged 18 or older and resident in the EEA through operator-controlled invitations. The operator MUST determine eligibility before issuing invitations; the application MUST NOT introduce additional identity-document collection. This is the adopted pilot scope, not a statement that any participant has been verified. Threats: [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010).

## Non-Functional Requirements

### Supported Platforms

The first-release acceptance platforms are Windows 11 24H2 on x64, macOS 15 on Apple silicon, and Ubuntu 24.04 LTS on x64. This is a fixed test scope, not a claim about the latest platform versions.

- **NFR-1.1** The system MUST provide all applicable desktop functions on the specified Windows acceptance platform.
- **NFR-1.2** The system MUST provide all applicable desktop functions on the specified macOS acceptance platform.
- **NFR-1.3** The system MUST provide all applicable desktop functions on the specified Linux acceptance platform.
- **NFR-1.4** The system MUST limit supported user interface platforms to native Windows, macOS, and Linux desktop applications.
- **NFR-1.5** The system MUST NOT provide a web frontend, embedded browser application UI, or mobile application.

### Offline Operation

- **NFR-2.1** The system MUST permit local import, viewing, filtering, manual editing, and recovery without a network connection.
- **NFR-2.2** The system MUST keep local workflows usable when network functions fail.

### Performance

- **NFR-3.1** The recommendation API MUST achieve p95 latency below 2 seconds at 10 concurrent requests on a 2-vCPU, 4-GiB RAM host at the pilot capacity defined in SC-001 in [SECURITY.md](SECURITY.md), excluding external MusicBrainz latency. Acceptance MUST NOT change ranking or omit results to meet this target.

## Threat-driven acceptance criteria

These are required future checks, not completed tests.

| Requirement | Acceptance evidence | Threat |
| --- | --- | --- |
| FR-1.44 | A modified retained recovery copy causes a per-file failure and no destination write; an intact copy still follows FR-1.32 and FR-1.37–FR-1.42. | [T-020](THREAT_MODEL.md#t-020) |
| FR-3.18 | Before MusicBrainz lookup and Bandcamp handoff, the recipient and outgoing terms/identifiers are available with sharing both enabled and disabled. | [T-011](THREAT_MODEL.md#t-011) |
| FR-3.19 | Invalidate a revision between pages: no mixed or partial ranking is displayed; the fresh query uses current eligibility. | [T-015](THREAT_MODEL.md#t-015), [T-023](THREAT_MODEL.md#t-023) |
| FR-1.45, FR-3.24 | Exercise every processing/response limit at and beyond its bound: failure leaves source files unchanged, continues other file work, and never silently truncates results. | [T-005](THREAT_MODEL.md#t-005), [T-021](THREAT_MODEL.md#t-021) |
| FR-1.46 | Restoration creates a verified copy of the current destination before mutation; disk-full/copy failure cancels restoration and retains earlier copies. | [T-020](THREAT_MODEL.md#t-020) |
| FR-3.20–FR-3.23, FR-4.28 | Cover cohorts of four/five other libraries and candidate support of two/three; exclusions and exact qualifying-result order hold. Responses contain no contributor counts/identities/suppressed releases. Run the inference checks in SC-009 before service release. | [T-004](THREAT_MODEL.md#t-004), [T-008](THREAT_MODEL.md#t-008), [T-010](THREAT_MODEL.md#t-010) |
| FR-4.29–FR-4.30, FR-4.32 | Reject expired/reused invitations and racing reuse without partial accounts; equivalent username case shares uniqueness and throttle identity; every admission limit returns the defined failure. | [T-001](THREAT_MODEL.md#t-001), [T-009](THREAT_MODEL.md#t-009), [T-017](THREAT_MODEL.md#t-017) |
| FR-4.31 | Simulate store loss: unavailable service, empty reprovisioning, new invitations and explicit resubmission; no automatic sharing or change to local music. | [T-025](THREAT_MODEL.md#t-025) |
| FR-4.33–FR-4.34 | Notice and separate sharing consent appear before the applicable action; eligibility is checked before invitations; required release evidence is present before pilot data collection. | [T-010](THREAT_MODEL.md#t-010), [T-011](THREAT_MODEL.md#t-011), [T-012](THREAT_MODEL.md#t-012) |

## Resolved product decisions

Resolved under the maintainer's instruction to use best judgment on 2026-10-20. These are adopted policy choices, not observations of an implemented system. IDs remain reserved for traceability.

| ID | Resolution | Security dependency / threats |
| --- | --- | --- |
| RQ-001 | Privacy eligibility and count suppression are defined in FR-3.20–FR-3.23; disclosure and verification are defined in FR-4.28. Exact ranking remains required for qualifying results. | OD-010; T-004, T-008, T-010 |
| RQ-002 | Operator invitations govern closed-pilot enrollment under FR-4.29 and FR-4.34. | OD-011; T-009, T-017 |
| RQ-003 | Restoration first preserves the current destination under FR-1.46. | OD-016; T-020 |
| RQ-004 | Store-loss behavior and absence of a recovery deadline are explicit in FR-4.31; no-backup controls remain unchanged. | OD-017; T-025 |
| RQ-005 | Account-name acceptance and equivalence are defined in FR-4.30. | OD-015; T-001, T-009 |
