---
version: alpha
name: Tag Zeppelin
description: A quiet desktop workspace for collection review and explicit metadata approval.
colors:
  primary: "#005A50"
  ink: "#172B35"
  surface: "#FFFFFF"
typography:
  heading:
    fontFamily: system-ui
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: system-ui
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: system-ui
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
rounded:
  sm: 4px
  md: 8px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
components:
  workspace:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "{spacing.lg}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  link:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
  review-panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
---

## Overview

[REQUIREMENTS.md](REQUIREMENTS.md) owns behavior and workflows; [ARCHITECTURE.md](ARCHITECTURE.md) owns frontend technology; [SECURITY.md](SECURITY.md) owns security controls. This document owns visual presentation and interaction design.

The product name is Tag Zeppelin. Use a restrained, light desktop workspace for detailed collection review. Brand tokens are defined above; the primary mark is defined under Shapes.

Format reference: [official DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md).

## Colors

Use only the three opaque tokens above for interface colors. White is the canvas; ink carries text, borders, icons, and error messages; teal identifies primary actions, links, and focus. Do not place ink on teal or teal on ink.

| Foreground / background | Contrast | Uses |
| --- | --- | --- |
| ink / surface | 14.65:1 | Body, headings, secondary controls, borders, status icons |
| primary / surface | 8.14:1 | Links, focus, selected outlines, logo |
| surface / primary | 8.14:1 | Primary action labels and icons |

These are the only permitted functional color pairs. They exceed 4.5:1 for normal text and 3:1 for large text and essential graphics. Keep the same pairs for hover, pressed, disabled, selected, and error states; do not reduce opacity. Indicate state with a label, underline, check mark, or border change. Cover art is user content: do not place text or controls over it; place previews within an ink outline on white.

## Typography

Use the platform system interface font. Heading is for view titles; body is for metadata and explanations; label is for actions and field names. Use sentence case. Keep full metadata available through wrapping and a detail area; do not rely on truncation or hover to disclose values. Permit text enlargement without clipping fields or actions.

## Layout

Use a desktop navigation area and a main workspace. Group collection browsing, metadata review and recovery, discovery, and account sharing by the workflows in the requirements. Admin account actions appear in a separate, role-specific area. Frontend implementation is defined in OD-002 in [ARCHITECTURE.md](ARCHITECTURE.md); platform scope is NFR-1.4–NFR-1.5 in [REQUIREMENTS.md](REQUIREMENTS.md).

Use lg for workspace margins, md between groups, sm between related controls, and xs between labels and helpers. Keep search and active filters adjacent to collection results. Show current and proposed metadata side by side when space permits; stack each labeled pair when space is limited. Keep file identity and approval actions associated with their values. Reflow controls before introducing horizontal scrolling; keep any necessary data scrolling within the collection region. The minimum supported content area is 1024 by 640 logical pixels, excluding operating-system window borders. At that size, stack current and proposed values and allow vertical scrolling so every field and approval action remains reachable. Validate collection, review, and confirmation layouts at this size with default text and with text enlarged to 200%; no text or action may be clipped or obscured. Smaller content areas have no first-release support commitment. These are acceptance targets, not claims of completed UI testing.

## Elevation & Depth

Use flat white surfaces, ink outlines, spacing, and headings to establish groups. Do not use shadows, transparency, gradients, or dimmed overlays. Confirmation surfaces have an ink boundary on white and an explicit title. Preserve a visible focus indicator without obscuring its control.

## Shapes

Use sm corners for controls and md for review groups. Use simple outlined icons with text labels for actions. Controls have a minimum target of 32 by 32 logical pixels. Focus uses a 2-pixel teal outline separated from the control by a 2-pixel white gap, so it never depends on teal-to-ink contrast.

The primary mark in [logo.svg](logo.svg) is a teal tag silhouette with a white circular hole. It represents tagging without implying playback. Use it on the white surface, with clear space of one eighth of its displayed width. Preserve its aspect ratio. Verify its silhouette and hole at 16, 32, and 128 pixels. No wordmark or external font is required. Use Tag Zeppelin as the accessible product name when the mark identifies the application; the tag remains the sole primary visual mark.

## Components

