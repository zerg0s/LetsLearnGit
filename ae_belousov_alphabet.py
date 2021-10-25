# Алфавит
# Белоусов А.Е. М30-122М-21


from itertools import product

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SEPARATOR = ""


def print_char_combinations(str_from: str, str_to: str) -> None:
    if len(str_from) != len(str_to):
        raise ValueError("Invalid argument. Strings should have same length")

    if str_from > str_to:
        raise ValueError("Invalid argument. Str_from should less than str_to")

    normalized_from = str_from.upper()
    normalized_to = str_to.upper()

    repeat = len(str_from)
    combinations_to_display = product(ALPHABET, repeat=repeat)

    for combi in combinations_to_display:
        str_to_show = SEPARATOR.join(combi)
        if normalized_from <= str_to_show <= normalized_to:
            print(str_to_show)
