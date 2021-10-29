# Created by Беликов Илья
# Date 26.10
# Task description: Алфавит


def changeChar(text, char, index):
    return text[:index] + char + text[index + 1: len(text)]


def convertBase(num, to_base=10, from_base=10):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if from_base == 26:
        for i in range(0, len(num)):
            charInAlphabetNum = alphabet.find(num[i])
            num = changeChar(num, alphabet[charInAlphabetNum - 10], i)
        n = int(num, from_base)
    else:
        n = int(num)
    shift = 0
    if to_base == 26:
        shift = 10
    if n < to_base:
        return alphabet[n + shift]
    else:
        return convertBase(n // to_base, to_base) + alphabet[n % to_base + shift]


def printAlphabet(startStr, endStr):
    try:
        startStr = startStr.upper()
        endStr = endStr.upper()
        if startStr > endStr:
            print("Строки должны быть одинаковой длинны и введены в алфавитном порядке")
        else:
            start = int(convertBase(startStr, 10, 26))
            end = int(convertBase(endStr, 10, 26))
            for number in range(start, end + 1):
                tail = convertBase(number, 26, 10)
                print(("A" * (len(startStr) - len(tail)) + tail).lower())
    except ValueError:
        print("ERROR!")