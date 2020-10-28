#891345: Nikita Overchuk
import string;

class Alphabet:
    def __init__(self, start: str, end: str):
        alphabet = string.ascii_lowercase
        self.__length: int = len(alphabet)
        self.__alphabet_codes: dict = {alphabet[i]: i + 1 for i in range(self.__length)}
        self.execute(start, end)

    def __alphabet_code(self, input_str: str) -> int:
        code: int = 0
        curr_pow: int = 1
        i: int = len(input_str) - 1

        if i == -1:
            raise ValueError('Пустая строка')

        while i != -1:
            code += self.__alphabet_codes[input_str[i]] * curr_pow
            curr_pow *= self.__length
            i -= 1

        return code

    def execute(self, start: str, end: str):
        if len(start) != len(end):
            raise ValueError('Строки должны быть одинаковой длины')
            return

        print(start)

        letters: list = list(self.__alphabet_codes.keys())
        num: int = 0
        res: str = ''
        temp: int = 0

        for i in range(self.__alphabet_code(start) + 1, self.__alphabet_code(end)):
            num: int = i
            while num != 0:
                temp = num % self.__length - 1
                res = f'{letters[temp]}{res}'
                num //= self.__length
                if temp == -1:
                    num -= 1
            print(res)
            res: str = ''
        print(end)