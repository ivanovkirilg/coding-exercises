def _is_divisible_by(number, denominator):
    return number % denominator == 0

def fizzBuzz(number):
    if _is_divisible_by(number, 3):
        return 'Fizz'
    return str(number)

