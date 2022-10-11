import pytest
from gendiff import generate_diff


def test_generate_diff_example_json(path1_plain_json, path2_plain_json):
    with open('tests/fixtures/result_example.txt', 'r') as result:
        assert generate_diff(path1_plain_json, path2_plain_json) == result.read()


def test_generate_diff_example_yml(path1_plain_yml, path2_plain_yml):
    with open('tests/fixtures/result_example.txt', 'r') as result:
        assert generate_diff(path1_plain_yml, path2_plain_yml) == result.read()


def test_generate_diff_json(path1_json, path2_json):
    with open('tests/fixtures/result_stylish.txt', 'r') as result:
        assert generate_diff(path1_json, path2_json) == result.read()
    with open('tests/fixtures/result_plain.txt', 'r') as result:
        assert generate_diff(path1_json, path2_json, 'plain') == result.read()
    with open('tests/fixtures/result_json.txt', 'r') as result:
        assert generate_diff(path1_json, path2_json, 'json') == result.read()


def test_generate_diff_yml(path1_yml, path2_yml):
    with open('tests/fixtures/result_stylish.txt', 'r') as result:
        assert generate_diff(path1_yml, path2_yml) == result.read()
    with open('tests/fixtures/result_plain.txt', 'r') as result:
        assert generate_diff(path1_yml, path2_yml, 'plain') == result.read()
    with open('tests/fixtures/result_json.txt', 'r') as result:
        assert generate_diff(path1_yml, path2_yml, 'json') == result.read()
