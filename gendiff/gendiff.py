from gendiff.parser import do_parse
from gendiff.generate_tree import get_raw_tree
from gendiff.formatters.stylish import format_stylish


def generate_diff(file1_path, file2_path, format='stylish'):
    data1 = do_parse(file1_path)
    data2 = do_parse(file2_path)
    tree = get_raw_tree(data1, data2)
    result = format_stylish(tree)
    return result
