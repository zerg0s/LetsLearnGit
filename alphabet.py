# Алфавит

import sys


def create_next_string(string):
    if ' ' in string:
        string = string.split(' ')
    else:
        string = list(string)

    for i in range(len(string) - 1, -1, -1):
        while string[i] == 'z':
            string[i] = 'a'
            i -= 1

        string[i] = chr(ord(string[i]) + 1)
        break

    return ''.join(map(str, string))



