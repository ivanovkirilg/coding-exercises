
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

    def test_given_two_separators_then_add_returns_sum(self):
        '''Allow the add method to handle newlines as separators,
           instead of comas
            1,2\n3 should return “6”
            2,\n3 is invalid, but no need to clarify it with the program'''
        numbers = "1,2\n3"
        result = add(numbers)
        self.assertEqual(result, 1 + 2 + 3)

    def test_given_separator_at_the_end_then_add_raises_exception(self):
        '''Add validation to not to allow a separator at the end
           For example “1,2,” should return an error (or throw an exception)'''
        numbers = "1,2,"
        with self.assertRaises(ValueError) as exc_context:
            add(numbers)
        self.assertIn('separator', str(exc_context.exception))

    def test_given_custom_separator_then_add_returns_sum(self):
        '''Allow the add method to handle different delimiters
           To change the delimiter, the beginning of the input will contain
           a separate line that looks like this:
            //[delimiter]\n[numbers]
            //;\n1;3 should return “4”
            //|\n1|2|3 should return “6”
            //sep\n2sep5 should return “7”
            //|\n1|2,3 is invalid
            and should return an error (or throw an exception) with the message
            “‘|’ expected but ‘,’ found at position 3.”'''
        numbers = "//sep\n1sep2"
        result = add(numbers)
        self.assertEqual(result, 1 + 2)

    def test_given_different_separators_then_add_raises_exception(self):
        '''Allow the add method to handle different delimiters
           To change the delimiter, the beginning of the input will contain
           a separate line that looks like this:
            //[delimiter]\n[numbers]
            //;\n1;3 should return “4”
            //|\n1|2|3 should return “6”
            //sep\n2sep5 should return “7”
            //|\n1|2,3 is invalid
            and should return an error (or throw an exception) with the message
            “‘|’ expected but ‘,’ found at position 3.”'''
        numbers = "//|\n1|2,3"
        with self.assertRaises(ValueError) as exc_context:
            add(numbers)
        self.assertEqual("'|' expected but ',' found at position 3.",
                         str(exc_context.exception))


if __name__ == '__main__':
    unittest.main()

