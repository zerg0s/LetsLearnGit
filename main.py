# Серёгин Сергей ( группа: М3О-121М-20 )
# 29.09.2020
# Перебор строк в алфавитном порядке

import alphabetClass

# Точка входа в программу
if __name__ == '__main__':
    try:
        alphabetClass.Alphabet('abcdefghijklmnopqrstuvwxyz').print_range(input(), input())
    except ValueError as errors:
        print(errors)
        exit(1)
    except KeyError:
        print('Input string have unknown symbol')
        exit(2)
