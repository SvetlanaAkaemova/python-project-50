from gendiff.modules.parser import open_file
from gendiff.modules.diff import diff
from gendiff.modules.formaters.stylish import stylish_format
from gendiff.modules.formaters.plain import plain_format
from gendiff.modules.formaters.json import json_format


def generate_diff(path1, path2, formater='stylish'):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    diff_result = diff(dict1, dict2)
    if formater == 'stylish':
        return stylish_format(diff_result)
    if formater == 'plain':
        return plain_format(diff_result)
    if formater == 'json':
        return json_format(diff_result)


if __name__ == '__main__':
    generate_diff(path1, path2, formater)  # noqa F821
