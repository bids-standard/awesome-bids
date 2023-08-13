from __future__ import annotations

from pathlib import Path


def readme_file() -> Path:
    """Return the README file."""
    return Path(__file__).parent.parent / "README.md"
