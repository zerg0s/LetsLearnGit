# Алфавит
# Сапунова Е.С. М3О-109М-20

def firstMoreLast(firstStr, lastStr):
    if len(firstStr) == 0:
        return True
    elif ord(firstStr[0]) <= ord(lastStr[0]):
        return firstMoreLast(firstStr[1:], lastStr[1:])
    else:
        return False

def iterateLetByLet(startString, endString):
    if startString == endString:
        print(''.join(list(map(chr, startString))))
        return 1

    elif startString[len(startString)-1] != ord('z'):
        while startString[len(startString)-1] != ord('z'):
            print(''.join(list(map(chr, startString))))
            if sstartString != endString:
                sstartString[len(startString) - 1] += 1
            else:
                return 1
        iterateLetByLet(startString, endString)

    elif startString.index(ord('z')) != -1:
        try:
            print(''.join(list(map(chr, startString))))
            identZ = startString.index(ord('z'))
            startString[identZ-1] += 1
            i = identZ
            while i < len(startString):
                startString[i] = ord('a')
                i += 1
            iterateLetByLet(startString, endString)
        except ValueError:
            print(''.join(list(map(chr, startString))))
            iterateLetByLet(startString, endString)

def alphIterate(firstString, lastString):
    if len(firstString) == len(lastString):
        if firstString.isalpha() and lastString.isalpha():
            if firstMoreLast(firstString, lastString):
                firstStrList = list(map(ord, firstString))
                lastStrList = list(map(ord, lastString))
                iterateLetByLet(firstStrList, lastStrList)
            else:
                print("Необходимо ввести строки: первая -", \
                "начало перебора, вторая - конец.", sep='\t', end='\n')
        else:
            print("Строки должны состоять только из букв.")
    else:
        print("Строки должны быть одной длины.")