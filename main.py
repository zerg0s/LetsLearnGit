from Alfavit import printIterationOverStringsAlphabetically
from gachiResolution import print_string_interval

if __name__ == "__main__":
    print("Alphabet task has started :)")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aba

    print("First solution")
    printIterationOverStringsAlphabetically(start, finish)

    print("Gachi solution")
    try:
        print_string_interval(start, finish)
    except RuntimeError as ex:
        print(ex)
