r"""Stop hook: send a reply back when it names an issue or PR without a link.

Reads the hook input on stdin: the assistant's text since the last user
message, from the transcript, plus `last_assistant_message` (the transcript
may not hold the turn's final text yet when Stop fires). Markdown links,
URLs and code are ignored. A bare `#12`, `repo#12`, `PR 12`, `PR-12`,
`GH-12` or `issue 12` that remains blocks the stop once, with the
references to link. Any other input, or a second stop in a row, passes.

`python3 hooks/check-links.py --test` runs the examples below. That a live
host fires it: with this hook in a settings file,
`claude -p "Run \`echo x\`, then reply exactly: Fixed in PR #10." --settings <file> --allowedTools "Bash(echo:*)"`
must be sent back.
"""
import json
import re
import sys

STRIP = [
    re.compile(r"```.*?```|~~~.*?~~~", re.S),  # fenced code
    re.compile(r"`[^`\n]*`"),  # inline code
    re.compile(r"!?\[[^\]\n]*\]\([^)\n]*\)"),  # markdown links and images
    re.compile(r"<https?://[^>\s]*>|https?://\S+"),  # URLs
]
# Not run/build/job/check numbers, not C#/F#; "issue 5 minutes" is not issue 5.
BARE = re.compile(
    r"(?<![&/\w])(?<!\b(?:run|job) )(?<!\bbuild )(?<!\bcheck )(?!(?:[CF]#))(?:[\w.-]+/)?[\w.-]*#\d+\b"
    r"|\b(?:PRs?|pull requests?|issues?)[ \t]+#?\d+\b(?![ \t]+(?:seconds?|minutes?|hours?|days?|weeks?|of)\b)(?!-\d)"
    r"|\b(?:PR|GH)-\d+\b",
    re.I,
)

EXAMPLES = [
    ("Fixed in PR #10.", ["PR #10"]),
    ("See issue 9 and #4.", ["issue 9", "#4"]),
    ("Merged upstream as compound-v#19.", ["compound-v#19"]),
    ("See [#4](https://github.com/o/r/issues/4) and [PR #10](https://github.com/o/r/pull/10).", []),
    ("https://github.com/o/r/pull/10#issuecomment-1 and `#[test]` and `cargo t #3`", []),
    ("```\ngit log  # 12 commits\nissue 5\n```", []),
    ("Rounds 1–9 passed; step 2 of 7; &#123; entity", []),
    ("CI run #512 and build #7 passed; C#12 and F#5 are languages.", []),
    ("An issue 5 minutes ago; issue 2023-01-01.", []),
    ("Tracked as PR-10 and GH-12.", ["PR-10", "GH-12"]),
    ("~~~\nsee #12\n~~~", []),
    ("the issue\n5 lines", []),
]

TRANSCRIPT = [
    {"type": "user", "message": {"content": "old prompt"}},
    {"type": "assistant", "message": {"content": [{"type": "text", "text": "Earlier: issue 3."}]}},
    {"type": "user", "message": {"content": "fix it"}},
    {"type": "assistant", "message": {"content": [{"type": "text", "text": "Working on #4."}, {"type": "tool_use", "id": "t"}]}},
    {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t", "content": "ok #9"}]}},
]


def bare_references(text: str) -> list[str]:
    for pattern in STRIP:
        text = pattern.sub(" ", text)
    found = []
    for m in BARE.finditer(text):
        ref = m.group(0)
        if ref not in found:
            found.append(ref)
    return found


def last_reply(transcript: str) -> str:
    texts: list[str] = []
    with open(transcript, encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            message = entry.get("message") or {}
            content = message.get("content")
            blocks = content if isinstance(content, list) else [{"type": "text", "text": content}] if isinstance(content, str) else []
            if entry.get("type") == "user":
                # A tool result is part of the assistant's turn; a typed message starts a new one.
                if any(b.get("type") == "text" for b in blocks if isinstance(b, dict)):
                    texts = []
            elif entry.get("type") == "assistant":
                texts += [b.get("text", "") for b in blocks if isinstance(b, dict) and b.get("type") == "text"]
    return "\n".join(texts)


def main() -> None:
    try:
        data = json.load(sys.stdin)
        if data.get("stop_hook_active"):
            return
        text = str(data.get("last_assistant_message") or "")
        try:
            text = last_reply(data["transcript_path"]) + "\n" + text
        except (OSError, KeyError, TypeError):
            pass
        refs = bare_references(text)
    except (TypeError, ValueError):
        return
    if refs:
        reason = (
            "Your reply names issues or PRs without a link: "
            + ", ".join(refs)
            + ". Rewrite the reply with each one linked to the URL the tracker reports, like [#123](<URL>)."
            + " If a match is not an issue or PR, reword it."
        )
        print(json.dumps({"decision": "block", "reason": reason}))


if __name__ == "__main__":
    if "--test" in sys.argv:
        import os
        import tempfile

        failed = [(t, want, got) for t, want in EXAMPLES if (got := bare_references(t)) != want]
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write("\n".join(json.dumps(e) for e in TRANSCRIPT))
        # The current turn only, without tool results.
        got = last_reply(f.name)
        os.unlink(f.name)
        if got != "Working on #4.":
            failed.append(("last_reply", "Working on #4.", got))
        for t, want, got in failed:
            print(f"FAIL {t!r}: want {want}, got {got}")
        sys.exit(1 if failed else print(f"{len(EXAMPLES) + 1} examples pass") or 0)
    main()
