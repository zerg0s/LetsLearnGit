import alphabet
import abcExample
import abcKlokov
import abcBySmolnaya
import Alphabet_Overchuk
import alphabet
import alphabetClass
import abcStartFinish
import alphSapunova
import abcKremeshnaya
import alphavitByKuznetsov
import Alphabet_Morozov

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    alphavitByKuznetsov.abc(start,finish)
    abcExample.abc(start, finish)
    abcKlokov.printIntermediateRows(start, finish)
    abcBySmolnaya.abc(start, finish)
    alphabet.abc(start, finish)
    abcExample.abc(start, finish)
    Alphabet_Overchuk.Alphabet(start, finish)
    alphabet.alphabetV2(start, finish)
    alphSapunova.alphIterate(start, finish)
    abcKremeshnaya.alphabeticalProcessing(start, finish)
    Alphabet_Morozov.printSortedStrings(start, finish)

    try:
        alphabetClass.Alphabet('abcdefghijklmnopqrstuvwxyz').print_range(start, finish)
        abcStartFinish.abcv4(start, finish)
    except ValueError as errors:
        print(errors)
        exit(1)
    except KeyError:
        print('Input string have unknown symbol')
        exit(2)
