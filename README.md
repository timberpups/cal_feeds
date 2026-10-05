# cal_feeds

Personal iCalendar feeds for training, trips, and other schedules.

## Calendars

Training calendars, published as iCalendar (`.ics`) feeds.

| File | Calendar | Events |
|---|---|---|
| `nyc_marathon_2026.ics` | NYC Marathon 2026 training plan | 247 |
| `gym_program_2026.ics` | Gym program 2026 — hike prep + 8-week build | 40 |

## Repository roles

- `timberpups/cal_feeds` is the private working repository. Edit calendars here,
  in `/Users/richardchen/Documents/cal_feeds`.
- `timberpups/cal-feeds-public` publishes the ICS files for calendar subscriptions.
  Keep this repository public and preserve its filenames and URLs.
- Career records and résumés live separately in `timberpups/career`.

The private repository is the source of truth. After committing and pushing
calendar updates here, run `python3 publish_feeds.py` to publish the tracked
root-level ICS files. Use `python3 publish_feeds.py --dry-run` to preview changes.
The publisher uses a temporary checkout; no second permanent working folder is
needed. It copies only ICS files and generates a public subscription README.
Review calendar contents before publishing: all published event details are
publicly accessible. Keep private booking or personal details outside these feeds.

## Subscribing

In Google Calendar, choose Other calendars → From URL and add each feed you want:

- [NYC Marathon 2026](https://raw.githubusercontent.com/timberpups/cal-feeds-public/main/nyc_marathon_2026.ics)
- [Gym program 2026](https://raw.githubusercontent.com/timberpups/cal-feeds-public/main/gym_program_2026.ics)

Existing subscriptions to these public URLs continue to work. New feeds require
a new subscription. Google Calendar controls refresh timing; publication may
not appear immediately on your phone. URLs from the private `cal_feeds`
repository are not suitable for unauthenticated calendar subscriptions.

## Marathon update — October 5, 2026

The NYC feed now uses Staten Island Half on Sunday, October 11, with a reduced
race-week workload and recovery-led taper. The provisional NYC goal is about
3:35; 3:25–3:30 depends on the half, conditions, recovery and endurance evidence.
Conflicting October gym build sessions are replaced by rest/mobility until NYC.
Summer pace is interpreted with temperature, humidity/dew point, wind and route
context; no automatic heat correction is applied. October 17 is now an optional
20–24 km rehearsal with at most 6–8 km at marathon pace if fully recovered.

Existing event UIDs are retained and revision metadata incremented, so calendar
subscriptions can update the existing entries. Refresh timing depends on the
calendar app. Historical training entries remain as the original plan.
