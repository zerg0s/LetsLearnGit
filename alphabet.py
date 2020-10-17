# Task 889100. Andrey Zhirov.


def abc(start, finish):
    SHIFT = -97

    def incr(num):
        # num + 1
        if num[-1] + 1 > 25:
            num[-1] = 0
            num[-2] += 1
            for i in range(len(num) - 2, 0, -1):
                if num[i] > 25:
                    num[i] = 0
                    num[i - 1] += 1
                else:
                    break
        else:
            num[-1] += 1

    def diff(numA, numB):
        # NumA - NumB
        for i in range(len(numA) - 1, -1, -1):
            if numA[i] - numB[i] < 0:
                numA[i] = numA[i] - numB[i] + 26
                numA[i - 1] -= 1
            else:
                numA[i] -= numB[i]
        return numA

    def from26to10base(num):
        res = 0
        for i in range(0, len(num)):
            res += (26 ** i) * num[len(num) - i - 1]
        return res

    def isOver(numA, numB):
        '''NumA > NumB?'''
        for i in range(0, len(numA)):
            if numA[i] > numB[i]:
                return True
            elif numA[i] == numB[i]:
                continue
            else:
                return False
        return False

    if len(start) != len(finish) or len(start) == 0 or len(finish) == 0:
        print('Input Error.')
        exit(1)

    # a = 97
    # z = 122
    numA = [ord(e)+SHIFT for e in start]
    numB = [ord(e)+SHIFT for e in finish]
    
    if isOver(numA, numB):
        print('Input Error.')
        exit(1)

    dif = from26to10base(diff(numB, numA))
    for i in range(0, dif+1):
        print(''.join(map(lambda x: chr(x-SHIFT), numA)))
        incr(numA)
