import abcStartFinish
import abcExample
import Alphabet_Overchuk
import alphabet

if __name__ == '__main__':
    start = str(input())
    finish = str(input())
    try:
    abcStartFinish.abcv4(start, finish)
    abcExample.abc(start, finish)
    Alphabet_Overchuk.Alphabet(start, finish)
    alphabet.alphabetV2(start, finish)
    except KeyError:
        print("Для перебора вводятся только буквы")
        
