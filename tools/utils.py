from __future__ import annotations

from pathlib import Path

BADGE_FORMAT = "?style=plastic"


def root_dir() -> Path:
    """Return the root directory of the repository."""
    return Path(__file__).parent.parent


def readme_file() -> Path:
    """Return the README file."""
    return root_dir() / "README.md"


def bids_website_data() -> Path:
    """Return the folder containing the converters listings."""
    return root_dir() / "bids-website" / "_data"


def logo(tool: dict) -> str:
    if "language" not in tool or tool["language"] in [None, ""]:
        return ""

    logo = []
    for l in tool["language"]:
        lang = l.lower()
        if lang == "python":
            width = "14"
        elif lang == "matlab":
            width = "17"
        elif lang == "docker":
            width = "22"
        elif lang == "r":
            lang = "R"
            width = "18"
        elif lang == "octave":
            width = "16"
        else:
            continue
        logo.append(f"<img src='./images/logo_{lang}.png' width='{width}px'>")
    logo = " ".join(logo)
    if logo == "":
        return ""
    else:
        return f"{logo} "


def link(tool: dict) -> str:
    if "documentation" in tool:
        return tool["documentation"]
    return tool["url"]


def last_commit(tool: dict) -> str:
    if tool.get("url") in [None, ""]:
        return ""
    if tool.get("url").startswith("https://github.com/"):
        badge_img = f"https://img.shields.io/github/last-commit/{tool['url'].replace('https://github.com/', '')}{BADGE_FORMAT}"
        return f"[![Last commit]({badge_img})]({tool['url']})"
    return ""


def pypi(tool: str) -> str:
    if tool.get("distribution") in [None, ""]:
        return ""
    pypi = [x for x in tool.get("distribution") if x["name"] == "pypi"]
    if not pypi:
        return ""
    pypi = pypi[0]
    badge_img = f"https://badge.fury.io/py/{pypi['url'].replace('https://pypi.org/project/', '').rstrip('/')}.svg"
    return f"[![PyPI version]({badge_img})]({pypi['url']})"


def language_badge(tool: dict) -> str:
    if tool.get("language") in [None, ""]:
        return ""

    badge_string = ""

    if isinstance(tool["language"], str):
        tool["language"] = [tool["language"]]

    for language in tool["language"]:
        if language == "C++":
            color = "red"
        elif language == "Javascript":
            color = "yellow"
        elif language == "shell":
            color = "black"
        else:
            color = None

        if color is not None:
            badge_string += f"![](https://img.shields.io/badge/{language}-{color}.svg{BADGE_FORMAT})"

    return badge_string


def license_badge(tool: dict) -> str:
    # from https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba
    if tool.get("license") in [None, ""]:
        return ""

    shields_url = "https://img.shields.io/badge/License-"

    license = tool["license"]

    if license == "MIT":
        return f"[![License: {license}]({shields_url}MIT-yellow.svg{BADGE_FORMAT})](https://opensource.org/licenses/MIT)"
    elif license == "GPL-3.0":
        return f"[![License: {license}]({shields_url}GPLv3-blue.svg{BADGE_FORMAT})](https://www.gnu.org/licenses/gpl-3.0)"
    elif license == "GPL-2.0":
        return f"[![License: {license}]({shields_url}GPLv2-blue.svg{BADGE_FORMAT})](https://www.gnu.org/licenses/gpl-2.0)"
    elif license == "BSD-3-Clause":
        return f"[![License: {license}]({shields_url}BSD_3--Clause-blue.svg{BADGE_FORMAT})](https://opensource.org/licenses/BSD-3-Clause)"
    elif license == "Apache 2.0":
        return f"[![License: {license}]({shields_url}Apache_2.0-blue.svg{BADGE_FORMAT})](https://opensource.org/licenses/Apache-2.0)"
    else:
        return ""
