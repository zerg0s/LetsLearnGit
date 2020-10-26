# Created by Morozov Pavel
# Date 26.09.2020
# Task Description: Вводятся 2 строки : например, “aaa” и “abd” одинаковой длины.
# Нужно вывести полный перебор строк от первой до второй в алфавитном порядке.

def printSortedStrings(fStr, sStr, resultStr = "", flag = True):
    if flag:
        if (len(fStr) == 0):
            print(resultStr)
            if (resultStr == sStr):
                flag = False
                return flag
            return flag
        for char in range(ord(fStr[0]), 123):
            resultStr += chr(char)
            flag = printSortedStrings(fStr[1:], sStr, resultStr, flag)
            resultStr = resultStr[:len(resultStr) - 1]
    return flag