import unittest
from datetime import datetime
# Function under test
def convert_date_format(date_str):
    try:
        # Trim spaces
        date_str = date_str.strip()
        # Parse date assuming YYYY-MM-DD
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
        return parsed_date.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid date or format"
class TestConvertDateFormat(unittest.TestCase):
    def test_standard_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
    def test_beginning_of_year(self):
        self.assertEqual(convert_date_format("1999-01-01"), "01-01-1999")
    def test_end_of_year(self):
        self.assertEqual(convert_date_format("2000-12-31"), "31-12-2000")
    def test_leap_year(self):
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")
    def test_invalid_non_leap_year(self):
        self.assertEqual(convert_date_format("2023-02-29"), "Invalid date or format")
    def test_invalid_characters(self):
        self.assertEqual(convert_date_format("abcd-ef-gh"), "Invalid date or format")
    def test_wrong_separator(self):
        self.assertEqual(convert_date_format("2023/10/15"), "Invalid date or format")
    def test_already_in_target_format(self):
        self.assertEqual(convert_date_format("15-10-2023"), "Invalid date or format")
    def test_invalid_month(self):
        self.assertEqual(convert_date_format("2023-13-10"), "Invalid date or format")
        self.assertEqual(convert_date_format("2023-00-05"), "Invalid date or format")
    def test_invalid_day(self):
        self.assertEqual(convert_date_format("2023-10-00"), "Invalid date or format")
        self.assertEqual(convert_date_format("2023-10-32"), "Invalid date or format")
    def test_single_digit_month_day(self):
        self.assertEqual(convert_date_format("2023-5-7"), "07-05-2023")
    def test_empty_string(self):
        self.assertEqual(convert_date_format(""), "Invalid date or format")
    def test_extra_spaces(self):
        self.assertEqual(convert_date_format(" 2023-10-15 "), "15-10-2023")
if __name__ == "__main__":
    unittest.main()