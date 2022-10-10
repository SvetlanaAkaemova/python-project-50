import itertools


def stylish(res, replacer=' ', spaces_count=2):  # noqa C901

    def walk(val, depth):
        space = replacer * spaces_count * (depth + 1)
        result = ''
        if not isinstance(val, dict):
            return str(val)

        for k, v in val.items():
            if 'operation' in v:
                if v['operation'] == 'unchanged' or v['operation'] == 'nested':
                    result += f"\n{space}  {str(v['key'])}: {walk(v['value'], depth + 2)}"
                elif v['operation'] == 'changed':
                    result += f"\n{space}- {str(v['key'])}: {walk(v['old'], depth + 2)}"
                    result += f"\n{space}+ {str(v['key'])}: {walk(v['new'], depth + 2)}"
                elif v['operation'] == 'removed':
                    result += f"\n{space}- {str(v['key'])}: {walk(v['value'], depth + 2)}"
                elif v['operation'] == 'added':
                    result += f"\n{space}+ {str(v['key'])}: {walk(v['value'], depth + 2)}"
            else:
                result += f'\n{space}  {str(k)}: {walk(v, depth + 2)}'
        res = itertools.chain(
            '{', result, '\n', [replacer * spaces_count * depth + '}']
        )
        return ''.join(res)
    return walk(res, 0)


if __name__ == '__main__':
    stylish(diff_result)  # noqa F821
