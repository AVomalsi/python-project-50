def format_value(dct_value):
    if isinstance(dct_value, dict):
        return '[complex value]'
    elif dct_value is None:
        return 'null'
    elif isinstance(dct_value, bool):
        return str(dct_value).lower()
    elif isinstance(dct_value, str):
        return f"'{str(dct_value)}'"
    return dct_value


def format_plain(diff, path=''):
    lines = []
    for item in diff:
        if 'key' in item:
            nested_path = f"{path}.{item['key']}" if path else str(item['key'])
            if item['flag'] == 'added':
                lines.append(
                    f"Property '{nested_path}' was added with value: "
                    f"{format_value(item['value'])}"
                )
            elif item['flag'] == 'deleted':
                lines.append(
                    f"Property '{nested_path}' was removed"
                )
            elif item['flag'] == 'changed':
                lines.append(
                    f"Property '{nested_path}' was updated. "
                    f"From {format_value(item['old_value'])} to "
                    f"{format_value(item['new_value'])}"
                )
            elif item['flag'] == 'nested':
                lines.append(format_plain(item['value'], nested_path))
    result = '\n'.join(lines)
    return result
