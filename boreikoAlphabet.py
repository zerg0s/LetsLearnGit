# Борейко Елизавета
# группа М3О-109М-20

# Алфавит
# Вводятся 2 строки : например, “aaa” и “abd” одинаковой длины. Нужно вывести полный перебор строк
# от первой до второй в алфавитном порядке

def checkingStrings(row1, row2):
    if len(row1) == 0:
        return True
    elif ord(row1[0]) <= ord(row2[0]):
        return checkingStrings(row1[1:], row2[1:])
    else:
        return False


def shift(row):
    if row[0] <= 'z':
        trow = shift(row[1:])
        if trow[0] == 'a' and trow[0] != row[1]:
            row = chr(ord(row[0]) + 1) + trow
        else:
            row = chr(ord(row[0])) + trow
    if row[0] > 'z':
        row = 'a' + row[1:]
    return row


def alphabetIterating(startString, endString):
    stringToChange = startString
    if len(startString) == len(endString) and startString.isalpha() and endString.isalpha():
        if checkingStrings(startString, endString):
            i = ord(stringToChange[-1]) + 1
            while stringToChange != endString:
                print(stringToChange)
                stringToChange = stringToChange[:-1] + chr(i)
                if stringToChange[-1] > 'z':
                    stringToChange = shift(stringToChange)
                    i = ord(stringToChange[-1]) + 1
                else:
                    i += 1
            print(stringToChange)
    else:
        print("Строки были введены неверно")