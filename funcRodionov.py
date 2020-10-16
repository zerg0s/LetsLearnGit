def getArrWords(x, y):
    lenOffFstString, lenOffSecString = len(x), len(y)
    resultStringFst, resultStringSec = [0] * lenOffFstString, [0] * lenOffSecString
    for i in range(0, len(x)):
        resultStringFst[i] = ord(x[i])
    for j in range(0, len(y)):
        resultStringSec[j] = ord(y[j])
    countWords(resultStringFst, 0, resultStringSec, lenOffSecString)
    # for i in range(0, 26):
    #     for j in range(0, 26):
    #         while resultStringFst[2] != 123:
    #             print(chr(resultStringFst[0]) + chr(resultStringFst[1]) + chr(resultStringFst[2]))
    #             if resultStringFst[0] == resultStringSec[0] and resultStringFst[1] == resultStringSec[1] and resultStringFst[2] == resultStringSec[2]:
    #                 return False
    #             elif resultStringFst[2] == 123:
    #                 resultStringFst[2] = 97
    #                 break
    #             resultStringFst[2] += 1
    #         resultStringFst[1] += 1
    #     resultStringFst[0] += 1

def countWords(arrX, pos, finalArr, length) -> bool:
    while arrX[pos] != 123:
        if pos != length - 1:
            pos += 1
            countWords(arrX, pos, finalArr, length)
        elif pos == length - 1:
            for ij in range(0, pos + 1):
                print(chr(arrX[ij]), end='')
            print()
        if (arrX[length - 1] == finalArr[pos]) and pos <= 122:
            arrX[pos] = 97
            return False
        arrX[pos] += 1
    return True
