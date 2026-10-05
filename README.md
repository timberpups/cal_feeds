# cal_feeds

Personal iCalendar feeds for training, trips, and other schedules.

## Calendars

Training calendars, published as iCalendar (`.ics`) feeds.

| File | Calendar | Events |
|---|---|---|
| `nyc_marathon_2026.ics` | NYC Marathon 2026 training plan | 247 |
| `gym_program_2026.ics` | Gym program 2026 — hike prep + 8-week build | 40 |

## Subscribing

Subscribe to the raw file URL in your calendar app (Apple Calendar:
File → New Calendar Subscription; Google Calendar: Other calendars →
From URL):

```
https://raw.githubusercontent.com/timberpups/cal_feeds/main/nyc_marathon_2026.ics
```

Note: subscription refresh requires the repo to be **public**. If the repo is
private, download the `.ics` and import it manually instead.

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
