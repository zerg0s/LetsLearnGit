# Серёгин Сергей ( группа: М3О-121М-20 )
# 29.09.2020
# Перебор строк в алфавитном порядке

import alphabetClass

# Точка входа в программу
if __name__ == '__main__':
    try:
        first_str: str = input()
        second_str: str = input()
        if len(first_str) != len(second_str):
           raise ValueError('Str lenghts not equals') 
        alphabetClass.Alphabet('abcdefghijklmnopqrstuvwxyz').print_range(first_str, second_str)
    except ValueError as errors:
        print(errors)
        exit(1)
    except KeyError:
        print('Input string have unknown symbol')
        exit(2)
