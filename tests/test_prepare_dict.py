from gendiff.modules.prepare_dict import bool_and_none_lower, common_and_different, new_value, new_key


def test_bool_and_none_lower(file1):
    assert bool_and_none_lower(file1) == {'a': 'hexlet', 'b': 'true', 'c': '234'}


def test_bool_and_none_lower(file2):
    assert bool_and_none_lower(file2) == {'a': 'hexlet', 'b': 'false', 'd': 'null'}


def test_bool_and_none_lower_for_empty_dict():
    assert bool_and_none_lower({}) == {}


def test_common_and_different(file1, file2):
    common, removed, added = common_and_different(file1, file2)
    assert common == {'a', 'b'}
    assert removed == {'c'}
    assert added == {'d'}


def test_new_value(file1):
    assert new_value(file1) == {'  a': 'hexlet', '  b': True, '  c': '234'}


def test_new_value_not_dict(value='foo'):
    assert new_value(value='foo') == 'foo'


def test_new_key(key='a'):
    assert new_key(key='a') == '  a'
