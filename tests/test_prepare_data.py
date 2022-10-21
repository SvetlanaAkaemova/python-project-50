from gendiff.modules.prepare_data import stylish_value, common_and_different,\
    plain_value, json_value


def test_stylish_value(file1):
    assert stylish_value(False) == 'false'
    assert stylish_value(None) == 'null'
    assert stylish_value(5) == '5'
    assert stylish_value(file1) == {'a': 'hexlet', 'b': 'true', 'c': '234'}


def test_common_and_different(file1, file2):
    common, removed, added = common_and_different(file1, file2)
    assert common == {'a', 'b'}
    assert removed == {'c'}
    assert added == {'d'}


def test_plain_value(file1):
    assert plain_value(file1) == '[complex value]'
    assert plain_value(True) == 'true'
    assert plain_value(False) == 'false'
    assert plain_value(None) == 'null'
    assert plain_value('bar') == "'bar'"


def test_json_value(file1):
    assert json_value(5) == 5
    assert json_value('') is None
    assert json_value(file1) == {'a': 'hexlet', 'b': True, 'c': 234}
