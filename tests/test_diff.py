import pytest
from gendiff.modules.diff import diff


@pytest.fixture
def file1_dict_simple():
    return {'b': True, 'a': 'hexlet', 'c': 234}


@pytest.fixture
def file2_dict_simple():
    return {'b': False, 'a': 'hexlet', 'd': None} 


def test_diff_plain(file1_dict_simple, file2_dict_simple, diff_example_simple):
    assert diff(file1_dict_simple, file2_dict_simple) == diff_example_simple


def test_diff(file1_dict, file2_dict, diff_example):
    assert diff(file1_dict, file2_dict) == diff_example
