def _is_divisible_by(number, divisor):
    return number % divisor == 0

FIZZ_DIVISOR = 3
BUZZ_DIVISOR = 5

FIZZ_STRING = 'Fizz'
BUZZ_STRING = 'Buzz'

def fizzBuzz(number):
    if _is_divisible_by(number, FIZZ_DIVISOR):
        return 'Fizz'
    if _is_divisible_by(number, BUZZ_DIVISOR):
        return 'Buzz'
    return str(number)
