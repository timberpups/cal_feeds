# Calendar repository

The working source is `/Users/richardchen/Documents/cal_feeds`, with remote
`git@github.com:timberpups/cal_feeds.git` and default branch `main`.

On October 6, 2026 the user requested public subscription endpoints, a clean
structure, and publication through ordinary Git pushes. That request supersedes
the prior instruction to keep this repository private and its feeds unpublished.
Do not recreate a second calendar repository; this is the source of truth.

## Files and publication

- Store every published calendar under `feeds/` with a descriptive stable `.ics`
  filename. Subfolders are allowed; their paths become part of the public URL.
- Subscription URL: `https://raw.githubusercontent.com/timberpups/cal_feeds/main/feeds/<filename>.ics`.
- Current and historical repository content becomes public when repository
  visibility is public. Never add credentials, booking references, private
  addresses, private documents or other sensitive details without explicit
  authorization to publish those details.
- Career records belong in `/Users/richardchen/Documents/career`, not here.
- Preserve unrelated files and historical events. Do not rewrite Git history
  or change existing subscription filenames without user authorization.

## Calendar edits

- Inspect the current feed before editing. Preserve existing event UIDs.
- Increment changed events' SEQUENCE, and update DTSTAMP/LAST-MODIFIED in UTC.
- Use the correct local timezone and exclusive next-day DTEND for all-day events.
- Retain valid escaping, CRLF line endings and UTF-8-safe content-line folding.
- Run `python3 scripts/validate_feeds.py`, check the intended changes, then commit
  and push when authorized. Update README subscription links for new feeds.
- Coordinate overlapping calendars so their prescriptions do not conflict.

## Verify delivery

After publishing, fetch the unauthenticated raw URL and compare its content to
local source. A saved file or successful push alone does not confirm public
availability. Each new feed needs its own Google Calendar From URL subscription.
Google controls refresh timing. Avoid imports and duplicate subscriptions when
updating an existing calendar. Do not claim a calendar has refreshed until its
live events show the intended revision.
