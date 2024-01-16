from gendiff.parser import do_parse


def generate_diff(file1_path, file2_path):
    data1 = do_parse(file1_path)
    data2 = do_parse(file2_path)

    keys = set(data1.keys()) | set(data2.keys())
    keys = sorted(keys)

    diff = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] != data2[key]:
                diff.append(f'  - {key}: {str(data1[key]).lower()}')
                diff.append(f'  + {key}: {str(data2[key]).lower()}')
            else:
                diff.append(f'    {key}: {str(data1[key]).lower()}')
        elif key in data1:
            diff.append(f'  - {key}: {str(data1[key]).lower()}')
        elif key in data2:
            diff.append(f'  + {key}: {str(data2[key]).lower()}')

    result = '{\n' + '\n'.join(diff) + '\n}'
    return result
