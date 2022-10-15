def checkOverflow(string):
    for i in range(0, len(string) - 1):
        if (ord(string[len(string) - 1 - i]) == ord('z') + 1):
            string = string[0:len(string) - 2 - i] + chr(
                ord(string[len(string) - 2 - i]) + 1) + 'a' + string[len(string) - i:]
    return string


def printStrings(start, end):
    temp = start
    print(temp)
    while (temp < end):
        temp = checkOverflow(temp[0:len(temp) - 1] + chr(ord(temp[len(temp) - 1]) + 1))
        print(temp)


def printIterationOverStringsAlphabetically(firstString, secondString):
    if (len(firstString) == len(secondString)):
        if (firstString == secondString):
            print(firstString)
        elif (firstString < secondString):
            printStrings(firstString, secondString)
        else:
            printStrings(secondString, firstString)
