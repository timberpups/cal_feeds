# Calendar feed context

## Purpose and user preference

This private repository is the user's working source for iCalendar (`.ics`) feeds.
The user refers to it as `/documents/cal_feeds`; its current local path is
`/Users/richardchen/Documents/cal_feeds`.

Use this repository when creating, uploading, or changing ICS calendars.
When planning a trip and producing a schedule, create a new ICS calendar here
with the itinerary and relevant information so the user can view it in Google
Calendar on their phone. Include useful details such as locations, addresses,
transport, booking references when appropriate, and practical notes in event
descriptions. Do not publish sensitive personal or booking information to a
public feed without the user's explicit authorization.

## Creating and updating feeds

- Read `README.md` and inspect existing feeds before making changes.
- Use a descriptive, stable filename for each new trip or calendar.
- Use the correct local timezone for each event, particularly on trips that
  cross timezones; distinguish timed events from all-day events.
- Preserve existing event UIDs when updating events. Update revision metadata
  so subscribed calendars can recognize changes.
- Validate the ICS structure and check event dates, times, and descriptions.
- Keep the README's calendar list and subscription instructions current.
- Preserve unrelated calendars and archive content.

## Publishing and Google Calendar

Saving a file locally does not publish it. Inspect the repository's remote and
existing publishing workflow before uploading changes, and distinguish local
creation from successful publication in the completion message.

For a new feed, provide its published subscription URL and explain that the user
must subscribe to it in Google Calendar unless an existing subscription is
confirmed. Do not assume that Google Calendar automatically discovers new ICS
files. Existing subscribed feeds refresh according to the calendar service's
schedule, so changes may not appear immediately on the phone.

## Repository and delivery workflow

- Edit calendars only in `/Users/richardchen/Documents/cal_feeds`.
- `origin` points to private `timberpups/cal_feeds`, the only calendar repository.
- Commit and push calendar changes to `origin` when authorized.
- The former public feed repository was deleted at the user's request on
  October 5, 2026. Its URLs no longer work. Do not recreate it or make private
  calendars public without authorization.
- There is currently no automatic Google Calendar subscription endpoint.
  Clearly distinguish a saved or pushed ICS file from a working calendar feed.
- For one-time access, provide the ICS file for Google Calendar import. Imports
  do not automatically update; check for duplicates before repeated imports.
- The user's preference remains automatic calendar access on their phone.
  Establish an authorized hosting or calendar integration before claiming sync.
- Career lives separately in `/Users/richardchen/Documents/career`.
