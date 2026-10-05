# Calendar feed context

## Purpose and user preference

This repository is the user's home for published iCalendar (`.ics`) feeds.
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
