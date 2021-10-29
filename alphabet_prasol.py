def firstMoreLast(firstStr, lastStr):
    if len(firstStr) == 0:
        return True
    elif ord(firstStr[0]) <= ord(lastStr[0]):
        return firstMoreLast(firstStr[1:], lastStr[1:])
    else:
        return False


def iterateLetByLet(startString, endString):
    if startString == endString:
        print("".join(list(map(chr, startString))))
        return 1

    elif startString[len(startString) - 1] != ord("z"):
        while startString[len(startString) - 1] != ord("z"):
            print("".join(list(map(chr, startString))))
            if startString != endString:
                startString[len(startString) - 1] += 1
            else:
                return 1
        iterateLetByLet(startString, endString)

    elif startString.index(ord("z")) != -1:
        try:
            print("".join(list(map(chr, startString))))
            identifyZ = startString.index(ord("z"))
            startString[identifyZ - 1] += 1
            i = identifyZ
            while i < len(startString):
                startString[i] = ord("a")
                i += 1
            iterateLetByLet(startString, endString)
        except ValueError:
            print("".join(list(map(chr, startString))))
            iterateLetByLet(startString, endString)


def alphabetIterate(firstString, lastString):
    if len(firstString) == len(lastString):
        if firstString.isalpha() and lastString.isalpha():
            if firstMoreLast(firstString, lastString):
                firstStrList = list(map(ord, firstString))
                lastStrList = list(map(ord, lastString))
                iterateLetByLet(firstStrList, lastStrList)
            else:
                print("Необходимо ввести строки: первая -",
                      "начало перебора, вторая - конец.", sep='\t', end='\n')