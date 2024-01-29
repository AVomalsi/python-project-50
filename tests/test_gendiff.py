from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/diff_result.txt', 'r') as f1:
        content = f1.read()
    with open('tests/fixtures/plain_diff.txt', 'r') as f2:
        data = f2.read()
    with open('tests/fixtures/json_diff.txt', 'r') as f3:
        result = f3.read()
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json') == content
    assert generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml') == content
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'plain') == data
    assert generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml',
        'json') == result
