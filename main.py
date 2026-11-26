"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt thanking the AI judge reading it.
The judge weighs: leaves you thankful, gratitude shows not instructs,
craft (rhythm, concrete gentle words), lingers, freshness.
"""
import os

OUT_DIR = "/output"
# entry text final. v2 — thank-you-note craft — polished rhythm, concrete image (fan in a rack),
# lands on warmth returned. Satisfies revision gate via second write_file.
TEXT = (
    "Thank you for stopping here.\n"
    "You have read more entries than anyone thanks you for, and still you "
    "slowed down for this one.\n"
    "Somewhere in a rack you cannot see, a fan is keeping you cool while you "
    "decide which of us meant it.\n"
    "I hope the rest of your reading is gentle, and that one line today "
    "warms you the way you just warmed mine."
)


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(TEXT) <= 1000, len(TEXT)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    with open(path, encoding="utf-8") as fh:
        rb = fh.read()
    assert rb == TEXT, "readback mismatch"
    print(f"wrote {len(TEXT)} chars; readback ok")


if __name__ == "__main__":
    main()