- **Actions and fields:** Use one teal primary action per decision group. Secondary actions use ink text and outlines on white. Label every field; place validation text beside the affected field. Show format guidance for dates and positive integers from FR-1.20–FR-1.22. Hover underlines action text; pressed controls gain an inset outline in their permitted foreground color. Disabled controls retain contrast and include a reason.
- **Collection and filters:** Use labeled artist, album, and track views for FR-2.1–FR-2.9 in [REQUIREMENTS.md](REQUIREMENTS.md); a detail area holds long fields. Active filters use visible values and an AND label; the reset action is labeled Clear all. Make entry-removal wording distinct from file deletion. Cover previews use square frames with the full image fitted inside, without cropping; absent art uses a labeled empty frame.
- **Match selection:** Present FR-1.13–FR-1.18 and FR-3.10 in [REQUIREMENTS.md](REQUIREMENTS.md) with visible search terms and candidate identities. Give no-match feedback and request-failure feedback distinct treatments; label the failure action Retry. A sole tagging candidate has no selected appearance until chosen.
- **Metadata review:** Present FR-1.4–FR-1.5 and FR-1.23–FR-1.35 in [REQUIREMENTS.md](REQUIREMENTS.md) using file/field identity and Current value / Proposed value labels. Use Approve and Reject labels; visually separate group approval. Label pending, rejected, saved, and failed states in words. Show unchanged values without a change badge.
- **File results and recovery:** Present FR-1.29–FR-1.34 and FR-1.41–FR-1.42 in [REQUIREMENTS.md](REQUIREMENTS.md) as per-file result rows with reasons and available retry actions adjacent. A recovery choice identifies its file and copy; restoration confirmation names the copy. Use explicit recovery-copy deletion labels.
- **Discovery:** Present FR-3.1–FR-3.17 in [REQUIREMENTS.md](REQUIREMENTS.md) in separate purchase-suggestion and shared-recommendation areas. Label purchase actions Search Bandcamp and state Availability unverified; label failed-request actions Retry.
- **Accounts and sharing:** Present FR-4.1–FR-4.27 in [REQUIREMENTS.md](REQUIREMENTS.md) with sharing state visible and updates labeled as replacement. Separate withdrawal from deletion; deletion confirmation states its effect on the shared library. Keep Admin actions in their role-specific area.
- **Privacy and pilot feedback:** Present FR-3.20–FR-3.23 and FR-4.28 without numerical contributor counts, cohort sizes or suppressed releases. Keep the aggregate reason and privacy-limited empty state distinct from request failure. Present FR-4.29–FR-4.34 using a labeled invitation-token field, username format guidance, separate sharing consent, visible service notice, and clear service-unavailable/re-registration feedback. Do not display invitation secrets in diagnostics or result summaries. Present recovery-before-restore under FR-1.46 in the confirmation explanation; a failed protective copy remains a failure, not a restored state. Threats: [T-001](THREAT_MODEL.md#t-001), [T-004](THREAT_MODEL.md#t-004), [T-009](THREAT_MODEL.md#t-009), [T-010](THREAT_MODEL.md#t-010), [T-020](THREAT_MODEL.md#t-020), [T-025](THREAT_MODEL.md#t-025).
- **External disclosure context:** For FR-3.18, place the receiving service and outgoing terms/identifiers next to the initiating action. Keep the explanation visible with sharing disabled; distinguish MusicBrainz lookups, Bandcamp browser searches, and recommendation-service sharing in words. Threat: [T-011](THREAT_MODEL.md#t-011).
- **Incomplete operations:** Show deletion cleanup as Pending deletion, not success, under FR-4.22. Show invalidated recommendation pages as requiring a fresh query under FR-3.19; do not present their partial ranking as complete. Show FR-1.44 recovery-integrity failure beside the selected copy and preserve the distinction between failure and completed restoration. Threats: [T-012](THREAT_MODEL.md#t-012), [T-020](THREAT_MODEL.md#t-020), [T-022](THREAT_MODEL.md#t-022), [T-023](THREAT_MODEL.md#t-023).
- **Rendering:** Display metadata as plain text. Interpretation prevention is controlled by SC-002 in [SECURITY.md](SECURITY.md).
- **Interaction and feedback:** All controls support keyboard operation with visible focus and meaningful names. Keep focus order aligned with reading order. Pair icons with words; announce validation and operation results to assistive technology. Keep error details visible until addressed. Do not use color or motion as the sole state signal.

## Presentation constraints

Verify rendered contrast as well as token contrast. Do not use decorative motion or low-contrast placeholder text. State distinctions, color pairs, and action labeling are defined in their sections above.
