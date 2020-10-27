def shift(changingStr, iteration, firstNotCorrectSymbol):
    if changingStr[iteration] == 'z' and iteration == len(changingStr) - 1:
        changingStr = changingStr[:iteration - 1] + chr(ord(changingStr[iteration - 1]) + 1) \
                      + 'a' + changingStr[iteration + 1:]
        if changingStr[iteration - 1] <= 'z':
            print(changingStr)
        if iteration - 1 >= firstNotCorrectSymbol and changingStr[iteration - 1] > 'z':
            changingStr = shift(changingStr, iteration - 1, firstNotCorrectSymbol)
    elif changingStr[iteration] > 'z':
        changingStr = changingStr[:iteration - 1] + chr(ord(changingStr[iteration - 1]) + 1) \
                      + 'a' + changingStr[iteration + 1:]
        print(changingStr)

    return changingStr


def printIntermediateRows(str1, str2):
    tempStr = str1
    firstNotCorrect = len(str2) - 1
    print(str1)

    while tempStr != str2:
        for i in range(len(str2)):
            if str2[i] != tempStr[i]:
                firstNotCorrect = i
                break

        if firstNotCorrect < len(str1) - 1:
            for i in range(ord(tempStr[-1]) + 1, ord('z') + 1):
                tempStr = tempStr[:-1] + chr(i)
                print(tempStr)
        else:
            for i in range(ord(tempStr[-1]) + 1, ord(str2[-1]) + 1):
                tempStr = tempStr[:-1] + chr(i)
                print(tempStr)

        tempStr = shift(tempStr, len(tempStr) - 1, firstNotCorrect)