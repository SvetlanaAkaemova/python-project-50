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


if __name__ == '__main__':
    bool_to_low(file)  # noqa F821
    common_and_different(file1, file2)  # noqa F821
