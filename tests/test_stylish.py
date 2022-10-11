from gendiff.modules.formaters.stylish import stylish_format


def test_stylish_format(diff_example):
    with open('tests/fixtures/result_stylish.txt', 'r') as result:
        assert stylish_format(diff_example) == result.read()
