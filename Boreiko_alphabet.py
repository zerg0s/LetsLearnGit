# Борейко Елизавета
# группа М3О-109М-20

# Алфавит
# Вводятся 2 строки : например, “aaa” и “abd” одинаковой длины. Нужно вывести полный перебор строк
# от первой до второй в алфавитном порядке

def cheak(row1, row2):
    if len(row1) == 0:
        return True
    elif ord(row1[0]) <= ord(row2[0]):
        return cheak(row1[1:], row2[1:])
    else:
        return False


def offset(row):
    if row[0] <= 'z':
        trow = offset(row[1:])
        if trow[0] == 'a' and trow[0] != row[1]:
            row = chr(ord(row[0]) + 1) + trow
        else:
            row = chr(ord(row[0])) + trow
    if row[0] > 'z':
        row = 'a' + row[1:]
    return row


def abc(str1, str2):
    temp = str1
    if len(str1) == len(str2) and str1.isalpha() and str2.isalpha():
        if cheak(str1, str2):
            i = ord(temp[-1]) + 1
            while temp != str2:
                print(temp)
                temp = temp[:-1] + chr(i)
                if temp[-1] > 'z':
                    temp = offset(temp)
                    i = ord(temp[-1]) + 1
                else:
                    i += 1
            print(temp)
    else:
        print("Строки были введены неверно")