# Класс для работы с алфавитом
class Alphabet:

    def __init__(self, alphabet: str):
        self.__alphabet_len: int = len(alphabet)
        self.__alphabet_codes: dict = {alphabet[i]: i + 1 for i in range(self.__alphabet_len)}

    def __alphabet_code(self, input_str: str) -> int:
        code: int = 0
        current_pow_mult: int = 1
        i: int = len(input_str) - 1
        if i == -1:
            raise ValueError('Empty string')
        while i != -1:
            code += self.__alphabet_codes[input_str[i]] * current_pow_mult
            current_pow_mult *= self.__alphabet_len
            i -= 1
        return code

    def print_range(self, start_str: str, last_str: str):
        print(start_str)
        letters: list = list(self.__alphabet_codes.keys())
        num: int = 0
        res: str = ''
        temp: int = 0
        for i in range(self.__alphabet_code(start_str) + 1, self.__alphabet_code(last_str)):
            num: int = i
            while num != 0:
                temp = num % self.__alphabet_len - 1
                res = f'{letters[temp]}{res}'
                num //= self.__alphabet_len
                if temp == -1:
                    num -= 1
            print(res)
            res: str = ''
        print(last_str)
