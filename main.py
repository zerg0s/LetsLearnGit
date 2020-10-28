import alphabet
import abcExample
import abcKlokov
import abcBySmolnaya
import Alphabet_Overchuk
import alphabet
import alphabetClass
import abcStartFinish
import abcDenisov
import boreikoAlphabet
import alphSapunova
import abcKremeshnaya
import alphavitByKuznetsov
import Alphabet_Morozov
import abcByRVS

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
<<<<<<< HEAD
    alphavitByKuznetsov.abc(start,finish)
    abcExample.abc(start, finish)
    abcKlokov.printIntermediateRows(start, finish)
    abcBySmolnaya.abc(start, finish)
    alphabet.abc(start, finish)
    abcExample.abc(start, finish)
    Alphabet_Overchuk.Alphabet(start, finish)
    alphabet.alphabetV2(start, finish)
    abcKremeshnaya.alphabeticalProcessing(start, finish)
    Alphabet_Morozov.printSortedStrings(start, finish)
    abcByRVS.alphabet(start, finish)

=======
>>>>>>> b6ce75c0ca6b25107846c100b233b0dce4e1aca1
    try:
        alphavitByKuznetsov.abc(start, finish)
        abcExample.abc(start, finish)
        abcKlokov.printIntermediateRows(start, finish)
        abcBySmolnaya.abc(start, finish)
        alphabet.abc(start, finish)
        abcExample.abc(start, finish)
        Alphabet_Overchuk.Alphabet(start, finish)
        alphabet.alphabetV2(start, finish)
        abcDenisov.alphabet(start, finish)
        boreikoAlphabet.alphabetIterating(start, finish)
        alphSapunova.alphIterate(start, finish)
        abcKremeshnaya.alphabeticalProcessing(start, finish)
        Alphabet_Morozov.printSortedStrings(start, finish)
        alphabetClass.Alphabet('abcdefghijklmnopqrstuvwxyz').print_range(start, finish)
        abcStartFinish.abcv4(start, finish)
    except ValueError as errors:
        print(errors)
        exit(1)
    except KeyError:
        print('Input string have unknown symbol')
        exit(2)
