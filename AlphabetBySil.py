def printAlphabet(line1, line2):
    try:
        checkStrings(line1, line2)
        word = list(line1)
        strValue = len(line1)
        i = strValue - 1
        print(line1)
        while "".join(word) != line2:
            if word[i] != 'z':
                word[i] = chr(ord(word[i]) + 1)
                i = strValue - 1
                print("".join(word))
            else:
                word[i] = 'a'
                i -= 1
    except ValueError:
        print("Error!")


def cheks(line1, line2):
    if len(line1) != len(line2):
        print("Error!")
    if line1 > line2:
        print("Error!")
    for x in line1:
        if not 'a' <= x <= 'z':
            print("Error!")
    for y in line2:
        if not 'a' <= y <= 'z':
            print("Error!")
