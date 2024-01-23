def generate_space(length):
    return ' ' * length


def edit_value(dct_value, depth):
    if isinstance(dct_value, dict):
        result = []
        for key, value in dct_value.items():
            result.append(
                f'{generate_space(depth * 4 - 2)}  {key}: '
                f'{edit_value(value, depth + 1)}'
            )
        result = (
            '{\n'
            + '\n'.join(result)
            + '\n'
            + f'{generate_space((depth - 1) * 4)}'
            + '}'
        )
        return result
    elif dct_value is None:
        return 'null'
    elif isinstance(dct_value, bool):
        return str(dct_value).lower()
    return dct_value


def format_stylish(diff):
    def walk(diff, depth=1):
        lst = []
        for item in diff:
            if 'key' in item:
                if item['flag'] == 'added':
                    lst.append(
                        f'{generate_space(depth * 4 - 2)}+ {item["key"]}: '
                        f'{edit_value(item["value"], depth + 1)}'
                    )
                elif item['flag'] == 'deleted':
                    lst.append(
                        f'{generate_space(depth * 4 - 2)}- {item["key"]}: '
                        f'{edit_value(item["value"], depth + 1)}'
                    )
                elif item['flag'] == 'unchanged':
                    lst.append(
                        f'{generate_space(depth * 4 - 2)}  {item["key"]}: '
                        f'{edit_value(item["value"], depth + 1)}'
                    )
                elif item['flag'] == 'changed':
                    lst.append(
                        f'{generate_space(depth * 4 - 2)}- {item["key"]}: '
                        f'{edit_value(item["old_value"], depth + 1)}'
                    )
                    lst.append(
                        f'{generate_space(depth * 4 - 2)}+ {item["key"]}: '
                        f'{edit_value(item["new_value"], depth + 1)}'
                    )
                elif item['flag'] == 'nested':
                    lst.append(
                        f'{generate_space(depth * 4 - 2)}  {item["key"]}: '
                        f'{walk(item["value"], depth + 1)}'
                    )

        result = (
            '{\n'
            + '\n'.join(lst)
            + '\n'
            + f'{generate_space((depth - 1) * 4)}'
            + '}'
        )
        return result
    return walk(diff)
