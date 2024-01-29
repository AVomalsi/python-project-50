def generate_space(length):
    return ' ' * length


def format_dict(data, depth):
    lines = ['{']
    for key, value in data.items():
        lines.append(
            f'{generate_space(depth * 4 - 2)}  {key}: '
            f'{format_value(value, depth + 1)}'
        )
    output_data = lines + [f'{generate_space((depth - 1) * 4)}}}']
    return '\n'.join(output_data)


def format_value(dct_value, depth):
    if isinstance(dct_value, dict):
        return format_dict(dct_value, depth)
    elif dct_value is None:
        return 'null'
    elif isinstance(dct_value, bool):
        return str(dct_value).lower()
    return dct_value


def format_stylish(diff):
    def walk(diff, depth=1):
        lines = ['{']
        for item in diff:
            if 'key' in item:
                if item['flag'] == 'added':
                    lines.append(
                        f'{generate_space(depth * 4 - 2)}+ {item["key"]}: '
                        f'{format_value(item["value"], depth + 1)}'
                    )
                elif item['flag'] == 'deleted':
                    lines.append(
                        f'{generate_space(depth * 4 - 2)}- {item["key"]}: '
                        f'{format_value(item["value"], depth + 1)}'
                    )
                elif item['flag'] == 'unchanged':
                    lines.append(
                        f'{generate_space(depth * 4 - 2)}  {item["key"]}: '
                        f'{format_value(item["value"], depth + 1)}'
                    )
                elif item['flag'] == 'changed':
                    lines.append(
                        f'{generate_space(depth * 4 - 2)}- {item["key"]}: '
                        f'{format_value(item["old_value"], depth + 1)}'
                    )
                    lines.append(
                        f'{generate_space(depth * 4 - 2)}+ {item["key"]}: '
                        f'{format_value(item["new_value"], depth + 1)}'
                    )
                elif item['flag'] == 'nested':
                    lines.append(
                        f'{generate_space(depth * 4 - 2)}  {item["key"]}: '
                        f'{walk(item["value"], depth + 1)}'
                    )

        output_data = lines + [f'{generate_space((depth - 1) * 4)}}}']
        return '\n'.join(output_data)
    return walk(diff)
