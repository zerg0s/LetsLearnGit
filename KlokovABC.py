def shift(defStr, iteration, fnc):
    if defStr[iteration] == 'z' and iteration == len(defStr) - 1:
        defStr = defStr[:iteration - 1] + chr(ord(defStr[iteration - 1]) + 1) + 'a' \
                 + defStr[iteration + 1:]
        if defStr[iteration - 1] <= 'z':
            print(defStr)
        if iteration - 1 >= fnc and defStr[iteration - 1] > 'z':
            defStr = shift(defStr, iteration - 1, fnc)
    elif defStr[iteration] > 'z':
        defStr = defStr[:iteration - 1] + chr(ord(defStr[iteration - 1]) + 1) + 'a' + \
                 defStr[iteration + 1:]
        print(defStr)

    return defStr


def abc(str1, str2):
    tempStr = str1
    firstNotCorrect = len(str2) - 1
    print(str1)

    while tempStr != str2:
        j = 1

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