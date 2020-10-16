def getArrWords(x, y):
    lenOffFstString, lenOffSecString = len(x), len(y)
    resultStringFst, resultStringSec = [0] * lenOffFstString, [0] * lenOffSecString
    for i in range(0, len(x)):
        resultStringFst[i] = ord(x[i])
    for j in range(0, len(y)):
        resultStringSec[j] = ord(y[j])
    for fst in range(0, 26):
        tempA = resultStringFst[fst]
        for sec in range(0, 26):
            tempB = resultStringFst[sec]
            for thr in range(0, 26):
                resultStringFst[thr] += 1
                tempC = resultStringFst[thr]
                print(chr(tempA) + chr(tempB) + chr(tempC))
            resultStringFst[sec] += 1
        resultStringFst[fst] += 1
    return 0