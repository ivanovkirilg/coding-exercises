import unittest

from fizzbuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzBuzz_returns_number_as_string(self):
        '''Write a fizzBuzz method that accepts a number as input
           and returns it as a String.'''
        number = 2

        result = fizzBuzz(number)

        self.assertEqual(result, '2')

    def test_fizzBuzz_returns_fizz_for_multiples_of_three(self):
        '''For multiples of three return “Fizz” instead of the number'''
        numbers = 3, 3*2, 3*3

        results = ( fizzBuzz(number) for number in numbers )

        for result in results:
            self.assertEqual(result, 'Fizz')

    def test_fizzBuzz_returns_buzz_for_multiples_of_five(self):
        '''For the multiples of five return “Buzz”'''
        numbers = 5, 5*2, 5*5

        results = ( fizzBuzz(number) for number in numbers )

        for result in results:
            self.assertEqual(result, 'Buzz')

    def test_fizzBuzz_returns_fizzBuzz_for_multiples_of_three_and_five(self):
        '''For numbers that are multiples of both three and five
           return “FizzBuzz”.'''
        numbers = 3*5, 3*5*2, 3*3*5*5

        results = ( fizzBuzz(number) for number in numbers )

        for result in results:
            self.assertEqual(result, 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
