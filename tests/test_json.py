import pytest
from gendiff.parser import do_parse
from gendiff.generate_tree import get_raw_tree
from gendiff.formatters.json import get_json_format


def test_get_json_format():
    data1 = do_parse('tests/fixtures/filepath1.json')
    data2 = do_parse('tests/fixtures/filepath2.json')
    tree = get_raw_tree(data1, data2)
    with open('tests/fixtures/diff_json_format.txt', 'r') as f1:
        content = f1.read()
    assert get_json_format(tree) == content