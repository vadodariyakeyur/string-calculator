import unittest
from app import string_calculator


class StringCalculatorTests(unittest.TestCase):

    def test_string_calculator_should_return_zero_on_empty_string(self) -> None:
        result = string_calculator("")
        self.assertEqual(result, 0)

    def test_string_calculator_should_return_seven(self) -> None:
        result = string_calculator("7")
        self.assertEqual(result, 7)

    def test_string_calculator_should_add_two_numbers(self) -> None:
        result = string_calculator("21,19")
        self.assertEqual(result, 40)

        result = string_calculator("15,10")
        self.assertEqual(result, 25)

    def test_string_calculator_should_add_multiple_numbers(self) -> None:
        result = string_calculator("4,9,11")
        self.assertEqual(result, 24)

        result = string_calculator("17,4")
        self.assertEqual(result, 21)

    def test_string_calculator_should_allow_new_line_character_delimiter(self) -> None:
        result = string_calculator("5\n10")
        self.assertEqual(result, 15)

        result = string_calculator("4\n6,7")
        self.assertEqual(result, 17)

        result = string_calculator("\n5,3\n4\n")
        self.assertEqual(result, 12)

    def test_string_calculator_should_allow_custom_delimiter(self) -> None:
        result = string_calculator("//;\n6;7")
        self.assertEqual(result, 13)

        result = string_calculator("//#\n7#4#5")
        self.assertEqual(result, 16)

    def test_string_calculator_should_allow_multiple_character_custom_delimiter(self) -> None:
        result = string_calculator("//;+-\n1;+-2")
        self.assertEqual(result, 3)

        result = string_calculator("//#*o\n4#*o2#*o7")
        self.assertEqual(result, 13)

    def test_string_calculator_negative_number_exception(self) -> None:
        result = None
        try:
            string_calculator("1\n18\n-33,7,-9")
        except ValueError as e:
            result = str(e)
        self.assertEqual(result, "negatives not allowed: [-33, -9]")


if __name__ == '__main__':
    unittest.main()
