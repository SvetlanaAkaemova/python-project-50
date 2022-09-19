import pytest
from gendiff.modules.bool_lower import bool_to_low


@pytest.fixture
def file():
    return {'a': 'hexlet', 'b': True, 'c': '234'}


def test_bool_to_low(file):
    assert bool_to_low(file) == {'a': 'hexlet', 'b': 'true', 'c': '234'}


def test_bool_to_low_for_empty_dict():
    assert bool_to_low({}) == {}
