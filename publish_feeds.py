#!/usr/bin/env python3
"""Publish tracked ICS feeds from the private source to the public repository."""
import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
PUBLIC_BASE = "https://raw.githubusercontent.com/timberpups/cal-feeds-public/main/"


def git(folder, *args):
    return subprocess.check_output(["git", "-C", str(folder), *args], text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview without committing or pushing")
    args = parser.parse_args()
    tracked = git(ROOT, "ls-files", "-z").split("\0")
    feeds = sorted(name for name in tracked if name and "/" not in name and name.endswith(".ics"))
    if not feeds:
        raise SystemExit("No tracked root-level ICS feeds found.")
    if git(ROOT, "status", "--porcelain", "--", *feeds):
        raise SystemExit("Commit calendar changes in the private repository before publishing.")
    remote = git(ROOT, "remote", "get-url", "public")
    with tempfile.TemporaryDirectory(prefix="cal-feeds-publish-") as temporary:
        checkout = Path(temporary) / "public"
        subprocess.run(["git", "clone", "--branch", "main", "--single-branch", remote, str(checkout)], check=True)
        for name in feeds:
            shutil.copyfile(ROOT / name, checkout / name)
        links = "\n".join(f"- [{name}]({PUBLIC_BASE}{quote(name)})" for name in feeds)
        (checkout / "README.md").write_text(
            "# Public calendar feeds\n\n"
            "Published from the private `timberpups/cal_feeds` working repository. "
            "Edit calendars there and use its publisher to update these feeds.\n\n"
            "## Google Calendar subscriptions\n\n"
            "Choose Other calendars → From URL and add the feeds you want:\n\n"
            + links + "\n\n"
            "Existing subscriptions retain the same URLs. New feeds require a new "
            "subscription. Refresh timing is controlled by Google Calendar. "
            "All files and event details in this repository are public.\n",
            encoding="utf-8",
        )
        subprocess.run(["git", "-C", str(checkout), "add", "--", "README.md", *feeds], check=True)
        changes = git(checkout, "diff", "--cached", "--stat")
        if not changes:
            print("Public feeds are already current.")
            return
        print(changes)
        if args.dry_run:
            print("Preview only; nothing pushed.")
            return
        subprocess.run(["git", "-C", str(checkout), "commit", "-m", "Update published calendar feeds"], check=True)
        subprocess.run(["git", "-C", str(checkout), "push", "origin", "main"], check=True)
        print("Published calendar feeds successfully.")


if __name__ == "__main__":
    main()
