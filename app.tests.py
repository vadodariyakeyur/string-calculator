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

if __name__ == '__main__':
    unittest.main()