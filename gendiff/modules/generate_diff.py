import json
import itertools


def bool_to_low(file):
    for key, value in file.items():
        if type(value) == bool:
            value = str(value).lower()
            file[key] = value
    return file


def common_and_different(file1, file2):
    common = file1.keys() & file2.keys()
    only_file1 = file1.keys() - file2.keys()
    only_file2 = file2.keys() - file1.keys()
    return common, only_file1, only_file2


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    file1 = bool_to_low(file1)
    file2 = bool_to_low(file2)
    common, only_file1, only_file2  = common_and_different(file1, file2)
    sorted_set = sorted(common|only_file1|only_file2)
    res = ''

    for key in sorted_set:
        if key in common and file1[key] == file2[key]:
            res += f'\n  {key}: {file1[key]}'
        if key in common and file1[key] != file2[key]:
            res+= f'\n- {key}: {file1[key]}'
            res+= f'\n+ {key}: {file2[key]}'
        if key in only_file1:
            res += f'\n- {key}: {file1[key]}'
        if key in only_file2:
            res += f'\n+ {key}: {file2[key]}'
        result = itertools.chain('{', res, '\n}')
    return ''.join(result)



if __name__ == '__main__':
    generate_diff(file1, file2)
