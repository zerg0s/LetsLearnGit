# Задача #889102: Алфавит
# сделана студентом группы М3О-109М-20 Кремешной Марией
# Дата выполнения 26.10.2020
# Вводятся 2 строки : например, “aaa” и “abd” одинаковой длины.
# Нужно вывести полный перебор строк от первой до второй в алфавитном порядке, т.е.

def slip(stringToChange):
    for i in range(len(stringToChange) - 1, 0, -1):
        if stringToChange[i] > 'z':
            stringToChange = stringToChange[:i - 1] + chr(ord(stringToChange[i - 1]) + 1) + 'a'\
                             + stringToChange[i + 1:]
    return stringToChange


def alphabeticalProcessing(startString, endString):
    while startString != endString:
        print(startString)
        startString = startString[:-1] + chr(ord(startString[-1]) + 1)
        if startString[-1] > 'z':
            startString = slip(startString)

    print(startString)