from gendiff.parser import parse_file
from gendiff.generate_tree import get_diff_tree
from gendiff.formatters.json import format_json


def test_format_json():
    data1 = parse_file('tests/fixtures/filepath1.json')
    data2 = parse_file('tests/fixtures/filepath2.json')
    tree = get_diff_tree(data1, data2)
    with open('tests/fixtures/diff_json_format.txt', 'r') as f1:
        content = f1.read()
    assert format_json(tree) == content
