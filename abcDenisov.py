def alphabet(startString, endString):
    startStringList = []
    endStringList = []

    for i in range(len(startString)):
        startStringList.append(ord(startString[i]))
        endStringList.append(ord(endString[i]))

    while startStringList != endStringList:
        while startStringList[-1] <= ord('z'):
            midString = ''
            zCounter = 0
            for i in range(len(startString)):
                midString += chr(startStringList[i])
            print(midString)
            if startStringList == endStringList:
                break
            if startStringList[-1] == ord('z'):
                for i in reversed(range(len(startString))):
                    if startStringList[i] == ord('z'):
                        zCounter += 1
                        startStringList.pop(i)
                    else:
                        break
                startStringList[-1] += 1
                for i in range(zCounter):
                    startStringList.append(ord('a'))
                if startStringList[-1] == ord('a'):
                    startStringList[-1] -= 1
            startStringList[-1] += 1