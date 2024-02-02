from gendiff.parser import parse_file
from gendiff.generate_tree import get_diff_tree
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def get_format(output_format, diff_tree):
    if output_format == 'stylish':
        return format_stylish(diff_tree)
    elif output_format == 'plain':
        return format_plain(diff_tree)
    elif output_format == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError('This format is not supported')


def generate_diff(file1_path, file2_path, output_format='stylish'):
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    tree = get_diff_tree(data1, data2)
    formatted_diff = get_format(output_format, tree)
    return formatted_diff
