import itertools
from gendiff.modules.prepare_data import stylish_value


def stylish_format(diff_result, replacer=' ', spaces_count=2):  # noqa C901

    def walk(value, depth):
        val = stylish_value(value)
        space = replacer * spaces_count * (depth + 1)
        result = ''
        if not isinstance(val, dict):
            return val

        for k, v in val.items():
            if 'operation' in v:
                if v['operation'] == 'unchanged' or v['operation'] == 'nested':
                    result += f"\n{space}  {v['key']}: {walk(v['value'], depth + 2)}"
                elif v['operation'] == 'changed':
                    result += f"\n{space}- {v['key']}: {walk(v['old'], depth + 2)}"
                    result += f"\n{space}+ {v['key']}: {walk(v['new'], depth + 2)}"
                elif v['operation'] == 'removed':
                    result += f"\n{space}- {v['key']}: {walk(v['value'], depth + 2)}"
                elif v['operation'] == 'added':
                    result += f"\n{space}+ {v['key']}: {walk(v['value'], depth + 2)}"
            else:
                result += f'\n{space}  {k}: {walk(v, depth + 2)}'
        res = itertools.chain(
            '{', result, '\n', [replacer * spaces_count * depth + '}']
        )
        return ''.join(res)
    return walk(diff_result, 0)


if __name__ == '__main__':
    stylish_format(diff_result)  # noqa F821
