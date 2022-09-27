from gendiff.modules.prepare_dict import bool_to_low, common_and_different


def test_bool_to_low(file1):
    assert bool_to_low(file1) == {'a': 'hexlet', 'b': 'true', 'c': '234'}


def test_bool_to_low_for_empty_dict():
    assert bool_to_low({}) == {}


def test_common_and_different(file1, file2):
    common, only_file1, only_file2 = common_and_different(file1, file2)
    assert common == {'a', 'b'}
    assert only_file1 == {'c'}
    assert only_file2 == {'d'}
    
