from gendiff.modules.prepare_data import open_file
from gendiff.modules.parse import parse
from gendiff.modules.diff import diff
from gendiff.modules.formaters.stylish import stylish_format
from gendiff.modules.formaters.plain import plain_format
from gendiff.modules.formaters.json import json_format


def generate_diff(path1, path2, formater='stylish'):
    data1, format1 = open_file(path1)
    data2, format2 = open_file(path2)
    dict1 = parse(data1, format1)
    dict2 = parse(data2, format2)
    diff_result = diff(dict1, dict2)
    if formater == 'stylish':
        return stylish_format(diff_result)
    if formater == 'plain':
        return plain_format(diff_result)
    if formater == 'json':
        return json_format(diff_result)


if __name__ == '__main__':
    generate_diff(path1, path2, formater)  # noqa F821
