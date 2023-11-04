SEPARATOR = ','

def add(numbers):
    if not numbers:
        return 0

    numbers = ( int(num) for num in numbers.split(SEPARATOR) )

    return sum(numbers)
