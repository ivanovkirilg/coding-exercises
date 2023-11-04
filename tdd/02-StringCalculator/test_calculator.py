
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


if __name__ == '__main__':
    unittest.main()

