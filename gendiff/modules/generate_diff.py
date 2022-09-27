import itertools
from gendiff.modules.parser import open_file
from gendiff.modules.prepare_dict import bool_to_low, common_and_different


def generate_diff(path1, path2):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    file1 = bool_to_low(dict1)
    file2 = bool_to_low(dict2)
    common, only_file1, only_file2 = common_and_different(file1, file2)
    sorted_set = sorted(common | only_file1 | only_file2)
    res = ''

    for key in sorted_set:
        if key in common and file1[key] == file2[key]:
            res += f'\n    {key}: {file1[key]}'
        if key in common and file1[key] != file2[key]:
            res += f'\n  - {key}: {file1[key]}'
            res += f'\n  + {key}: {file2[key]}'
        if key in only_file1:
            res += f'\n  - {key}: {file1[key]}'
        if key in only_file2:
            res += f'\n  + {key}: {file2[key]}'
        result = itertools.chain('{', res, '\n}')
    return ''.join(result)


if __name__ == '__main__':
    generate_diff(file1, file2)  # noqa F821
