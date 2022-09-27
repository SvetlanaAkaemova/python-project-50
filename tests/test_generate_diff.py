import pytest
from gendiff import generate_diff


@pytest.fixture
def path1_json():
    return 'tests/fixtures/file1_example.json'


@pytest.fixture
def path2_json():
    return 'tests/fixtures/file2_example.json'


@pytest.fixture
def path1_yml():
    return 'tests/fixtures/file1_example.yml'


@pytest.fixture
def path2_yml():
    return 'tests/fixtures/file2_example.yml'


def test_generate_diff_json(path1_json, path2_json):
    with open('tests/fixtures/result.txt', 'r') as result:
        assert generate_diff(path1_json, path2_json) == result.read()


def test_generate_diff_yml(path1_yml, path2_yml):
    with open('tests/fixtures/result.txt', 'r') as result:
        assert generate_diff(path1_yml, path2_yml) == result.read()
