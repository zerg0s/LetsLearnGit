import sys


def strings_wrapper(s1, s2):
    if len(s1) != len(s2):
        sys.exit(1)
    else:
        print(s1)
        while s1 != s2:
            s1 = create_next_string(s1)
            print(s1)


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
