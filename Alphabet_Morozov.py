def printSortedStrings(fStr, sStr, resultStr = "", flag = True):
    if flag:
        if (len(fStr) == 0):
            print(resultStr)
            if (resultStr == sStr):
                flag = False
                return flag
            return flag
        for char in range(ord(fStr[0]), 123):
            resultStr += chr(char)
            flag = printSortedStrings(fStr[1:], sStr, resultStr, flag)
            resultStr = resultStr[:len(resultStr) - 1]
    return flag