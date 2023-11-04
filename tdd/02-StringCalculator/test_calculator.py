
import unittest

from calculator import add


class TestCalculatorAdd(unittest.TestCase):
    def test_given_empty_input_then_add_returns_0(self):
        '''The method can take up to two numbers, separated by commas,
           and will return their sum as a result. So the inputs can be:
           “”, “1”, “1,2”. For an empty string, it will return 0.'''
        numbers = ""
        result = add(numbers)
        self.assertEqual(result, 0)

    def test_given_one_number_then_add_returns_the_number(self):
        '''The method can take up to two numbers, separated by commas,
           and will return their sum as a result. So the inputs can be:
           “”, “1”, “1,2”. For an empty string, it will return 0.'''
        numbers = "3"
        result = add(numbers)
        self.assertEqual(result, 3)

    def test_given_two_numbers_then_add_returns_their_sum(self):
        '''The method can take up to two numbers, separated by commas,
           and will return their sum as a result. So the inputs can be:
           “”, “1”, “1,2”. For an empty string, it will return 0.'''
        numbers = "1,2"
        result = add(numbers)
        self.assertEqual(result, 1 + 2)

    def test_given_more_numbers_then_add_returns_their_sum(self):
        '''Allow the add method to handle an unknown number of arguments'''
        numbers = "1,2,3,4"
        result = add(numbers)
        self.assertEqual(result, 1 + 2 + 3 + 4)

    def test_given_newline_separator_then_add_returns_sum(self):
        '''Allow the add method to handle newlines as separators,
           instead of comas
            1,2\n3 should return “6”
            2,\n3 is invalid, but no need to clarify it with the program'''
        numbers = "1\n2"
        result = add(numbers)
        self.assertEqual(result, 1 + 2)


if __name__ == '__main__':
    unittest.main()

