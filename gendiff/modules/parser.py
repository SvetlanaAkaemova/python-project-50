import json
import yaml
from pathlib import Path


def open_file(path):
    extension = Path(path).suffix
    if extension == '.json':
        return json.load(open(path))
    elif extension == '.yml' or extension == '.yaml':
        return yaml.safe_load(Path(path).read_text())


if __name__ == '__main__':
    open_file(path)  # noqa: F821
