from gendiff.modules.prepare_data import plain_value


def plain_format(diff_result: dict, path: str = None):
    if path is None:
        path = str()
    result = ''
    for k, v in diff_result.items():
        current_path = f"{path}{v['key']}"
        if v['operation'] == 'changed':
            result += f"Property '{current_path}' was updated. From {plain_value(v['old'])} to {plain_value(v['new'])}\n"
        elif v['operation'] == 'removed':
            result += f"Property '{current_path}' was removed\n"
        elif v['operation'] == 'added':
            result += f"Property '{current_path}' was added with value: {plain_value(v['value'])}\n"
        elif v['operation'] == 'nested':
            result += plain_format(v['value'], current_path + '.') + '\n'
    return result[:-1]


if __name__ == '__main__':
    plain_format(diff_result)  # noqa F821
