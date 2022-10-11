from gendiff.modules.formaters.plain import plain_format


def test_plain_format(diff_example):
    with open('tests/fixtures/result_plain.txt', 'r') as result:
        assert plain_format(diff_example) == result.read()
