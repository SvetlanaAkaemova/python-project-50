from gendiff.modules.formaters.stylish import stylish_format
from gendiff.modules.formaters.plain import plain_format
from gendiff.modules.formaters.json import json_format


def format_applying(diff_result, formater):
    if formater == 'stylish':
        return stylish_format(diff_result)
    if formater == 'plain':
        return plain_format(diff_result)
    if formater == 'json':
        return json_format(diff_result)
