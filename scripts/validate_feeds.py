#!/usr/bin/env python3
"""Validate public iCalendar files using the Python standard library."""
from pathlib import Path
from datetime import datetime
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate(path):
    data = path.read_bytes()
    text = data.decode('utf-8')
    if b'\n' in data.replace(b'\r\n', b'') or b'\r' in data.replace(b'\r\n', b''):
        raise ValueError('Use CRLF line endings for iCalendar files')
    if not text.endswith('END:VCALENDAR\r\n'):
        raise ValueError('Missing calendar ending or final CRLF')
    lines = re.sub(r'\r\n[ \t]', '', text).split('\r\n')
    stack, events, event, seen = [], [], None, set()
    for line in lines:
        if not line:
            continue
        if ':' not in line:
            raise ValueError('Content line without a colon')
        field, value = line.split(':', 1)
        key = field.split(';', 1)[0]
        if key == 'BEGIN':
            if not stack and value != 'VCALENDAR':
                raise ValueError('Root component must be VCALENDAR')
            stack.append(value)
            if value == 'VEVENT':
                event = {}
        elif key == 'END':
            if not stack or stack.pop() != value:
                raise ValueError('Unbalanced iCalendar components')
            if value == 'VEVENT':
                events.append(event)
                event = None
        elif event is not None and stack[-1] == 'VEVENT':
            if key in {'UID', 'DTSTART', 'DTEND', 'DTSTAMP', 'SUMMARY', 'SEQUENCE'}:
                if key in event:
                    raise ValueError('Duplicate event property: ' + key)
                event[key] = (field, value)
    if stack:
        raise ValueError('Unclosed components')
    if lines.count('BEGIN:VCALENDAR') != 1 or 'VERSION:2.0' not in lines:
        raise ValueError('Expected one VERSION:2.0 calendar')
    for event in events:
        for key in ('UID', 'DTSTART', 'DTSTAMP', 'SUMMARY'):
            if key not in event or not event[key][1]:
                raise ValueError('Missing event property: ' + key)
        uid = event['UID'][1]
        if uid in seen:
            raise ValueError('Duplicate UID: ' + uid)
        seen.add(uid)
        def date(key):
            field, value = event[key]
            all_day = ';VALUE=DATE' in field
            fmt = '%Y%m%d' if all_day else ('%Y%m%dT%H%M%SZ' if value.endswith('Z') else '%Y%m%dT%H%M%S')
            if all_day and ';TZID=' in field:
                raise ValueError('All-day event must not have TZID')
            return datetime.strptime(value, fmt), all_day
        start, all_day = date('DTSTART')
        if 'DTEND' in event:
            end, end_all_day = date('DTEND')
            if all_day != end_all_day or end <= start:
                raise ValueError('Invalid start/end interval: ' + uid)
        datetime.strptime(event['DTSTAMP'][1], '%Y%m%dT%H%M%SZ')
        if 'SEQUENCE' in event and int(event['SEQUENCE'][1]) < 0:
            raise ValueError('Negative SEQUENCE: ' + uid)
    return len(events)

def main():
    files = sorted((ROOT / 'feeds').rglob('*.ics'))
    if not files:
        print('No feeds found under feeds/', file=sys.stderr)
        return 1
    failed = False
    for path in files:
        try:
            print(f'{path.relative_to(ROOT)}: {validate(path)} events OK')
        except (ValueError, UnicodeError) as exc:
            print(f'{path.relative_to(ROOT)}: {exc}', file=sys.stderr)
            failed = True
    return int(failed)

if __name__ == '__main__':
    sys.exit(main())
