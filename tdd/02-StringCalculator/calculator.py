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

def _preprocess(lines):
    separator = DEFAULT_SEPARATOR

    if lines[0].startswith(CUSTOM_SEPARATOR_MARKER):
        separator = lines[0][len(CUSTOM_SEPARATOR_MARKER):]
        del lines[0]

    return separator


def add(numbers: str):
    if not numbers:
        return 0

    lines = numbers.split(NEWLINE_SEPARATOR)
    separator = _preprocess(lines)

    number_strings = _flatten( line.split(separator) for line in lines )

    return sum(_convert_to_ints(number_strings))
