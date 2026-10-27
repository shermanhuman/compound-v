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

FENCED = re.compile(r"```.*?```|~~~.*?~~~", re.S)  # stripped before indented code
STRIP = [
    re.compile(r"(`+)[^\n]*?\1"),  # inline code, any number of backticks
    re.compile(r"!?\[[^\]\n]*\]\([^)\n]*\)"),  # markdown links and images
    re.compile(r"<https?://[^>\s]*>|https?://\S+"),  # URLs
]
# Reference-style links: `[text][ref]`, `[ref][]` and `[ref]` with a `[ref]: url` line.
DEFINITION = re.compile(
    r"""^[ ]{0,3}\[([^\]\n]+)\]:[ \t]*(?:<[^>\n]*>|\S+)(?:[ \t]+(?:"[^"\n]*"|'[^'\n]*'|\([^)\n]*\)))?[ \t]*\r?$""", re.M
)
LIST_ITEM = re.compile(r"^ {0,3}(?:[-*+]|\d{1,9}[.)])(?:\s|$)")
# Not run/build/job numbers, not C#/F#; "issue 5 minutes" is not issue 5.
BARE = re.compile(
    r"(?<![&/\w.-])(?<!\b(?:run|job) )(?<!\bbuild )(?!(?:[CF]#))(?:[\w.-]+/)?[\w.-]*#\d+\b"
    r"|\b(?:PRs?|pull requests?|issues?) #?\d+\b(?! (?:seconds?|minutes?|hours?|days?|weeks?|months?|years?|commits?|times?)\b| of \d)(?!-\d)"
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
    ("I'll check #12; check compound-v#19.", ["#12", "compound-v#19"]),
    ("An issue 5 months ago.", []),
    ("An issue 5 minutes ago; issue 2023-01-01.", []),
    ("Tracked as PR-10 and GH-12.", ["PR-10", "GH-12"]),
    ("~~~\nsee #12\n~~~", []),
    ("the issue\n5 lines", []),
    ("See ``#12`` and `` issue 5 ``.", []),
    ("Intro:\n\n    issue 12\n\nDone.", []),
    ("See [#12][fix] and [#13].\n\n[fix]: https://github.com/o/r/issues/12\n[#13]: https://github.com/o/r/issues/13", []),
    ("See PR 12 of the upstream repository.", ["PR 12"]),
    ("CI run  #512 passed; I fixed the issue 2 commits ago.", []),
    ("- Item\n    - fixed in #12", ["#12"]),
    ("1. Step\n    - see PR #10\n- Item\n\n    See #12 for details.", ["PR #10", "#12"]),
    ("Intro paragraph\n    issue 12 continues", ["issue 12"]),
    ("[note]: this is prose, see #12", ["#12"]),
    ("Done issue 2 of 7 and PR 1 of 3.", []),
    ("- a\n  continued\n\n    See #12", ["#12"]),
    ("- a\n\tfixed #12", ["#12"]),
    ("    code #12\nmore #13", ["#13"]),
    ("[fix]: https://x/y\r\nsee [#12][fix]", []),
]

TRANSCRIPT = [
    {"type": "user", "message": {"content": "old prompt"}},
    {"type": "assistant", "message": {"content": [{"type": "text", "text": "Earlier: issue 3."}]}},
    {"type": "user", "message": {"content": "fix it"}},
    {"type": "assistant", "message": {"content": [{"type": "text", "text": "Working on #4."}, {"type": "tool_use", "id": "t"}]}},
    {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t", "content": "ok #9"}]}},
]


def strip_indented_code(text: str) -> str:
    """Blank out indented code: a four-space or tab line after a blank line,
    outside a list. Indented list items and continuations stay prose, and so
    (a known trade-off) do code right after a heading and code nested in a
    list item."""
    out, prev_blank, in_list, in_code = [], True, False, False
    for line in text.split("\n"):
        indented = line.startswith("    ") or line.startswith("\t")
        if indented and (in_code or (prev_blank and not in_list)):
            in_code = True
            out.append("")
            continue
        in_code = False
        if line.strip():
            in_list = bool(LIST_ITEM.match(line)) or (in_list and line[0] in " \t")
            prev_blank = False
        else:
            prev_blank = True
        out.append(line)
    return "\n".join(out)


def bare_references(text: str) -> list[str]:
    labels = {m.group(1).lower() for m in DEFINITION.finditer(text)}
    text = DEFINITION.sub(" ", text)
    text = strip_indented_code(FENCED.sub(" ", text))
    for pattern in STRIP:
        text = pattern.sub(" ", text)
    text = re.sub(r"\[([^\]\n]+)\](?:\[([^\]\n]*)\])?", lambda m: " " if (m.group(2) or m.group(1)).lower() in labels else m.group(0), text)
    # One space between words, so "run  #512" reads as "run #512".
    text = re.sub(r"[ \t]+", " ", text)
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
            if not isinstance(entry, dict):
                continue
            message = entry.get("message")
            content = message.get("content") if isinstance(message, dict) else None
            blocks = content if isinstance(content, list) else [{"type": "text", "text": content}] if isinstance(content, str) else []
            blocks = [b for b in blocks if isinstance(b, dict)]
            if entry.get("type") == "user":
                # A tool result is part of the assistant's turn; anything else the user sends (text, an image) starts a new one.
                if any(b.get("type") != "tool_result" for b in blocks):
                    texts = []
            elif entry.get("type") == "assistant":
                texts += [b["text"] for b in blocks if b.get("type") == "text" and isinstance(b.get("text"), str)]
    return "\n".join(texts)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(data, dict) or data.get("stop_hook_active"):
        return
    text = data.get("last_assistant_message")
    text = text if isinstance(text, str) else ""
    try:
        text = last_reply(data["transcript_path"]) + "\n" + text
    except Exception:  # a bad transcript must not stop the final-message check
        pass
    refs = bare_references(text)
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
        try:
            got = last_reply(f.name)
        finally:
            os.unlink(f.name)
        if got != "Working on #4.":
            failed.append(("last_reply", "Working on #4.", got))
        # main() checks last_assistant_message even with no transcript.
        import io
        from contextlib import redirect_stdout

        sys.stdin, out = io.StringIO(json.dumps({"last_assistant_message": "Fixed in PR #10."})), io.StringIO()
        with redirect_stdout(out):
            main()
        if "PR #10" not in out.getvalue():
            failed.append(("main", "a block naming PR #10", out.getvalue()))
        # Odd input fails open; an image-only user turn starts a new reply.
        for odd in ["null", "[]", '{"last_assistant_message": 5}']:
            sys.stdin, out = io.StringIO(odd), io.StringIO()
            with redirect_stdout(out):
                main()
            if out.getvalue():
                failed.append(("main", f"no block for {odd}", out.getvalue()))
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write("\n".join(json.dumps(e) for e in [
                {"type": "assistant", "message": {"content": [{"type": "text", "text": "See issue 12."}]}},
                {"type": "user", "message": {"content": [{"type": "image", "source": {}}]}},
                {"message": "oops"},
                {"type": "assistant", "message": {"content": [{"type": "text", "text": "A cat."}]}},
            ]))
        try:
            got = last_reply(f.name)
        finally:
            os.unlink(f.name)
        if got != "A cat.":
            failed.append(("last_reply after an image", "A cat.", got))
        for t, want, got in failed:
            print(f"FAIL {t!r}: want {want}, got {got}")
        sys.exit(1 if failed else print(f"{len(EXAMPLES) + 6} examples pass") or 0)
    main()
