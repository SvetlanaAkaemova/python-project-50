from gendiff.modules.formaters.json import json_format


def test_json_format(diff_example):
    with open('tests/fixtures/result_json.txt', 'r') as result:
        assert json_format(diff_example) == result.read()
