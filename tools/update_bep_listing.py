"""update section about BEP in readme file"""
from __future__ import annotations

from pathlib import Path

from rich import print
from ruamel.yaml import YAML
from utils import bids_website_data
from utils import readme_file

yaml = YAML(typ="safe")


def write_beps(f, beps: list[dict]) -> None:
    f.write("<!-- BEP starts -->\n")

    for section in ["raw", "derivative", "file format"]:
        f.write(f"\n ### {section}\n\n")

        subset = [x for x in beps if section in x["content"]]
        for bep_ in subset:
            f.write(
                f"- [BEP{bep_['number']}](https://bids.neuroimaging.io/bep{bep_['number']}): {bep_['title']}\n"
            )


def main():
    bep_file = bids_website_data() / "beps.yml"
    with open(bep_file, "r") as f:
        beps = yaml.load(f)

    print(readme_file())
    with open(readme_file(), "r") as f:
        readme = f.readlines()

    # update section about BEP

    with open(readme_file(), "w") as f:
        updating = False

        for line in readme:
            if line.startswith("<!-- BEP starts -->"):
                updating = True

                write_beps(f, beps)

            if line.startswith("<!-- BEP ends -->"):
                updating = False

            if not updating:
                f.write(line)


if __name__ == "__main__":
    main()
