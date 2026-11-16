#!/usr/bin/env python3
"""Convert one meeting time across IANA time zones, including date changes."""
from __future__ import annotations
import argparse, sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

def offset_label(value: datetime) -> str:
    raw = value.strftime("%z")
    return raw[:3] + ":" + raw[3:] if raw else "unknown"

def convert(day: str, clock: str, source_name: str, targets: list[str]):
    naive = datetime.strptime(f"{day} {clock}", "%Y-%m-%d %H:%M")
    source_zone = ZoneInfo(source_name)
    source = naive.replace(tzinfo=source_zone, fold=0)
    round_trip = source.astimezone(timezone.utc).astimezone(source_zone).replace(tzinfo=None)
    if round_trip != naive:
        raise ValueError(f"{day} {clock} does not exist in {source_name} because of a clock change")
    ambiguous = naive.replace(tzinfo=source_zone, fold=0).utcoffset() != naive.replace(tzinfo=source_zone, fold=1).utcoffset()
    utc_value = source.astimezone(timezone.utc)
    results = []
    for target_name in targets:
        target = utc_value.astimezone(ZoneInfo(target_name))
        delta = (target.date() - source.date()).days
        results.append((target_name, target.strftime("%Y-%m-%d %H:%M"), offset_label(target), delta))
    return source, utc_value, results, ambiguous

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="meeting date in YYYY-MM-DD format")
    parser.add_argument("--time", required=True, help="meeting time in 24-hour HH:MM format")
    parser.add_argument("--from-zone", required=True, help="source IANA timezone, e.g. Asia/Tehran")
    parser.add_argument("--to-zones", required=True, help="comma-separated target zones")
    args = parser.parse_args()
    targets = [item.strip() for item in args.to_zones.split(",") if item.strip()]
    if not targets: parser.error("--to-zones must include at least one timezone")
    try:
        source, utc_value, results, ambiguous = convert(args.date, args.time, args.from_zone, targets)
    except (ValueError, ZoneInfoNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr); return 2
    print(f"Source: {source.strftime('%Y-%m-%d %H:%M')} {args.from_zone} ({offset_label(source)})")
    print(f"UTC:    {utc_value.strftime('%Y-%m-%d %H:%M')} +00:00")
    if ambiguous: print("Note: this local time occurs twice; the earlier occurrence (fold=0) was selected.")
    print()
    print(f"{'TIME ZONE':28} {'LOCAL TIME':20} {'UTC OFFSET':12} DAY")
    print("-" * 68)
    for zone, local, offset, delta in results:
        day_label = "same day" if delta == 0 else ("next day" if delta > 0 else "previous day")
        print(f"{zone:28} {local:20} {offset:12} {day_label}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
