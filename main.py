import abcExample
import Alphabet_Overchuk
import alphabet

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    abcExample.abc(start, finish)
    Alphabet_Overchuk.Alphabet(start, finish)
    alphabet.alphabetV2(start, finish)
