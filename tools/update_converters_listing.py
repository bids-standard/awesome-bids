"""update section about BEP in readme file"""

from __future__ import annotations

from pathlib import Path

from rich import print
from ruamel.yaml import YAML
from utils import (
    BADGE_FORMAT,
    bids_website_data,
    language_badge,
    last_commit,
    link,
    logo,
    pypi,
    readme_file,
)

yaml = YAML(typ="safe")


def comment(converter: dict):
    if converter.get("comment") in [None, ""]:
        return ""
    comment = " " + converter["comment"]
    comment = comment.replace("\n", " ")
    return comment.rstrip(" ")


def docker_badge(converter: dict):
    if converter.get("distribution") in [None, ""]:
        return ""
    docker = [x for x in converter.get("distribution") if x["name"] == "dockerhub"]
    if not docker:
        return ""
    docker = docker[0]
    badge_img = f"https://img.shields.io/docker/pulls/{docker['url'].replace('https://hub.docker.com/r/', '').rstrip('/')}.svg{BADGE_FORMAT}"
    return f"[![Docker version]({badge_img})]({docker['url']})"


def write_converters(readme, converters: list[dict], section: str):
    # for a section of converters write info about each converter with badges below
    readme.write(f"\n### {section}\n\n")

    sorted_converters = sorted(converters, key=lambda x: x["name"].lower())

    for converter_ in sorted_converters:
        if section not in converter_["data_types"]:
            continue
        if converter_["status"] != "active":
            continue
        print(converter_)
        readme.write(
            f"- {logo(converter_)} [{converter_['name']}]({link(converter_)}):{comment(converter_)}\n"
        )
        readme.write(
            f"  <br>{language_badge(converter_)}{last_commit(converter_)}{pypi(converter_)}{docker_badge(converter_)}\n"
        )


def load_converters(converters_file: Path) -> list[dict]:
    with open(converters_file, "r") as f:
        return yaml.load(f)


def main():
    converters_file = bids_website_data() / "tools" / "converters.yml"
    converters = load_converters(converters_file)

    sections = []
    for conv in converters:
        sections.extend([data_type for data_type in conv["data_types"]])
    sections = sorted(set(sections))

    with open(readme_file(), "r") as f:
        content = f.readlines()

    with open(readme_file(), "w") as readme:
        updating = False

        for line in content:
            if line.startswith("<!-- Converters starts -->"):
                updating = True

                readme.write("<!-- Converters starts -->\n")
                for section in sections:
                    write_converters(readme, converters, section)

            if line.startswith("<!-- Converters ends -->"):
                updating = False

            if not updating:
                readme.write(line)


if __name__ == "__main__":
    main()
