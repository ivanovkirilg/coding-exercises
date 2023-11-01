import unittest

from fizzbuzz import fizzBuzz

# Write a fizzBuzz method that accepts a number as input and returns it as a String.

class TestFizzBuzz(unittest.TestCase):
    def test_fizzBuzz_returns_number_as_string(self):
        number = 2

        result = fizzBuzz(number)

        self.assertEqual(result, '2')

unittest.main()
