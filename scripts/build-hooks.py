"""Build hooks/session-start.json from hooks/always-on.md.

Run after editing always-on.md; `--check` fails when the JSON is stale.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "hooks" / "always-on.md"
TARGET = ROOT / "hooks" / "session-start.json"
# Read by every session: keep it short (the oh plugin keeps the same kind of budget).
BUDGET = 4_000


def render() -> str:
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": SOURCE.read_text(encoding="utf-8").strip(),
        }
    }
    return json.dumps(payload, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    size = len(SOURCE.read_text(encoding="utf-8").strip())
    if size > BUDGET:
        sys.exit(f"hooks/always-on.md is {size} characters; the budget is {BUDGET}")
    expected = render()
    if "--check" in sys.argv:
        actual = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if actual != expected:
            sys.exit("hooks/session-start.json is stale: run python3 scripts/build-hooks.py")
        print("hooks/session-start.json is up to date")
    else:
        TARGET.write_text(expected, encoding="utf-8")
        print(f"wrote {TARGET.relative_to(ROOT)}")
