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
    
   # Function to write or append to a file (the one we defined earlier)


    if isinstance(data, list):
        with open(file_path, mode) as file:
            file.write(",".join(map(str, data)) + "\n")
    elif isinstance(data, dict):
        required_keys = ["id", "name", "age", "gender", "address", "phone_number", "email"]
        with open(file_path, mode) as file:
            values = [data.get(key, "") for key in required_keys]
            file.write(",".join(map(str, values)) + "\n")
    else:
        raise TypeError("data must be either a list or a dictionary")


    # Example usage:

    # 1. Define the file path
    file_path = 'user1_data.csv'

    # 2. Create a list to write (this is just an example)
    user_list = ['wilson', 'Abena', 'jackson']

    # 3. Create a dictionary to write (this is also an example)
    user_info = {
    'id': '001',
    'name': 'wil d',
    'age': 3,
    'gender': 'Male',
    'address': 'orange street',
    'phone_number': '0543310512',
    'email': 'wil.d@gmail.com'
}

    # 4. Write or append data to the file

    # Write the list to the file in comma-separated format
    write_or_append_to_file(file_path, user_list, 'w')  # Overwrites the file initially

    # Append the dictionary (user_info) to the same file
    write_or_append_to_file(file_path, user_info, 'a')  # Appends to the file


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