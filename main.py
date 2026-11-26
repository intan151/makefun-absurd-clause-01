"""The Absurd Clause Contest — entry program.

Writes a single original English sentence (one absurd clause buried
deep inside a terms-of-service agreement) to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
"""

import os

ENTRY = (
    "By using this service, you agree to leave one (1) sock outside "
    "your front door on the first Tuesday of each month for collection "
    "by the Company's sock gnome."
)


def self_check(text: str) -> None:
    """Gate self-check (mirrors RULES.txt): 1-200 chars, not only
    whitespace, single line, no control characters. Raises on failure.
    Does not change the output text."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert all(ord(ch) >= 0x20 or ch in "\t" for ch in text), (
        "entry must not contain control characters"
    )
    assert text.count(".") >= 1 and text.rstrip().endswith("."), (
        "entry must be a single sentence"
    )
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    self_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
