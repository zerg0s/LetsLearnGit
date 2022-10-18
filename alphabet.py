def printIterationOverStringsAlphabetically(start, finish):
    if len(start) != len(finish):
        raise ValueError('Incorrect data')

    if start > finish:
        return

    print(start)
    while True:
        for i in range(len(finish)):
            if start[-i - 1] != 'z':
                start = start[:-i - 1] + chr(ord(start[-i - 1]) + 1) + 'a' * i
                break
        print(start)
        if start == finish:
            break
