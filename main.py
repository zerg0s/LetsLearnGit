from alphabet_bondarenkoi07 import PrintAlphabetNumbers
from Alfavit import printIterationOverStringsAlphabetically
from alphabetDocNemo import printAlphabetSequence
from alphabet_t import strings_wrapper
from gachiResolution import print_string_interval
from alfavit_e import gen_generation
from alphabet import print_alphabet_values
from alphabetByRoman import dummyAlphabet
from alphabet_pashtet import printAlphabetByPashtet
from XavierAlphabet import ascii_alphabet_solution
from abc_SokolovaKV import generalFunc
import basil_antonov as an21
from AlphabetBySil import printAlphabet
from alphabet_dimanchella import print_iterating_strs
from AlphabetXXMargoRitaXX import alphabet_printing

if __name__ == "__main__":
    print("Alphabet task has started :)")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aba

    print("First solution")

    printIterationOverStringsAlphabetically(start, finish)


    print("Third solution")
    print_alphabet_values(start, finish)

    print("Tim solution")
    strings_wrapper(start, finish)

    print("Maxim solution")
    gen_generation(start, finish)

    print("Roman's solution")
    dummyAlphabet(start, finish)

    print("AlphabetBySil's solution")
    printAlphabet(start, finish)

    print("Pashtet's solution")
    printAlphabetByPashtet(start, finish)

    print("DocNemo's solution")
    printAlphabetSequence(start, finish)

    print("SokolovaKv's solution")
    generalFunc(start, finish)
    

    try:
        print("Basil Antonov solution")
        ascii_alphabet_solution(start, finish)
        an21.printIterationOverStringsAlphabetically(start, finish)
        print("bondarenkoi07 solution")
        PrintAlphabetNumbers(start, finish)
        print("XXMargoRitaXX's solution")
        alphabet_printing(start, finish)
        print("Gachi solution")
        print_string_interval(start, finish)
     except ValueError as ex:
        print(ex)

    print("Dimanchella's solution")
    print_iterating_strs(start, finish)
    
