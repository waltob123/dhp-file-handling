from typing import Any, Dict, List, Union

def write_or_append_to_file(
        data: Union[Dict[str, Any], List[str]], 
        file_path: str = "patients_with_data_append.csv", 
        mode: str="w") -> None:
   
    if not isinstance(data, (list, dict)):
        raise TypeError("Data must be of type list or dictionary")
    with open(file_path, mode, newline='') as file:
        if isinstance(data, list):
            file.write(",".join(data) + "\r\n")
        elif isinstance(data, dict):
            order = ["id", "name", "age", "gender", "address", "phone_number", "email"]
            values = [str(data.get(key, "")) for key in order]
            file.write(",".join(values) + "\r\n")

def read_all_lines(file_path: str = "patients_with_data_read.csv", mode: str="r") -> str:
   
    with open(file_path, mode, newline='') as file:
        return file.read().replace('\r\n', '\n')

def read_lines(file_path: str = "patients_with_data_read.csv", mode: str="r", lines: int=1, skip_line: int=0) -> List[str]:
   
    with open(file_path, mode, newline='') as file:
        all_lines = file.readlines()
        normalized_lines = [line.replace('\r\n', '\n') for line in all_lines]
        return normalized_lines[skip_line:skip_line + lines]

def count_lines_in_file(file_path: str = "patients_without_data_write.csv", mode: str="r") -> int:
   
    with open(file_path, mode, newline='') as file:
        return sum(1 for _ in file)
