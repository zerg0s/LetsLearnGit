# Решение
def printAlphabetByPashtet(str1, str2):
    try:
        checkStrings(str1, str2)
        answer = list(str1)
        strLen = len(str1)
        i = strLen - 1
        print(str1)
        while "".join(answer) != str2:
            if answer[i] != 'z':
                answer[i] = chr(ord(answer[i]) + 1)
                i = strLen - 1
                print("".join(answer))
            else:
                answer[i] = 'a'
                i -= 1
    except ValueError:
        print("PASHTET ERROR!")

# Проверка входных данных
def checkStrings(str1, str2):
    if len(str1) != len(str2):
        raise ValueError
    if str1 > str2:
        raise ValueError
    for chr1 in str1:
        if not 'a' <= chr1 <= 'z':
            raise ValueError
    for chr2 in str2:
        if not 'a' <= chr2 <= 'z':
            raise ValueError
