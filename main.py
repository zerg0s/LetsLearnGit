import Alphabet
from alphabet_task import printIterationOverStringsAlphabetically
from ae_belousov_alphabet import print_char_combinations
import AlphabetGit
import abcByDanilov
import alphabet_Bochkareva
import TaskChizh
import another_alphabet


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

    print("6th Solution")
    alphabet_Bochkareva.abc(start, finish)

    print("7th Solution")
    TaskChizh.IterateStrings(start, finish)

    print("another one solution")
    another_alphabet.print_strings_lexicographically(start, finish)
