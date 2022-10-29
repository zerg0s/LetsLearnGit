TWENTY_FIVE = ord('z')
ZERO = ord('a')
BASE = TWENTY_FIVE - ZERO + 1


class AlphabetNumber:
    @staticmethod
    def ToAlphabet(number: int, power: int) -> str:
        alph_number = ""
        while number > 0:
            alph_number = chr(ZERO + number % BASE) + alph_number
            number //= BASE

        if len(alph_number) < power:
            for _ in range(0, power - len(alph_number)):
                alph_number = chr(ZERO) + alph_number

        return alph_number

    @staticmethod
    def ToDec(alph_number: str) -> int:
        order = 0
        number = 0
        for rune in reversed(alph_number):
            number += (ord(rune) - ZERO) * BASE ** order
            order += 1

        return number


def PrintAlphabetNumbers(start_str: str, finish_str: str):
    start_dec = AlphabetNumber.ToDec(start_str)
    finish_dec = AlphabetNumber.ToDec(finish_str)

    if start_dec > finish_dec:
        start_dec, finish_dec = finish_dec, start_dec

    for i in range(start_dec, finish_dec + 1):
        print(AlphabetNumber.ToAlphabet(i, len(start_str)))


if __name__ == "__main__":
    start = input()
    finish = input()

    PrintAlphabetNumbers(start, finish)
