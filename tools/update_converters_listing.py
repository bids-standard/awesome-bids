"""update section about BEP in readme file"""
from __future__ import annotations

from pathlib import Path

from rich import print
from ruamel.yaml import YAML
from utils import bids_website_data
from utils import readme_file

yaml = YAML(typ="safe")

BADGE_FORMAT = "?style=plastic"


def link(converter):
    if "documentation" in converter:
        return converter["documentation"]
    return converter["url"]


def comment(converter):
    if converter.get("comment") in [None, ""]:
        return ""
    comment = " " + converter["comment"]
    comment = comment.replace("\n", " ")
    return comment.rstrip(" ")


def last_commit(converter):
    if converter.get("url") in [None, ""]:
        return ""
    badge_img = f"https://img.shields.io/github/last-commit/{converter['url'].replace('https://github.com/', '')}{BADGE_FORMAT}"
    return f"[![Last commit]({badge_img})]({converter['url']})"


def pypi(converter):
    if converter.get("distribution") in [None, ""]:
        return ""
    pypi = [x for x in converter.get("distribution") if x["name"] == "pypi"]
    if not pypi:
        return ""
    pypi = pypi[0]
    badge_img = f"https://badge.fury.io/py/{pypi['url'].replace('https://pypi.org/project/', '').rstrip('/')}.svg"
    return f"[![PyPI version]({badge_img})]({pypi['url']})"


def docker_badge(converter):
    if converter.get("distribution") in [None, ""]:
        return ""
    docker = [x for x in converter.get("distribution") if x["name"] == "dockerhub"]
    if not docker:
        return ""
    docker = docker[0]
    badge_img = f"https://img.shields.io/docker/pulls/{docker['url'].replace('https://hub.docker.com/r/', '').rstrip('/')}.svg{BADGE_FORMAT}"
    return f"[![Docker version]({badge_img})]({docker['url']})"


def language_badge(converter):
    if converter.get("language") in [None, ""]:
        return ""

    badge_string = ""

    if isinstance(converter["language"], str):
        converter["language"] = [converter["language"]]

    for language in converter["language"]:
        if language == "Python":
            color = "blue"
        elif language == "MATLAB":
            color = "orange"
        elif language == "R":
            color = "grey"
        elif language == "C++":
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


def license_badge(converter):
    # from https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba
    if converter.get("license") in [None, ""]:
        return ""

    shields_url = "https://img.shields.io/badge/License-"

    license = converter["license"]

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


def write_converters(readme, converters, section: str):
    # for a section of converters write info about each converter with badges below
    readme.write(f"\n ### {section}\n\n")

    converters = converters[0]["members"]
    sorted_converters = sorted(converters, key=lambda x: x["name"].lower())

    for converter_ in sorted_converters:
        print(converter_)
        readme.write(
            f"- [{converter_['name']}]({link(converter_)}):{comment(converter_)}\n"
        )
        readme.write(
            f"  {language_badge(converter_)}{last_commit(converter_)}{pypi(converter_)}{docker_badge(converter_)}{license_badge(converter_)}\n"
        )


def load_converters(converters_file: Path):
    with open(converters_file, "r") as f:
        return yaml.load(f)


def main():
    with open(readme_file(), "r") as f:
        content = f.readlines()

    with open(readme_file(), "w") as readme:
        updating = False

        for line in content:
            if line.startswith("<!-- Converters starts -->"):
                updating = True

                readme.write("<!-- Converters starts -->\n")

                for file, section in zip(
                    [
                        "converters.yml",
                        "MEEG_converters.yml",
                        "physio_converters.yml",
                        "other_converters.yml",
                    ],
                    ["MRI", "MEEG", "physiological", "others"],
                ):
                    converters_file = bids_website_data() / file
                    converters = load_converters(converters_file)

                    write_converters(readme, converters, section)

            if line.startswith("<!-- Converters ends -->"):
                updating = False

            if not updating:
                readme.write(line)


if __name__ == "__main__":
    main()
