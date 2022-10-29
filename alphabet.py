# Коды символов a и z
A_CODE = 97
Z_CODE = 122
ERROR_CODE = "ERROR!"


# Рассчитывает новые символы для входного списка
def alphabet(codes: list, index):
    if codes[index] >= Z_CODE:
        codes[index] = A_CODE
        return alphabet(codes, index - 1)
    else:
        codes[index] += 1
        return codes


# Конвертирует строку в список кодов
def ord_list(string: str):
    return list(map(ord, list(string[::])))


# Конвертирует список кодов в символы
def chr_list(ord_codes: list):
    return "".join(list(map(chr, ord_codes)))


# Проверяет корректность параметров и расчитывает диапазон строк от start до end
def calculate_values(start: str, end: str):
    if len(start) != len(end):
        return ERROR_CODE
    else:
        if start > end:
            temp = start
            start = end
            end = temp
        res = [start]
        st_code = ord_list(start)
        end_code = ord_list(end)
        if [A_CODE < x < Z_CODE for x in st_code].count(True) or \
                [A_CODE < x < Z_CODE for x in end_code].count(True):
            return ERROR_CODE
        while st_code < end_code:
            st_code = alphabet(st_code, len(start) - 1)
            res.append(chr_list(st_code))
        return res


# Печатает диапазон строк от start_range до end_range
def print_alphabet_values(start_range: str, end_range: str):
    result = calculate_values(start_range, end_range)
    print("\n".join(result) if result != ERROR_CODE else result)
