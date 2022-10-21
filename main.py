from Alfavit import printIterationOverStringsAlphabetically
from gachiResolution import print_string_interval
from alphabet import print_alphabet_values
from alfavit_e import gen_generation

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

    print("Maxim solution")
    gen_generation(start, finish)
