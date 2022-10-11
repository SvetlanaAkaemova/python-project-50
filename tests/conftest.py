import pytest


@pytest.fixture
def file1():
    return {'a': 'hexlet', 'b': True, 'c': 234}


@pytest.fixture
def file2():
    return {'a': 'hexlet', 'b': False, 'd': None}


@pytest.fixture
def path1_plain_json():
    return 'tests/fixtures/file1_example.json'


@pytest.fixture
def path2_plain_json():
    return 'tests/fixtures/file2_example.json'


@pytest.fixture
def path1_plain_yml():
    return 'tests/fixtures/file1_example.yml'


@pytest.fixture
def path2_plain_yml():
    return 'tests/fixtures/file2_example.yml'


@pytest.fixture
def path1_json():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def path2_json():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def path1_yml():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def path2_yml():
    return 'tests/fixtures/file2.yml'


@pytest.fixture
def diff_example():
    return {'common': {'key': 'common', 'operation': 'nested', 'value': {
        'follow': {'key': 'follow', 'operation': 'added', 'value': 'false'},
        'setting1': {'key': 'setting1', 'operation': 'unchanged', 'value': 'Value 1'},
        'setting2': {'key': 'setting2', 'operation': 'removed', 'value': 200},
        'setting3': {'key': 'setting3', 'operation': 'changed', 'old': 'true', 'new': 'null'},
        'setting4': {'key': 'setting4', 'operation': 'added', 'value': 'blah blah'},
        'setting5': {'key': 'setting5', 'operation': 'added', 'value': {'key5': 'value5'}}, 
        'setting6': {'key': 'setting6', 'operation': 'nested', 'value': {
        'doge': {'key': 'doge', 'operation': 'nested', 'value': {'wow': {
        'key': 'wow', 'operation': 'changed', 'old': '', 'new': 'so much'}}},
        'key': {'key': 'key', 'operation': 'unchanged', 'value': 'value'},
        'ops': {'key': 'ops', 'operation': 'added', 'value': 'vops'}}}}},
        'group1': {'key': 'group1', 'operation': 'nested', 'value': {
        'baz': {'key': 'baz', 'operation': 'changed', 'old': 'bas', 'new': 'bars'},
        'foo': {'key': 'foo', 'operation': 'unchanged', 'value': 'bar'},
        'nest': {'key': 'nest', 'operation': 'changed', 'old': {'key': 'value'}, 'new': 'str'}}},
        'group2': {'key': 'group2', 'operation': 'removed', 'value': {
        'abc': 12345, 'deep': {'id': 45}}},
        'group3': {'key': 'group3', 'operation': 'added', 'value': {
        'deep': {'id': {'number': 45}}, 'fee': 100500}}}


@pytest.fixture
def file1_dict():
    return {
        "common": {"setting1": "Value 1", "setting2": 200, "setting3": True,
        "setting6": {"key": "value", "doge": {"wow": ""}}},
        "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
        "group2": {"abc": 12345, "deep": {"id": 45}}
    }


@pytest.fixture
def file2_dict():
    return {
        "common": {"follow": False, "setting1": "Value 1", "setting3": None,
        "setting4": "blah blah", "setting5": {"key5": "value5"},
        "setting6": {"key": "value", "ops": "vops", "doge": {"wow": "so much"}}},
        "group1": {"foo": "bar", "baz": "bars", "nest": "str"},
        "group3": {"deep": {"id": {"number": 45}},"fee": 100500}
    }


@pytest.fixture
def diff_example_simple():
    return {
        'a': {'key': 'a', 'operation': 'unchanged', 'value': 'hexlet'},
        'b': {'key': 'b', 'operation': 'changed', 'old': 'true', 'new': 'false'},
        'c': {'key': 'c', 'operation': 'removed', 'value': 234},
        'd': {'key': 'd', 'operation': 'added', 'value': 'null'}}
