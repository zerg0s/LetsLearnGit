A_CODE = 97
Z_CODE = 122
ERROR_CODE = -1
ERROR_STRING = "ERROR!"


def incr_list_ord(string_codes: list[int], index):
    if string_codes[index] + 1 > Z_CODE:
        string_codes[index] = A_CODE
        return incr_list_ord(string_codes, index - 1)
    else:
        string_codes[index] += 1
        return string_codes


def increment_list_ord(string_codes: list[int]):
    return incr_list_ord(string_codes.copy(), len(string_codes) - 1)


def get_str_chr(string_codes: list[int]):
    return ''.join(map(chr, string_codes))


def get_list_ord(string: str):
    return list(map(ord, string))


def is_correct_str(string: str):
    return string.isalpha() and string.islower()


def get_iterating_strs(string1: str, string2: str):
    if len(string1) != len(string2) or string1 > string2 \
            or not is_correct_str(string1) or not is_correct_str(string2):
        raise ValueError
    iter_strs = [string1]
    str_codes = get_list_ord(string1)
    while get_str_chr(str_codes) != string2:
        str_codes = increment_list_ord(str_codes)
        iter_strs.append(get_str_chr(str_codes))
    return iter_strs


def print_iterating_strs(string1: str, string2: str):
    try:
        print('\n'.join(get_iterating_strs(string1, string2)))
    except ValueError:
        print(ERROR_STRING)
