"""update section about BEP in readme file"""

from __future__ import annotations

from rich import print
from ruamel.yaml import YAML
from utils import bids_website_data, last_commit, link, logo, pypi, readme_file

yaml = YAML(typ="safe")


def write_tools(f, tools: list[dict]) -> None:
    f.write("<!-- TOOLS starts -->\n")

    tools = sorted(tools, key=lambda x: x["name"].lower())

    for tool_ in tools:
        badges = f"{last_commit(tool_)} {pypi(tool_)}"
        badges = f"  <br>{badges}\n" if badges not in ["", " "] else ""
        print(f"adding {tool_['name']}")
        f.write(
            f"- {logo(tool_)}[{tool_['name']}]({link(tool_)}): {tool_['description'].strip()}\n{badges}"
        )


def main():
    tool_file = bids_website_data() / "tools" / "tools.yml"
    with open(tool_file, "r") as f:
        tools = yaml.load(f)

    print(readme_file())
    with open(readme_file(), "r") as f:
        readme = f.readlines()

    with open(readme_file(), "w") as f:
        updating = False

        for line in readme:
            if line.startswith("<!-- TOOLS starts -->"):
                updating = True

                write_tools(f, tools)

            if line.startswith("<!-- TOOLS ends -->"):
                updating = False

            if not updating:
                f.write(line)


if __name__ == "__main__":
    main()
