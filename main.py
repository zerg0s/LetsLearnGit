import Alphabet
from alphabet_task import printIterationOverStringsAlphabetically

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    Alphabet.printAlphabet(start, finish)
    printIterationOverStringsAlphabetically(start, finish)
