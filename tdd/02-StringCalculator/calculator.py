SEPARATOR = ','
NEWLINE = '\n'

def add(numbers):
    if not numbers:
        return 0

    numbers = numbers.split(SEPARATOR)
    numbers = ( num.split(NEWLINE) for num in numbers )

    int_numbers = []
    for l in numbers:
        for num in l:
            int_numbers.append(int(num))

    return sum(int_numbers)
