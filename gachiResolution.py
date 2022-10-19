# Выводит диапозона строк включая границы
def print_string_interval(start, finish):
    # Валидация строк
    if len(start) != len(finish):
        raise RuntimeError("ERROR! String must be the same length!")

    if start > finish:
        raise RuntimeError("ERROR! start must be <= finish")

    check_string(start)
    check_string(finish)

    # Непосредственно решение
    cur_string = start
    print(cur_string)
    while cur_string != finish:
        cur_string = next_string(cur_string, len(cur_string) - 1)
        print(cur_string)


# Увеличивает код указанного символа в сроке на единицу с учетом переполнения
# (допустимые в строке символы a-z)
def next_string(accumulator, pointer):
    rank_res = chr(ord(accumulator[pointer]) + 1)
    return accumulator[:pointer] + rank_res + accumulator[pointer + 1:] if rank_res <= 'z' \
        else next_string(accumulator[:pointer] + 'a' + accumulator[pointer + 1:], pointer - 1)


# Проверка вхождения символов строки в диапозон a-z
def check_string(string):
    for char in string:
        if char < 'a' or char > 'z':
            raise RuntimeError("ERROR! String must contains only a-z chars!")
