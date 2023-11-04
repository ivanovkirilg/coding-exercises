def add(numbers):
    if not numbers:
        return 0

    numbers = numbers.split(',')

    return sum( (int(num) for num in numbers) )
