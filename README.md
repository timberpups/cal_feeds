# Calendar feeds

Public iCalendar subscriptions for training and other schedules. The source of
truth is this repository: edit a file, commit, and push to `main`. Google Calendar
fetches updates from the same URL on its own refresh schedule.

## Subscription URLs

| Calendar | Public URL |
|---|---|
| NYC Marathon 2026 Training | [Subscribe / download](https://raw.githubusercontent.com/timberpups/cal_feeds/main/feeds/nyc_marathon_2026.ics) |
| Gym Program 2026 | [Subscribe / download](https://raw.githubusercontent.com/timberpups/cal_feeds/main/feeds/gym_program_2026.ics) |

These URLs require the repository to be public. A GitHub `blob` page is not a
calendar endpoint; use the `raw.githubusercontent.com` links above.

## Structure

```text
feeds/                  Published .ics files; one stable filename per calendar
scripts/validate_feeds.py
.github/workflows/validate-feeds.yml
README.md               Subscription URLs and editing instructions
AGENTS.md               Repository guidance for calendar updates
```

## Add to Google Calendar

On Google Calendar in a desktop browser:

1. Next to **Other calendars**, click **+**, then **From URL**.
2. Paste one subscription URL above and click **Add calendar**.
3. Repeat for other feeds you want. They will appear on your phone under the same
   Google account; check that each calendar is enabled in the phone app.
4. Hide or unsubscribe from obsolete feeds to avoid displaying the old plan.

Use **From URL**, not **Import**. An import creates a one-time copy and does not
follow later repository changes. Google controls refresh timing; this setup
cannot force an immediate refresh or discover new calendars automatically.

## Update or add a calendar

- Edit existing files in `feeds/` without changing their filenames or event UIDs.
- Increment changed events' `SEQUENCE`; update `DTSTAMP` and `LAST-MODIFIED` in UTC.
- Keep the correct event timezone and iCalendar CRLF line endings.
- Run `python3 scripts/validate_feeds.py` before committing.
- Commit and push to `main`. Existing subscriptions keep the same URL.
- To add a calendar, create `feeds/<stable-name>.ics`, add its URL to the table,
  validate, commit and push. Subscribe once to its new URL:

```text
https://raw.githubusercontent.com/timberpups/cal_feeds/main/feeds/<stable-name>.ics
```

The GitHub workflow validates feeds on pushes and pull requests. Raw URLs serve
committed files directly; validation does not delay publication or block a direct
push. If validation fails, correct the feed and push the fix.

## Public content

Everything in this repository, including Git history, is public once visibility
is enabled. Only add calendar details you intend to share publicly. Keep booking
codes, private addresses, credentials and private documents elsewhere. This
repository does not contain a private publication area.

## Training plan revision

The October 5, 2026 update replaces the solo half trial with Staten Island Half
on Sunday October 11, reduces race-week load and uses a recovery-dependent taper.
The provisional NYC goal is about 3:35; faster goals depend on performance,
weather and recovery. Gym entries agree with the running taper. Historical
training entries retain the original plan.
