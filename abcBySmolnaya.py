# Created by Anastasia
# Date 20.10.2020
# Task Description: вывести полный перебор строк от первой до второй в алфавитном порядке
import math


def abc(start: str, finish: str):
    """
    Выполняет последовательный перебор строк от start до finish.

    :param start: начальное значение
    :param finish: конечное значение
    :return: выводит перебор
    """
    start26 = toSystem26(start)
    finish26 = toSystem26(finish)
    start10 = toSystem10(start26)
    finish10 = toSystem10(finish26)

    for i in range(start10, finish10 + 1):
        print(toAbc(i))


def toSystem26(string: str):
    """
    Преобразует строку к списку номеров ее букв из английского алфавит.
    Преобразование к 26-ричной системе счисления.

    :param string: str
    :return: list
    """
    alphabet = []
    for i in range(1, 27):
        alphabet.append((i, chr((i + 96))))

    num26 = []
    for elem in string:
        for alpha in alphabet:
            if elem == alpha[1]:
                num26.append(alpha[0])
    return num26


def toSystem10(num26: list):
    """
    Перевод числа (в виде списка) из 26-ричной в 10ую систему счисления.

    :param num26: список номеров букв английского алфавита
    :return: int
    """
    num10 = 0
    for i in range(len(num26)):
        num10 = num10 + num26[-1] * 26 ** i
        del num26[-1]
    return num10


def toAbc(num10: int):
    """
    Перевод из 10ой в 26-ричную систему счисления и преобразование к строке.

    :param num10: int
    :return: str
    """
    numArray = []

    i = False
    if num10 % 26 == 0:
        num10 = num10 - 1
        i = True

    while num10 > 25:
        a = math.floor(num10 / 26)
        s = num10 - a * 26
        num10 = a
        numArray.insert(0, s)
        if a < 26:
            numArray.insert(0, a)

    if i:
        numArray[-1] = numArray[-1] + 1

    alphabet = []
    for i in range(1, 27):
        alphabet.append((i, chr((i + 96))))

    newAbc = ''
    for elem in numArray:
        for alpha in alphabet:
            if elem == alpha[0]:
                newAbc = newAbc + alpha[1]
                break
    return newAbc
