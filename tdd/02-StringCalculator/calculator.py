SEPARATORS = (
    ',',
    '\n'
)

def _flatten(nested_lists):
    flat_list = []
    for el in nested_lists:
        flat_list.extend(el)
    return flat_list

def _convert_to_ints(number_strings):
    try:
        return list( map(int, number_strings) )
    except ValueError as exc:
        raise ValueError("found extraneous separator") from exc


def add(numbers):
    if not numbers:
        return 0

    numbers = [numbers]

    for sep in SEPARATORS:
        numbers = _flatten( num.split(sep) for num in numbers )

    return sum(_convert_to_ints(numbers))
