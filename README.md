# Exercise: Implement File Handling Functions

You are tasked with implementing several file handling functions in Python. The functions are designed to perform operations such as writing to files, reading files, counting lines, and appending data.

Your task is to complete the function definitions in `main.py`. **Do not modify the structure of the functions**, only implement the logic inside them.

## Instructions:

1. **Complete the following functions in `main.py`:**
   - `write_or_append_to_file`: Writes or appends data to a file. Ensure that:
     - If the data is a list, write the elements as a single comma-separated line.
     - If the data is a dictionary, write its values in the following order: `id, name, age, gender, address, phone_number, email`.
     - Use `isinstance()` to check the type of the data and raise a `TypeError` if the data is not of type `list` or `dictionary`.

   - `read_all_lines`: Reads all lines from a file and returns them as a string.

   - `read_lines`: Reads a specified number of lines from a file, starting after skipping a given number of lines. Return the selected lines as a list.

   - `count_lines_in_file`: Counts and returns the number of lines in a file.

2. **Testing Your Code:**
   - A test file named `test.py` has been provided to validate your code.
   - **Do not modify `test.py`**.
   - To test your functions, run the test file:
     ```bash
     python test.py
     ```

3. **Test Data:**
   - CSV files have been provided for testing purposes. **Do not modify** these CSV files. They are used by the test file for validation.

4. **Submission:**
   - **Fork the project from GitHub**.
   - **Create a branch** with your `firstname-lastname-result` (e.g., `desmond-asiedu-asamoah-result`).
   - Implement the logic for the functions in `main.py`.
   - Once you have completed your code and tested it, **make a pull request** from your branch to the original repository into the `master` or `main` branch.

5. **Important Notes:**
   - **Do not modify** the `test.py` file or the provided CSV files.
   - Submit only the completed `main.py` file.
   - Ensure all functions are implemented correctly and pass the tests before submitting.
   - No spaces between comma separated values
   - Ensure you end all write data with a new line character ("\n")

## Starter Code (`main.py`):

```python
from typing import Any, Dict, List, Union

def write_or_append_to_file(file_path: str, data: Union[Dict[str, Any], List[str]], mode: str="w") -> None:
    """
    Write or append data to a file.

    :param file_path: File path to write data to
    :param data: Data to write to file
    :param mode: Write mode, default is 'w'

    :return: None
    """
    # Your code here

def read_all_lines(file_path: str, mode: str="r") -> str:
    """
    Read all lines from a file.

    :param file_path: File path to read lines from
    :param mode: Read mode, default is 'r'

    :return: Content of the file as a string
    """
    return ""  # Write your logic here

def read_lines(file_path, mode: str="r", lines: int=1, skip_line:int=0) -> List[str]:
    """
    Read a specified number of lines from a file.

    :param file_path: File path to read lines from
    :param mode: Read mode, default is 'r'
    :param lines: Number of lines to read, default is 1
    :param skip_line: Number of lines to skip, default is 0

    :return: List of lines read
    """
    return []  # Write your logic here

def count_lines_in_file(file_path, mode="r") -> int:
    """
    Count lines in a file.

    :param file_path: File path to count lines in
    :param mode: Read mode, default is 'r'

    :return: Number of lines in the file
    """
    return 0  # Write your logic here
