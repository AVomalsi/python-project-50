def get_diff_tree(data1, data2):
    diff = []

    for key in sorted(data1.keys() | data2.keys()):
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data1:
            diff.append({'flag': 'added', 'key': key, 'value': value2})
        elif key not in data2:
            diff.append({'flag': 'deleted', 'key': key, 'value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'flag': 'nested',
                'key': key,
                'value': get_diff_tree(value1, value2)
            })
        elif value1 != value2:
            diff.append({
                'flag': 'changed',
                'key': key,
                'old_value': value1,
                'new_value': value2
            })
        else:
            diff.append({'flag': 'unchanged', 'key': key, 'value': value1})

    return diff
