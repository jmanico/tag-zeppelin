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

Behavior and workflows come only from [REQUIREMENTS.md](REQUIREMENTS.md). This document defines presentation, not additional product functions. Existing implementation: UNKNOWN; assume none for this design. The product name is Tag Zeppelin. Use the existing teal tag mark, white canvas, ink text, and platform system typography as the first-release brand identity.

Design decision: use a restrained, light desktop workspace for detailed collection review. The tokens, sizes, layout, and mark below are first-release design decisions made under the project owner's instruction to resolve the design questions; they are not facts supplied by the requirements. Favor legible metadata, explicit decisions, and visible per-file results for current users; keep Admin account actions distinct from collection work.

Format reference: [official DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md). Use its canonical prose sections and token schema.

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

Use a desktop navigation area and a main workspace. Group collection browsing, metadata review and recovery, discovery, and account sharing by the workflows in the requirements. Admin account actions appear in a separate, role-specific area. No mobile workflow is specified.

Use lg for workspace margins, md between groups, sm between related controls, and xs between labels and helpers. Keep search and active filters adjacent to collection results. Show current and proposed metadata side by side when space permits; stack each labeled pair when space is limited. Keep file identity and approval actions associated with their values. Reflow controls before introducing horizontal scrolling; keep any necessary data scrolling within the collection region. The minimum supported content area is 1024 by 640 logical pixels, excluding operating-system window borders. At that size, stack current and proposed values and allow vertical scrolling so every field and approval action remains reachable. Validate collection, review, and confirmation layouts at this size with default text and with text enlarged to 200%; no text or action may be clipped or obscured. Smaller content areas have no first-release support commitment. These are acceptance targets, not claims of completed UI testing.

## Elevation & Depth

Use flat white surfaces, ink outlines, spacing, and headings to establish groups. Do not use shadows, transparency, gradients, or dimmed overlays. Confirmation surfaces have an ink boundary on white and an explicit title. Preserve a visible focus indicator without obscuring its control.

## Shapes

Use sm corners for controls and md for review groups. Use simple outlined icons with text labels for actions. Controls have a minimum target of 32 by 32 logical pixels. Focus uses a 2-pixel teal outline separated from the control by a 2-pixel white gap, so it never depends on teal-to-ink contrast.

The primary mark in [logo.svg](logo.svg) is a teal tag silhouette with a white circular hole. It represents tagging without implying playback. Use it on the white surface, with clear space of one eighth of its displayed width. Preserve its aspect ratio. Verify its silhouette and hole at 16, 32, and 128 pixels. No wordmark or external font is required. Use Tag Zeppelin as the accessible product name when the mark identifies the application; the tag remains the sole primary visual mark.

## Components

- **Actions and fields:** Use one teal primary action per decision group. Secondary actions use ink text and outlines on white. Label every field; place validation text beside the affected field. Show format guidance for dates and positive integers from FR-1.20–FR-1.22. Hover underlines action text; pressed controls gain an inset outline in their permitted foreground color. Disabled controls retain contrast and include a reason.
- **Collection and filters:** Use labeled artist, album, and track views. Rows expose the information in FR-2.1; a detail area holds long fields. Group only the specified filters, show active values and the AND relationship, and provide Clear all. Distinguish removing an entry from deleting a music file. Cover previews use square frames with the full image fitted inside, without cropping.
- **Match selection:** Show search terms, candidate release and recording identity, and explicit selection. Separate no-match feedback with editable terms from request failure with Retry. Do not imply that a sole candidate is already selected (FR-1.13–FR-1.18).
- **Metadata review:** Identify the file, field, Current value, and Proposed value. Show old and new cover previews. Use explicit Approve and Reject controls per field; visually separate the action to approve all displayed changes for selected files. Label pending, rejected, saved, and failed states in words. Show unchanged values without a change badge. Keep failed approved changes visible for retry (FR-1.4–FR-1.5, FR-1.23–FR-1.35).
- **File results and recovery:** Use per-file result rows so one failure does not mask other results. Place the reason and available retry action beside the failure. A recovery choice identifies its file and copy; restoration confirmation names the selected copy. Use explicit deletion labels for recovery copies. Do not show a successful save when recovery-copy creation fails.
- **Discovery:** Separate collection-based purchase suggestions from shared-library recommendations. Show artist, release title, and reason. Label purchase actions Search Bandcamp and state Availability unverified. Empty results show a reason; failed requests show Retry. Do not invent prices, availability, or other users' identities (FR-3.1–FR-3.9).
- **Accounts and sharing:** Keep local work available without sign-in. Present sharing as off initially, show release identifiers before submission, and label an update as replacing the shared library. Separate withdrawal from account deletion; deletion confirmation states its effect on the shared library. Admin controls show account suspension or restoration, without a local-file view (FR-4.1–FR-4.15).
- **Interaction and feedback:** All controls support keyboard operation with visible focus and meaningful names. Keep focus order aligned with reading order. Pair icons with words; announce validation and operation results to assistive technology. Keep error details visible until addressed. Do not use color or motion as the sole state signal.

## Do's and Don'ts

- Do preserve the distinction between proposed changes, approval, and saved results.
- Do reuse the permitted color pairs for every text, boundary, icon, and focus state; verify rendered contrast as well as token contrast.
- Do keep local workflows usable when network functions fail.
- Don't add functions, fields, or filter categories beyond REQUIREMENTS.md.
- Don't replace absent cover art with invented album artwork; use a labeled empty frame.
- Don't use decorative motion, gradients, low-contrast placeholder text, or unlabeled icon actions.
