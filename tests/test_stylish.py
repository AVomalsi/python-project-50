from gendiff.parser import do_parse
from gendiff.generate_tree import get_raw_tree
from gendiff.formatters.stylish import format_stylish


def test_format_stylish():
    data1 = do_parse('tests/fixtures/filepath1.yaml')
    data2 = do_parse('tests/fixtures/filepath2.yaml')
    tree = get_raw_tree(data1, data2)
    with open('tests/fixtures/diff_filepath.txt', 'r') as f1:
        content = f1.read()
    assert format_stylish(tree) == content
    assert isinstance(format_stylish(tree), str)
