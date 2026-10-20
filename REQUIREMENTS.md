# Music Tagging Application Requirements

## Required Requirement Inputs

- Project purpose: Music tagging application.
- Primary users / actors: Admin, current user, and other users whose music libraries support recommendations.
- Core workflows: Process music files; review metadata changes for approval; edit metadata manually; view and filter a music collection; get music purchase suggestions and new music recommendations.
- Business objects / data entities: Music files, metadata, music collections, user libraries, cover art, music tastes, purchase suggestions, and music recommendations.
- External integrations: MusicBrainz database.
- Authentication / roles: Admin, current user, and other users are named. Authentication and role permissions: UNKNOWN.
- Regulatory or privacy constraints: UNKNOWN.

## Functional Requirements

### Music Files and Metadata

- **FR-1.1** The system MUST support FLAC files in the music tagging workflow.
- **FR-1.2** The system MUST support MP3 files in the music tagging workflow.
- **FR-1.3** The system MUST use the MusicBrainz database as a source of music metadata.
- **FR-1.4** The system MUST show the current user the metadata values before and after each proposed change before it applies the change.
- **FR-1.5** The system MUST obtain approval from the current user before it applies a proposed metadata change.
- **FR-1.6** The system MUST let the current user manually edit music metadata.

### Collection Viewer and Filters

- **FR-2.1** The system MUST let the current user view their music collection.

### Music Suggestions and Recommendations

- **FR-3.1** The system MUST show the current user suggestions for music to buy based on their music collection.
- **FR-3.2** The system MUST show the current user recommendations for new music based on other users' music libraries.

## Non-Functional Requirements

### Supported Platforms

- **NFR-1.1** The system MUST provide a user interface on Windows.
- **NFR-1.2** The system MUST provide a user interface on macOS.
- **NFR-1.3** The system MUST provide a user interface on Linux.
- **NFR-1.4** The system MUST limit supported user interface platforms to Windows, macOS, and Linux.

## Open Questions

- **OQ-1** Which file formats must the system support in addition to FLAC and MP3?
- **OQ-2** How does the current user select music files for processing, and what processing must the system perform?
- **OQ-3** Which metadata fields must the system read, propose changes to, and let the current user edit?
- **OQ-4** How must the system select MusicBrainz matches and handle missing matches, multiple matches, or an unavailable database?
- **OQ-5** Must the user approve changes per field, file, or group of files? What must happen when the user rejects a change?
- **OQ-6** Where must the system save approved metadata changes, and what must happen if it cannot read a file or save a change?
- **OQ-7** What information must the collection viewer show, and what additional functions does “and similar” mean?
- **OQ-8** Which cover art properties and music taste criteria must users be able to filter by? Which additional filter categories are required?
- **OQ-9** What does “new music” mean, and what rules determine which purchase suggestions and recommendations qualify?
- **OQ-10** Does “$$” require a revenue feature? Must purchase suggestions include prices, seller links, or a purchase function?
- **OQ-11** How must the system obtain other users' libraries, and what access permissions or privacy restrictions apply?
- **OQ-12** Which actions must each named actor be permitted to perform, and is authentication required?
- **OQ-13** Which Windows and macOS versions and Linux distributions must the system support?
