from gendiff.parser import parse_file
from gendiff.generate_tree import get_diff_tree
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def generate_diff(file1_path, file2_path, format='stylish'):
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    tree = get_diff_tree(data1, data2)
    if format == 'stylish':
        return format_stylish(tree)
    elif format == 'plain':
        return format_plain(tree)
    elif format == 'json':
        return format_json(tree)
    else:
        raise ValueError('This format is not supported')
