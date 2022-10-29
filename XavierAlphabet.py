CODE_A = 97
CODE_Z = 122


# Function that handles ASCII overflow (in our case, if character
# is greater than 'z').
def overflow_handler(asciiList, n):
    asciiList[n - 1] = CODE_A  # If code value is greater than 'z', reset it to 'a'.
    asciiList[n - 2] += 1
    for i in reversed(range(1, n - 1)):  # Check if other code values have to be changed.
        if asciiList[i] > CODE_Z:
            asciiList[i] = CODE_A
            asciiList[i - 1] += 1
    return asciiList


# Function that converts string to a list of ASCII values for
# further calculations.
def str_to_ASCII(st, fin):
    # Using 'map' function, create lists of ASCII values out of input strings.
    return list(map(ord, list(st))), list(map(ord, list(fin)))


# Function that prints the combinations of characters until the
# target string has been produced.
def str_combinations(ascStart, ascFin, n):
    while ascStart != ascFin:
        ascStart[n - 1] += 1
        if ascStart[n - 1] > CODE_Z:
            ascStart = overflow_handler(ascStart, n)
        # Once list has been handled, use 'map' to convert ASCII values back to characters.
        print(''.join(list(map(chr, ascStart))))


# Function that handles input and combines functions defined above.
# Throws ValueError in case of bad input.
def ascii_alphabet_solution(st, fin):
    if len(st) != len(fin):
        raise ValueError('ERROR: Strings have different length.')
    elif st > fin:
        raise ValueError('ERROR: start line cannot be greater than finish.')
    asciiStart, asciiDest = str_to_ASCII(st, fin)
    strLength = len(asciiStart)
    # Print starting string, as it isn't printed in the functions above.
    print(st)

    str_combinations(asciiStart, asciiDest, strLength)
