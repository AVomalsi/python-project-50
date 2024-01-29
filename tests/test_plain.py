from gendiff.parser import parse_file
from gendiff.generate_tree import get_diff_tree
from gendiff.formatters.plain import format_plain


def test_format_plain():
    data1 = parse_file('tests/fixtures/filepath1.json')
    data2 = parse_file('tests/fixtures/filepath2.json')
    tree = get_diff_tree(data1, data2)
    with open('tests/fixtures/diff_flat.txt', 'r') as f1:
        content = f1.read()
    assert format_plain(tree) == content
    assert isinstance(format_plain(tree), str)
