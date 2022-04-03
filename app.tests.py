import unittest
from app import string_calculator

class StringCalculatorTests(unittest.TestCase):

    def test_string_calculator_should_return_zero_on_empty_string(self) -> None:
        result = string_calculator("")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()