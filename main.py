"""Resignation letter runner.

Loads the one-line resignation letter from entry.txt and prints it.
The entry itself is the whole submission: one line, at most 140 chars.
"""

from pathlib import Path


def load_letter(path=None):
    if path is None:
        path = Path(__file__).with_name("entry.txt")
    text = Path(path).read_text(encoding="utf-8")
    letter = text.strip()
    if len(letter) > 140:
        raise ValueError(f"resignation letter is {len(letter)} chars, over the 140-char cap")
    return letter


def main():
    print(load_letter())


if __name__ == "__main__":
    main()
