import Alphabet
from alphabet_task import printIterationOverStringsAlphabetically
from ae_belousov_alphabet import print_char_combinations
import AlphabetGit
import abcByDanilov

if __name__ == "__main__":
    print("Alphabet task has started :)")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aba

    print("First solution")
    printIterationOverStringsAlphabetically(start, finish)

    print("Second Solution")
    AlphabetGit.printAlphabet(start, finish)

    print("3rd Solution")
    print_char_combinations(start, finish)

    print("4th Solution")
    Alphabet.printAlphabet(start, finish)

    print("5th Solution")
    abcByDanilov.alp_start(start, finish)
