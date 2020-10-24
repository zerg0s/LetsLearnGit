import alphabet
import abcExample
import KlokovABC
import abcBySmolnaya
import Alphabet_Overchuk
import alphabet
import alphabetClass
import abcStartFinish

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    abcExample.abc(start, finish)
    KlokovABC.abc(start, finish)
    abcBySmolnaya.abc(start, finish)
    alphabet.abc(start, finish)
    abcExample.abc(start, finish)
    Alphabet_Overchuk.Alphabet(start, finish)
    alphabet.alphabetV2(start, finish)
    try:
        alphabetClass.Alphabet('abcdefghijklmnopqrstuvwxyz').print_range(start, finish)
        abcStartFinish.abcv4(start, finish)
    except ValueError as errors:
        print(errors)
        exit(1)
    except KeyError:
        print('Input string have unknown symbol')
        exit(2)
