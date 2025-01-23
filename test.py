import unittest
from unittest import TestCase

from results import write_or_append_to_file, read_all_lines, read_lines
from records import KEYS, PATIENTS_DATA


class TestDataManipulation(TestCase):
    """Test data manipulation functions"""

    # def test_with_wrong_file_path(self) -> None:
    #     """Test write_to_file function with wrong file path"""
    #     with self.assertRaises(FileNotFoundError):
    #         write_to_file(data=KEYS, file_path="wrong_patients.csv")

    def test_write_keys_to_file(self) -> None:
        """Test write_to_file function"""
        write_or_append_to_file(data=KEYS, file_path="patients_without_data_write.csv")
        with open("patients_without_data_write.csv", "r") as patients_file_obj:
            keys = patients_file_obj.read()
            self.assertEqual(",".join(KEYS)+"\n", keys)

    def test_write_data_to_file(self) -> None:
        """Test write_to_file function"""
        write_or_append_to_file(data=PATIENTS_DATA[0], file_path="patients_without_data_write.csv")
        with open("patients_without_data_write.csv", "r") as patients_file_obj:
            patient_data = patients_file_obj.read()
            self.assertEqual(",".join(list(PATIENTS_DATA[0].values()))+"\n", patient_data)

    def test_write_with_wrong_data_type(self) -> None:
        """Test write_to_file function with wrong data type"""#-
        with self.assertRaises(TypeError):
            write_or_append_to_file(data="wrong_data", file_path="patients_without_data_write.csv")  # type: ignore

    def test_read_all_lines(self) -> None:
        """Test read_all_lines function"""
        content = read_all_lines(file_path="patients_with_data_read.csv")
        self.assertEqual(
            ",".join(KEYS) + "\n" + ",".join(list(PATIENTS_DATA[0].values())) + "\n" + ",".join(list(PATIENTS_DATA[1].values())) + "\n", content
        )


    def test_read_lines_without_skip(self) -> None:
        """Test read_lines function"""
        content = read_lines(file_path="patients_with_data_read.csv", lines=2)
        self.assertEqual(
            [
                ",".join(KEYS) + "\n",
                ",".join(list(PATIENTS_DATA[0].values())) + "\n"
            ],
            content
        )

    def test_append_data_to_file(self) -> None:
        """Test append_to_file function"""
        write_or_append_to_file(data=PATIENTS_DATA[5], file_path="patients_with_data_append.csv", mode="a")
        result = read_lines(file_path="patients_with_data_append.csv", lines=1, skip_line=3)
        self.assertEqual(
            [",".join(list(PATIENTS_DATA[5].values())) + "\n"],
            result
        )

    def test_read_lines_with_skip(self) -> None:
        """Test read_lines function"""
        content = read_lines(file_path="patients_with_data_read.csv", lines=2, skip_line=1)
        self.assertEqual(
            [
                ",".join(list(PATIENTS_DATA[0].values())) + "\n",
                ",".join(list(PATIENTS_DATA[1].values())) + "\n"
            ],
            content
        )


if __name__ == "__main__":
    unittest.main()
