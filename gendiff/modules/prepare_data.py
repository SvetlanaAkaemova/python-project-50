import argparse
from pathlib import Path


def parser_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )
    args = parser.parse_args()
    return args


def open_file(path):
    extension = Path(path).suffix
    if extension == '.json':
        format = 'json'
        data = open(path)
    elif extension == '.yml' or extension == '.yaml':
        format = 'yaml'
        data = Path(path).read_text()
    return data, format


def stylish_value(value):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            value = str(value).lower()
            return value
        if value is None:
            value = 'null'
            return value
        else:
            return str(value)
    for k, v in value.items():
        v = stylish_value(v)
        value[k] = v
    return value


def common_and_different(dict1, dict2):
    common = dict1.keys() & dict2.keys()
    removed = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    return common, removed, added


def plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def json_value(value):
    if not isinstance(value, dict):
        if value == '':
            return None
        else:
            return value
    for k, v in value.items():
        v = json_value(v)
        value[k] = v
    return value
