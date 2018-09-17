import json

def read_file(data_path: str) -> iter:
    """
        Read content of the file

        Args
            path to a file

        return generaor whose .next() method returns a string without space and new line character
    """
    with open(data_path) as f:
        for line in f:
            yield line.rstrip()

def convert_csj_to_dict(key: str, value: str) -> dict:
    """Convert string in CSJ format into dictionary."""
    header = json.loads(f'[{key}]')
    content = json.loads(f'[{value}]')
    return dict(zip(header, content))

def create_dict_from_csj_file(data_path: str) -> iter:
    """
        Convert content in CSJ file into Python's dictionary

        Args
            path to a file

        return
            generator whose .next() method returns a dictionary which mapping header with content
    """
    lines = read_file(data_path)
    header = next(lines)
    for line in lines:
        yield convert_csj_to_dict(header, line)


def convert_dict_to_csj(data: dict, escape_non_ascii: bool=False) -> tuple:
    """Convert dictionary into string which are pair of header and content."""
    if escape_non_ascii:
        keys = json.dumps(list(data.keys()), ensure_ascii=False)[1:-1]
        values = json.dumps(list(data.values()), ensure_ascii=False)[1:-1]
    else:
        keys = json.dumps(list(data.keys()))[1:-1]
        values = json.dumps(list(data.values()))[1:-1]
    return keys, values

def convert_dict_key_to_csj(data: dict, escape_non_ascii: bool=False) -> string:
    """Convert key of dictionary into string."""
    if escape_non_ascii:
        data = json.dumps(list(data.keys()), ensure_ascii=False)[1:-1]
    else:
        data = json.dumps(list(data.keys()))[1:-1]
    return data

def convert_dict_value_to_csj(data: dict, escape_non_ascii: bool=False) -> string:
    """Convert value into string."""
    if escape_non_ascii:
        data = json.dumps(list(data.values()), ensure_ascii=False)[1:-1]
    else:
        data = json.dumps(list(data.values()))[1:-1]
    return data

def create_csj_file_from_dict(data_path, data_list: list) -> None:
    """
        Create CSJ file from Python' dictionary

        Args
            data_path - path to a file
            data_list - list of dictionary
    """
    header = convert_dict_key_to_csj(data_list[0])
    with open(data_path, 'w') as f:
        f.write(f'{header}\n')
        for data in data_list:
            content = convert_dict_value_to_csj(data, True)
            f.write(f'{content}\n')
