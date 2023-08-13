from __future__ import annotations

from pathlib import Path


def readme_file() -> Path:
    """Return the README file."""
    return Path(__file__).parent.parent / "README.md"


def bids_website_data() -> Path:
    """Return the folder containing the converters listings."""
    return Path(__file__).parent.parent / "bids-website" / "_data"
