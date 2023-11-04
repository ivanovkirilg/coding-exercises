SEPARATORS = (
    ',',
    '\n'
)

def _flatten(nested_lists):
    flat_list = []
    for el in nested_lists:
        flat_list.extend(el)
    return flat_list

def add(numbers):
    if not numbers:
        return 0

    numbers = [numbers]

    for sep in SEPARATORS:
        numbers = _flatten( num.split(sep) for num in numbers )

    try:
        numbers = [ int(num) for num in numbers ]
    except ValueError as exc:
        raise ValueError("found extraneous separator") from exc

    return sum(numbers)