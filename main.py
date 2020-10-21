import abcExample
import Alphabet_Overchuk
import alphabet
import alphabetClass
import abcStartFinish

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    try:
        abcStartFinish.abcv4(start, finish)
    except KeyError:
        print("Ошибка ввода")
        exit(1)
    abcExample.abc(start, finish)
    Alphabet_Overchuk.Alphabet(start, finish)
    alphabet.alphabetV2(start, finish)
    try:
        alphabetClass.Alphabet('abcdefghijklmnopqrstuvwxyz').print_range(start, finish)
    except ValueError as errors:
        print(errors)
        exit(1)
    except KeyError:
        print('Input string have unknown symbol')
        exit(2)
        
