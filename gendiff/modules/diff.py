from gendiff.modules.prepare_dict import bool_and_none_lower, \
    common_and_different, new_value, new_key


def diff(file1, file2):  # noqa C901
    file1 = bool_and_none_lower(file1)
    file2 = bool_and_none_lower(file2)
    common, removed, added = common_and_different(file1, file2)
    sorted_set = sorted(common | removed | added)
    diff_result = {}
    for key in sorted_set:
        if key in removed:
            file1[key] = new_value(file1[key])
            key_new = new_key(key, '- ')
            diff_result[key_new] = file1[key]
        elif key in added:
            file2[key] = new_value(file2[key])
            key_new = new_key(key, '+ ')
            diff_result[key_new] = file2[key]
        elif key in common:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                key_new = new_key(key)
                diff_result[key_new] = diff(file1[key], file2[key])
            elif isinstance(file1[key], dict) or isinstance(file2[key], dict):
                key_new1 = new_key(key, '- ')
                diff_result[key_new1] = new_value(file1[key])
                key_new2 = new_key(key, '+ ')
                diff_result[key_new2] = new_value(file2[key])
            elif file1[key] != file2[key]:
                key_new1 = new_key(key, '- ')
                diff_result[key_new1] = new_value(file1[key])
                key_new2 = new_key(key, '+ ')
                diff_result[key_new2] = new_value(file2[key])
            elif file1[key] == file2[key]:
                key_new = new_key(key)
                diff_result[key_new] = file1[key]
    return diff_result


if __name__ == '__main__':
    diff(file1, file2)  # noqa F821
