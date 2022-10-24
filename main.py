from Alfavit import printIterationOverStringsAlphabetically
from alphabet_t import strings_wrapper
from gachiResolution import print_string_interval
from alfavit_e import gen_generation
from alphabet import print_alphabet_values
from alphabetByRoman import dummyAlphabet
from XavierAlphabet import ascii_alphabet_solution

if __name__ == "__main__":
    print("Alphabet task has started :)")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aba

    print("First solution")
    printIterationOverStringsAlphabetically(start, finish)

    print("Gachi solution")
    try:
        print_string_interval(start, finish)
    except ValueError as ex:
        print(ex)

    print("Third solution")
    print_alphabet_values(start, finish)

    print("Tim solution")
    strings_wrapper(start, finish)

    print("Maxim solution")
    gen_generation(start, finish)
    
    print("Roman's solution")
    dummyAlphabet(start, finish)

    print("Denis' solution")
    try:
        ascii_alphabet_solution(start, finish)
    except ValueError as ex:
        print(ex)
