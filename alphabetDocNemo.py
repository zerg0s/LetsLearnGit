# Урубков Владислав
# Алфавит


def raiseChar(string, index_char):
    if string[index_char] == 'z':
        string = string[:index_char] + 'a' + string[index_char + 1:]
        return raiseChar(string, index_char - 1)
    else:
        char = chr(ord(string[index_char]) + 1)
        return string[:index_char] + char + string[index_char + 1:]


def printAlphabetSequence(str_start, str_finish):
    if len(str_start) != len(str_finish) or str_start > str_finish:
        print("ERROR!")

    str_list = [str_start]
    while str_list[-1] != str_finish:
        str_list += [raiseChar(str_list[-1], len(str_list[-1]) - 1)]

    for st in str_list:
        print(st)
