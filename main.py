import Alphabet
from alphabet_task import printIterationOverStringsAlphabetically
import AlphabetGit

if __name__ == "__main__":
    print("Alphabet task has started :)")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    Alphabet.printAlphabet(start, finish)
    print("First solution")
    printIterationOverStringsAlphabetically(start, finish)
    print("Second Solution")
    AlphabetGit.printAlphabet(startStr, finishStr)
