def value_to_string(value):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            value = str(value).lower()
            return value
        if value is None:
            value = 'null'
            return value
        else:
            return value
    for k, v in value.items():
        v = value_to_string(v)
        value[k] = v
    return value


def common_and_different(dict1, dict2):
    common = dict1.keys() & dict2.keys()
    removed = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    return common, removed, added


def modified_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif any(
        [value == 'null',
         value == 'true',
         value == 'false']
    ):
        return value
    return f"'{value}'"


def json_value(value):
    if not isinstance(value, dict):
        if value == 'true':
            return True
        elif value == 'false':
            return False
        elif value == 'null' or value == '':
            return None
        else:
            return value
    for k, v in value.items():
        v = json_value(v)
        value[k] = v
    return value


if __name__ == '__main__':
    value_to_ctring(value)  # noqa F821
    common_and_different(dict1, dict2)  # noqa F821
    modified_value(value)  # noqa F821
    json_value(value)  # noqa F821
