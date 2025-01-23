from typing import Any, Dict, List, Union


def write_or_append_to_file(file_path: str, data: Union[Dict[str, Any], List[str]], mode: str="w") -> None:
    """
    write or append data to a file

    :param file_path: file path to write data to
    :param data: data to write to file
    :param mode: write mode, default is 'w'

    :return: None
    """
    # data should be of type list or dictionary
        # look at how isinstance and type works to solve this

    # if data is a list, it is the keys of the dictionary
        # look at how to join list items into strings by using the string join method.

    # if data is a dictionary, write the values to the csv in the order below.
        # id,name,age,gender,address,phone_number,email

    # write your own logic here
    def write_or_append_to_file(file_path, data, mode="w"):
    # Check if the data is a list or dictionary
        if not isinstance(data, (list, dict)):
            raise TypeError("Only list or dictionary data types are supported.")

        # Open the file in the given mode
        with open(file_path, mode) as file:
            if isinstance(data, list):
                # Join the list items into a single line
                file.write(",".join(data) + "\n")
            elif isinstance(data, dict):
                keys = ["id", "name", "age", "gender", "address", "phone_number", "email"]
                
                file.write(",".join(str(data.get(key, "")) for key in keys) + "\n")



def read_all_lines(file_path: str, mode: str="r") -> str:
    """
    read all lines from a file

    :param file_path: file path to read lines from
    :param mode: read mode, default is 'r'

    :return: None
    """
    return ""  # write your own logic here


def read_lines(file_path, mode: str="r", lines: int=1, skip_line:int=0) -> List[str]:
    """
    read lines from a file

    :param file_path: file path to read lines from
    :param mode: read mode, default is 'r'
    :param lines: number of lines to read, default is 1, reads first line
    :param skip_line: number of lines to skip, default is 0

    :return: list of lines read
    """
    return []  # write your own logic here


def count_lines_in_file(file_path, mode="r") -> int:
    """
    count lines in a file

    :param file_path: file path to count lines in
    :param mode: read mode, default is 'r'

    :return: number of lines in the file
    """
    return 0  # write your own logic here