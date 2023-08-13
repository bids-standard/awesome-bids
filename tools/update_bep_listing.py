"""update section about BEP in readme file"""
from utils import readme_file
from pathlib import Path
from rich import print
from ruamel.yaml import YAML

yaml = YAML(typ='safe')

bep_file = Path(__file__).parent.parent / "bids-website" / "_data" / "beps.yml"
with open(bep_file, 'r') as f:
    beps = yaml.load(f)


print(readme_file())
with open(readme_file(), 'r') as f:
    readme = f.readlines()



for bep_ in beps:
    print(f"- [BEP{bep_['number']}]https://bids.neuroimaging.io/bep{bep_['number']}")
