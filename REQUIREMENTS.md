# Music Tagging Application Requirements

The original project notes define the purpose. The decisions below resolve their gaps for the first release, as requested by the project owner. They are product decisions, not facts from the original notes.

## Required Requirement Inputs

- Project purpose: Tag a local music collection, review metadata changes, and discover music to buy.
- Primary users / actors: Current user, Admin, and other users who choose to share library data for recommendations.
- Core workflows: Select files or folders; read metadata; select a MusicBrainz match; review and approve changes; edit metadata; view and filter a collection; get recommendations and purchase suggestions.
- Business objects / data entities: Music files, metadata, cover art, collections, accounts, shared release identifiers, recommendations, purchase suggestions, and recovery copies.
- External integrations: MusicBrainz for metadata; the application recommendation service for shared library data; Bandcamp search links for purchase suggestions.
- Authentication / roles: Local functions need no account. Shared recommendations require a signed-in account. Current users control their own data. Admins manage recommendation-service accounts.
- Regulatory or privacy constraints: Applicable legal obligations: UNKNOWN. Product privacy requirements: sharing is optional; share only release identifiers; permit withdrawal and deletion; do not share audio, file paths, or cover art.

## Functional Requirements

### Music Files and Metadata

Supported formats are FLAC, MP3, AAC audio in M4A files, Ogg Vorbis, Ogg Opus, and AIFF. Other formats are outside the first release.

Editable fields are title, artist, album, album artist, track number, track total, disc number, disc total, release date, genre, and front cover art. MusicBrainz recording and release identifiers are also stored fields. A date has the form YYYY, YYYY-MM, or YYYY-MM-DD.

- **FR-1.1** The system MUST read metadata from FLAC files selected by the current user.
- **FR-1.2** The system MUST read metadata from MP3 files selected by the current user.
- **FR-1.3** The system MUST use MusicBrainz as the source of proposed text metadata and MusicBrainz identifiers.
- **FR-1.4** The system MUST show the current and proposed values for each metadata change before approval, including image previews for cover art.
- **FR-1.5** The system MUST obtain approval from the current user for each metadata change before it writes that change to a music file.
- **FR-1.6** The system MUST let the current user manually edit each editable field.
- **FR-1.7** The system MUST read metadata from each additional supported format selected by the current user.
- **FR-1.8** The system MUST let the current user select individual files or folders for collection import.
- **FR-1.9** The system MUST include supported files in all subfolders of a selected folder during import.
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

### Collection Viewer and Filters

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

A release is one MusicBrainz release identifier. A new release is a release absent from the current user's collection. Music tastes mean the collection's artists and genres; the first release has no separate taste profile.

- **FR-3.1** The system MUST show purchase suggestions for releases by collection artists that are absent from the collection, using MusicBrainz release identifiers for comparison.
- **FR-3.2** The system MUST show new-release recommendations from other participating users whose shared libraries have at least one release in common with the current user's shared library.
- **FR-3.3** The system MUST rank recommendations by the number of eligible other libraries that contain the release, with release identifier as the ascending tie breaker.
- **FR-3.4** The system MUST show the artist, release title, and suggestion reason for each purchase suggestion or recommendation.
- **FR-3.5** The system MUST show a Bandcamp search link based on artist and release title for each purchase suggestion.
- **FR-3.6** The system MUST label purchase links as searches with unverified availability.
- **FR-3.7** The system MUST show an empty result with a reason when no release satisfies the suggestion or recommendation rules.
- **FR-3.8** The system MUST exclude collection entries without MusicBrainz release identifiers from collection comparisons and shared-library recommendations.
- **FR-3.9** The system MUST show a retry action when a suggestion or recommendation request fails.

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

## Non-Functional Requirements

### Supported Platforms

The first-release acceptance platforms are Windows 11 24H2 on x64, macOS 15 on Apple silicon, and Ubuntu 24.04 LTS on x64. This is a fixed test scope, not a claim about the latest platform versions.

- **NFR-1.1** The system MUST provide all applicable desktop functions on the specified Windows acceptance platform.
- **NFR-1.2** The system MUST provide all applicable desktop functions on the specified macOS acceptance platform.
- **NFR-1.3** The system MUST provide all applicable desktop functions on the specified Linux acceptance platform.
- **NFR-1.4** The system MUST limit supported user interface platforms to Windows, macOS, and Linux.

### Offline Operation

- **NFR-2.1** The system MUST permit local import, viewing, filtering, manual editing, and recovery without a network connection.

## Open Questions

None remain from OQ-1 through OQ-13. The following decisions close those questions:

- **OQ-1 — Resolved:** Add AAC in M4A, Ogg Vorbis, Ogg Opus, and AIFF to FLAC and MP3. Exclude other formats from the first release.
- **OQ-2 — Resolved:** Import selected files or folders, including subfolders. Read tags, perform user-requested MusicBrainz searches, and write only approved changes. Do not rename, move, or transcode music files.
- **OQ-3 — Resolved:** Use the fields defined under Music Files and Metadata. Users edit descriptive fields and local front cover art. MusicBrainz identifiers come from the selected match. Automatic cover art retrieval is outside the first release.
- **OQ-4 — Resolved:** Require explicit match selection, including when only one candidate exists. Permit search correction for no matches and retry for service failures. Do not guess a match.
- **OQ-5 — Resolved:** Approve or reject per field and file, with an additional action to approve all displayed changes for selected files. Rejection discards the proposal.
- **OQ-6 — Resolved:** Save tags in the original files. Preserve audio and unrelated tags. Create recovery copies before writes, retain them until explicit deletion, and report failures per file with retry support.
- **OQ-7 — Resolved:** Show stored fields, path, format, and duration. Include artist, album, and track views, text search, removal from the collection, and refresh from disk. Playback and other unspecified viewer functions are outside the first release.
- **OQ-8 — Resolved:** Filter cover art by presence, type, and minimum dimensions. Use artist and genre for music tastes. Also filter by album, year, format, and MusicBrainz match status. Combine filters with AND.
- **OQ-9 — Resolved:** New means absent from the collection by release identifier. Purchase suggestions use collection artists. Shared recommendations use libraries with at least one common release and rank candidates by occurrence count. Different editions remain distinct releases.
- **OQ-10 — Resolved:** Provide Bandcamp search links with no availability guarantee. Prices, checkout, payment collection, affiliate tracking, and revenue features are outside the first release.
- **OQ-11 — Resolved:** Use explicit, manual submissions of release identifiers to the recommendation service. Sharing is off by default. Withdrawal deletes the shared library. Do not expose other users' identities or complete libraries.
- **OQ-12 — Resolved:** Local functions need no login. Shared recommendations require an account. Users control only their own data. Admins can suspend and restore service accounts, but cannot access local music files.
- **OQ-13 — Resolved:** Test the first release on Windows 11 24H2 x64, macOS 15 Apple silicon, and Ubuntu 24.04 LTS x64. Other versions, distributions, and processor architectures have no first-release support commitment.
