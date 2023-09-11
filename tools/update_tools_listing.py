"""update section about BEP in readme file"""
from __future__ import annotations

from rich import print
from ruamel.yaml import YAML
from utils import bids_website_data
from utils import link
from utils import readme_file

yaml = YAML(typ="safe")


def write_tools(f, tools: list[dict]) -> None:
    f.write("<!-- TOOLS starts -->\n")

    # osrt tools by name

    tools = sorted(tools, key=lambda x: x["name"].lower())

    for tool_ in tools:
        f.write(f"- [{tool_['name']}]({link(tool_)}): {tool_['description']}\n")


def main():
    bep_file = bids_website_data() / "tools.yml"
    with open(bep_file, "r") as f:
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
