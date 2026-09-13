"""Dependency-free validation for the public GitHub profile README."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
REQUIRED_HEADINGS = ("# Bastien Deffradas", "## Featured work", "## Principles")
SECRET_PATTERNS = (
    r"gh" + r"[pousr]_[A-Za-z0-9_]{20,}",
    r"github" + r"_pat_",
    r"sk" + r"-[A-Za-z0-9_-]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN" + r".*PRIVATE" + r" KEY-----",
)
FRENCH_MARKERS = r"\b(bonjour|merci|français|données|développement|utilisation|connexion)\b"


def main() -> None:
    text = README.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    if missing:
        raise SystemExit(f"error: missing required README sections: {', '.join(missing)}")
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in SECRET_PATTERNS):
        raise SystemExit("error: a secret-like signature was detected in README.md")
    if re.search(FRENCH_MARKERS, text, re.IGNORECASE):
        raise SystemExit("error: README.md contains a French-language marker")
    print("Profile validation passed")


if __name__ == "__main__":
    main()
