import itertools


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


def build_string(dictionary, value, sign='  '):
    string = f"{sign}{dictionary['key']}: {value}"
    return string


def stylish_format(diff_result):  # noqa C901

    def walk(node, depth, replacer='  '):
        if not isinstance(node, dict):
            return stylish_value(node)
        space = replacer * (depth + 1)
        strings = ''
        for k, v in node.items():
            if 'operation' not in stylish_value(v):
                strings += f"\n{space}  {k}: {walk(v, depth + 2)}"
            elif v['operation'] == 'nested':
                strings += f"\n{space}  {v['key']}: {walk(v['value'], depth + 2)}"
            elif v['operation'] == 'unchanged':
                strings += f"\n{space}{build_string(v, walk(v['value'], depth + 2), '  ')}"
            elif v['operation'] == 'changed':
                strings += f"\n{space}{build_string(v, walk(v['old'], depth + 2), '- ')}"
                strings += f"\n{space}{build_string(v, walk(v['new'], depth + 2), '+ ')}"
            elif v['operation'] == 'removed':
                strings += f"\n{space}{build_string(v, walk(v['value'], depth + 2), '- ')}"
            elif v['operation'] == 'added':
                strings += f"\n{space}{build_string(v, walk(v['value'], depth + 2), '+ ')}"
        result = itertools.chain('{', strings, '\n', [replacer * depth + '}'])
        return ''.join(result)
    return walk(diff_result, 0)


if __name__ == '__main__':
    stylish_format(diff_result)  # noqa F821
