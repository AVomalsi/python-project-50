import pytest
from gendiff.parser import do_parse
from gendiff.generate_tree import get_raw_tree
from gendiff.formatters.plain import in_flat_format


def test_in_flat_format():
    data1 = do_parse('tests/fixtures/filepath1.json')
    data2 = do_parse('tests/fixtures/filepath2.json')
    tree = get_raw_tree(data1, data2)
    with open('tests/fixtures/diff_flat.txt', 'r') as f1:
        content = f1.read()
    assert in_flat_format(tree) == content
    assert isinstance(in_flat_format(tree), str)