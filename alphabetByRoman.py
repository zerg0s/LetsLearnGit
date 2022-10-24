# Function builds an output string, transforming symbols from UTF-8 code back to char
def printChar(numbers):
    output = ""
    for number in numbers:
        output = output + chr(number)
    print(output) # Output string

# recursive function, checks if UTF-8 digit overflowed, if true returns it back to 97 ('a'),
# then adds +1 to the left digit. Function exits when reached the leftest digit.
def checkOverflow(currentList, i):
    if i == 0:
        return currentList
    if currentList[i] == 123:
        currentList[i] = 97
        currentList[i-1] += 1
        return checkOverflow(currentList, i - 1)


def dummyAlphabet(str1, str2):
    if len(str1) != len(str2):  # Check if lengths match
        return print("Error: Lengths of strings don't match")
    startStr1 = []
    finishStr2 = []
    length = len(str1)
    for ch in str1:
        if ord(ch) > 122 or ord(ch) < 97:  # Check if input strings contain only "a-z"
            return print("Error: Invalid input")
        else:
            startStr1.append(ord(ch))  # Makes new list containing chars in UTF-8 code
    for ch in str2:
        if ord(ch) > 122 or ord(ch) < 97:  # Check if input strings contain only "a-z"
            return print("Error: Invalid input")
        else:
            finishStr2.append(ord(ch))  # Makes new list containing chars in UTF-8 code
    if finishStr2 < startStr1:
        print("Finish is less than start. Rearranging start and finish strings")

        startStr1, finishStr2 = finishStr2, startStr1
    if startStr1 == finishStr2:  # if start string == finish string, return
        return printChar(startStr1)

    while True:
        printChar(startStr1)
        startStr1[length - 1] += 1  # add +1 to the last digit
        checkOverflow(startStr1, length - 1)
        if startStr1 == finishStr2:  # if start string reached finish, return last string
            return printChar(startStr1)


if __name__ == '__main__':
    dummyAlphabet()