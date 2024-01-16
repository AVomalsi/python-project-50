import pytest
from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/diff_result.txt', 'r') as f1:
        content = f1.read()
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json') == content
    assert generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml') == content
