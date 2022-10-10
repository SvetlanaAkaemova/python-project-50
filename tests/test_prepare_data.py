from gendiff.modules.prepare_data import value_to_string, common_and_different,\
    modified_value


def test_value_to_string(file1):
    assert value_to_string(False) == 'false'
    assert value_to_string(None) == 'null'
    assert value_to_string(5) == '5' 
    assert value_to_string(file1) == {'a': 'hexlet', 'b': 'true', 'c': '234'}


def test_common_and_different(file1, file2):
    common, removed, added = common_and_different(file1, file2)
    assert common == {'a', 'b'}
    assert removed == {'c'}
    assert added == {'d'}


def test_modified_value(file1):
    assert modified_value(file1) == '[complex value]'


def test_modified_value_another_values():
    assert modified_value('true') == 'true'
    assert modified_value('false') == 'false'
    assert modified_value('null') == 'null'
    assert modified_value('bar') == "'bar'"
