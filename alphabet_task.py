def changeNextSymbol(index, tempStr):
    currentSymbol = ord(tempStr[index]) + 1
    if currentSymbol > ord('z'):
        tempStr = tempStr[0:len(tempStr) + index] + \
                  'a' + \
                  tempStr[len(tempStr) + index + 1:]
        tempStr = changeNextSymbol(index - 1, tempStr)
        return tempStr
    else:
        tempStr = tempStr[0:len(tempStr) + index] + \
                  chr(currentSymbol) + tempStr[len(tempStr) + index + 1:]
        return str(tempStr)


def printIterationOverStringsAlphabetically(startStr: str, finishStr: str):
    while startStr != finishStr:
        for i in range(ord(startStr[-1]) + 1, ord('z') + 2):
            print(startStr)
            startStr = startStr[:len(startStr) - 1] + chr(i)
            if ord(startStr[-1]) > ord('z'):
                startStr = changeNextSymbol(-1, startStr)
                startStr = startStr[:-1] + 'a'
            if startStr == finishStr:
                print(startStr)
                break
