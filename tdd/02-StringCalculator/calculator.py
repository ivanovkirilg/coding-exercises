DEFAULT_SEPARATOR = ','
CUSTOM_SEPARATOR_MARKER = '//'
NEWLINE_SEPARATOR = '\n'

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


def add(numbers: str):
    if not numbers:
        return 0

    if numbers.startswith(CUSTOM_SEPARATOR_MARKER):
        separator = numbers[len(CUSTOM_SEPARATOR_MARKER):].split('\n')[0]
        numbers = numbers.split('\n')[1:]
    else:
        separator = DEFAULT_SEPARATOR
        numbers = [numbers]
    separators = (separator, NEWLINE_SEPARATOR)

    for sep in separators:
        numbers = _flatten( num.split(sep) for num in numbers )

    return sum(_convert_to_ints(numbers))
