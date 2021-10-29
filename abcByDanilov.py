# created by Илья Данилов
# date 27.10.2021
# description Алфавит

def alp_start(start_str, end_str):
    try:
        start_str = start_str.lower()
        end_str = end_str.lower()
        if start_str > end_str and len(start_str) != len(end_str):
            raise ValueError
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        alp_check(start_str, end_str)


def alp_check(first_str, final_str):
    while first_str != final_str:
        print(first_str)
        first_str = first_str[:-1] + chr(ord(first_str[-1]) + 1)
        if first_str[-1] > 'z':
            first_str = alp_shift(first_str)

    print(first_str)


def alp_shift(letter):
    for i in range(len(letter) - 1, 0, -1):
        if letter[i] > 'z':
            letter = letter[:i - 1] + chr(ord(letter[i - 1]) + 1) + 'a' + letter[i + 1:]
    return letter
