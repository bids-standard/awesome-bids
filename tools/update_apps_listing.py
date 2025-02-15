"""update section about BEP in readme file"""

from __future__ import annotations

from rich import print
from ruamel.yaml import YAML
from utils import BADGE_FORMAT, bids_website_data, readme_file

yaml = YAML(typ="safe")

APPS_TO_SKIP = ["MAGeTbrain", "example"]


def write_apps(f, apps: list[dict]) -> None:
    f.write("<!-- APP starts -->\n")

    apps = sorted(apps, key=lambda x: x["gh"].lower())

    for app_ in apps:
        if any(x in app_["gh"] for x in APPS_TO_SKIP):
            continue
        if app_.get("status") in ["unmaintained"]:
            continue
        print(f"adding: {app_['gh']}")
        f.write(
            f"- [{app_['gh'].split('/')[1]}](https://github.com/{app_['gh']}): {app_['description']}\n  <br>{docker_badge(app_)}\n"
        )


def docker_badge(app: dict):
    badge_img = f"https://img.shields.io/docker/pulls/{app['dh']}.svg{BADGE_FORMAT}"
    return f"[![Docker version]({badge_img})](https://hub.docker.com/r/{app['dh']})"


def main():
    apps_file = bids_website_data() / "tools" / "apps.yml"
    with apps_file.open("r") as f:
        apps = yaml.load(f)
        apps = apps["apps"]

    print(readme_file())
    with readme_file().open("r") as f:
        readme = f.readlines()

    with readme_file().open("w") as f:
        updating = False

        for line in readme:
            if line.startswith("<!-- APP starts -->"):
                updating = True

                write_apps(f, apps)

            if line.startswith("<!-- APP ends -->"):
                updating = False

            if not updating:
                f.write(line)


if __name__ == "__main__":
    main()
