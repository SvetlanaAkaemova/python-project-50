from gendiff.modules.parser import open_file
from gendiff.modules.diff import diff
from gendiff.modules.formaters.stylish import stylish
from gendiff.modules.formaters.plain import plain


def generate_diff(path1, path2, formater='stylish'):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    diff_result = diff(dict1, dict2)
    if formater == 'stylish':
        return stylish(diff_result)
    if formater == 'plain':
        return plain(diff_result)


if __name__ == '__main__':
    generate_diff(path1, path2, formater)  # noqa F821
