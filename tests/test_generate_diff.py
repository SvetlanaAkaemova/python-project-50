import json
import pytest
from gendiff import generate_diff
from gendiff.modules.generate_diff import common_and_different


@pytest.fixture
def file1():
    return {'a': 'hexlet', 'b': 'true', 'c': '234'}
   

@pytest.fixture
def file2():
    return {'a': 'hexlet', 'b': 'false', 'd': 33}

@pytest.fixture
def f1():
    return 'tests/fixtures/file1_example.json'


@pytest.fixture
def f2():
    return 'tests/fixtures/file2_example.json'


def test_common_and_different(file1, file2):
    common, only_file1, only_file2 = common_and_different(file1, file2)
    assert common == {'a', 'b'}
    assert only_file1 == {'c'}
    assert only_file2 == {'d'}


def test_generate_diff(f1, f2):
    with open('tests/fixtures/result_of_json.txt', 'r') as result:
        assert generate_diff(f1, f2) == result.read()
