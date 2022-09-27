import pytest


@pytest.fixture
def file1():
    return {'a': 'hexlet', 'b': 'true', 'c': '234'}


@pytest.fixture
def file2():
    return {'a': 'hexlet', 'b': 'false', 'd': 33}
