import pytest
from gendiff.modules.diff import diff


@pytest.fixture
def file1_dict_plain():
    return {'b': True, 'a': 'hexlet', 'c': 234}


@pytest.fixture
def file2_dict_plain():
    return {'b': False, 'a': 'hexlet', 'd': None} 


def test_diff_plain(file1_dict_plain, file2_dict_plain, diff_example_plain):
    assert diff(file1_dict_plain, file2_dict_plain) == diff_example_plain


def test_diff(file1_dict, file2_dict, diff_example):
    assert diff(file1_dict, file2_dict) == diff_example
