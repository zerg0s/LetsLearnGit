def slip(str3):
    for i in range(len(str3) - 1, 0, -1):
        if str3[i] > 'z':
            str3 = str3[:i - 1] + chr(ord(str3[i - 1]) + 1) + 'a' + str3[i + 1:]
    return str3


def abc(str1, str2):
    while str1 != str2:
        print(str1)
        str1 = str1[:-1] + chr(ord(str1[-1]) + 1)
        if str1[-1] > 'z':
            str1 = slip(str1)

    print(str1)