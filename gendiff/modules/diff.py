from gendiff.modules.prepare_data import common_and_different


def diff(dict1, dict2):  # noqa C901
    common, removed, added = common_and_different(dict1, dict2)
    keys = sorted(common | removed | added)
    result = {}
    for key in keys:
        if key in removed:
            description = {
                'key': key, 'operation': 'removed', 'value': dict1[key]}
            result[key] = description
        elif key in added:
            description = {'key': key,
                           'operation': 'added',
                           'value': dict2[key]}
            result[key] = description
        elif key in common and dict1[key] == dict2[key]:
            description = {
                'key': key,
                'operation': 'unchanged',
                'value': dict1[key]}
            result[key] = description
        elif all(
            [key in common,
             dict1[key] != dict2[key],
             isinstance(dict1[key], dict),
             isinstance(dict2[key], dict)]
        ):
            description = {
                'key': key,
                'operation': 'nested',
                'value': diff(dict1[key], dict2[key])}
            result[key] = description
        else:
            description = {
                'key': key,
                'operation': 'changed',
                'old': dict1[key],
                'new': dict2[key]}
            result[key] = description
    return result
