from typing import Any, Dict, List, Union

def write_or_append_to_file(file_path: str, data: Union[Dict[str, Any], List[str]], mode: str="w") -> None:
    """
    Write or append data to a file.

    :param file_path: File path to write data to
    :param data: Data to write to file
    :param mode: Write mode, default is 'w'

    :return: None
    """
    if not isinstance(data, (list, dict)):
        raise TypeError("Data must be of type list or dictionary")

    with open(file_path, mode) as file:
        if isinstance(data, list):
            file.write(",".join(data) + "\n")
        elif isinstance(data, dict):
            required_keys = ["id", "name", "age", "gender", "address", "phone_number", "email"]
            values = [str(data.get(key, "")) for key in required_keys]
            file.write(",".join(values) + "\n")

def read_all_lines(file_path: str, mode: str="r") -> str:
    """
    Read all lines from a file.

    :param file_path: File path to read lines from
    :param mode: Read mode, default is 'r'

    :return: Content of the file as a string
    """
    with open(file_path, mode) as file:
        return file.read()

def read_lines(file_path, mode: str="r", lines: int=1, skip_line: int=0) -> List[str]:
    """
    Read a specified number of lines from a file.

    :param file_path: File path to read lines from
    :param mode: Read mode, default is 'r'
    :param lines: Number of lines to read, default is 1
    :param skip_line: Number of lines to skip, default is 0

    :return: List of lines read
    """
    with open(file_path, mode) as file:
        all_lines = file.readlines()
        return all_lines[skip_line:skip_line + lines]

def count_lines_in_file(file_path, mode="r") -> int:
    """
    Count lines in a file.

    :param file_path: File path to count lines in
    :param mode: Read mode, default is 'r'

    :return: Number of lines in the file
    """
    with open(file_path, mode) as file:
        return sum(1 for _ in file)
