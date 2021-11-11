# Created by Diana Shabatokova
# Date 29.10.21
# Task 6 (Алфавит)

from itertools import product as prod

accepted = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}


def checkAssepted(start, finish):
    try:
        if not accepted.issuperset(start) and accepted.issuperset(finish):
            raise ValueError
        if len(start) != len(finish):
            raise ValueError
    except ValueError:
        print('Ошибка ввода')
        quit()
    orderStrings(start, finish)


def orderStrings(start, finish):
    for i in prod(accepted, repeat=len(start)):
        string = ' '.join(i)
        if start <= string and string <= finish:
            print(string)