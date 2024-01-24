def edit_value(dct_value):
    if isinstance(dct_value, dict):
        return '[complex value]'
    elif dct_value is None:
        return 'null'
    elif isinstance(dct_value, bool):
        return str(dct_value).lower()
    elif isinstance(dct_value, str):
        return f"'{str(dct_value)}'"
    return dct_value


def in_flat_format(diff, path=''):
    lst = []
    for item in diff:
        if 'key' in item:
            nested_path = f"{path}.{item['key']}" if path else str(item['key'])
            if item['flag'] == 'added':
                lst.append(
                    f"Property '{nested_path}' was added with value: "
                    f"{edit_value(item['value'])}"
                )
            elif item['flag'] == 'deleted':
                lst.append(
                    f"Property '{nested_path}' was removed"
                )
            elif item['flag'] == 'changed':
                lst.append(
                    f"Property '{nested_path}' was updated. "
                    f"From {edit_value(item['old_value'])} to "
                    f"{edit_value(item['new_value'])}"
                )
            elif item['flag'] == 'nested':
                lst.append(in_flat_format(item['value'], nested_path))
    result = '\n'.join(lst)
    return result
