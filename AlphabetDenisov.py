def abcdef(StartString, EndString):
    StartStringList = []
    EndStringList = []

    for i in range(len(StartString)):
        StartStringList.append(ord(StartString[i]))
        EndStringList.append(ord(EndString[i]))

    while StartStringList != EndStringList:
        while StartStringList[-1] <= 122:
            MidString = ''
            ZCounter = 0
            for i in range(len(StartString)):
                MidString += chr(StartStringList[i])
            print(MidString)
            if StartStringList == EndStringList:
                break
            if StartStringList[-1] == 122:
                for i in reversed(range(len(StartString))):
                    if StartStringList[i] == 122:
                        ZCounter += 1
                        StartStringList.pop(i)
                    else:
                        break
                StartStringList[-1] += 1
                for i in range(ZCounter):
                    StartStringList.append(97)
                if StartStringList[-1] == 97:
                    StartStringList[-1] -= 1
            StartStringList[-1] += 1