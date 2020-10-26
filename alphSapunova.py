# Алфавит
# Сапунова Е.С. М3О-109М-20

def firstMoreLast(str1, str2):
    if len(str1) == 0:
        return True
    elif ord(str1[0]) <= ord(str2[0]):
        return firstMoreLast(str1[1:], str2[1:])
    else:
        return False

def iterateLetByLet(s1, s2):
    if s1 == s2:
        print(''.join(list(map(chr, s1))))
        return 1

    elif s1[len(s1)-1] != 122:
        while s1[len(s1)-1] != 122:
            print(''.join(list(map(chr, s1))))
            if s1 != s2:
                s1[len(s1) - 1] += 1
            else:
                return 1
        iterateLetByLet(s1, s2)

    elif s1.index(122) != -1:
        try:
            print(''.join(list(map(chr, s1))))
            idZ = s1.index(122)
            s1[idZ-1] += 1
            i = idZ
            while i < len(s1):
                s1[i] = 97
                i+=1
            iterateLetByLet(s1, s2)
        except ValueError:
            print(''.join(list(map(chr, s1))))
            iterateLetByLet(s1, s2)

def alphIterate(string1, string2):
    if len(string1) == len(string2):
        if string1.isalpha() and string2.isalpha():
            if firstMoreLast(string1, string2):
                str1List = list(map(ord, string1))
                str2List = list(map(ord, string2))
                iterateLetByLet(str1List, str2List)
            else:
                print("Необходимо ввести строки: первая -", \
                "начало перебора, вторая - конец.", sep='\t', end='\n')
        else:
            print("Строки должны состоять только из букв.")
    else:
        print("Строки должны быть одной длины.")