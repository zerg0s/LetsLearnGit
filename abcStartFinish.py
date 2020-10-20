import string


def abc(start, last):
    alph = string.ascii_lowercase
    dic = {alph[i]: i + 1 for i in range(len(alph))}
    code1 = 0
    code2 = 0
    curr = 1
    listSize = len(start) - 1
    while listSize != -1:
        code1 = code1 + dic[start[listSize]] * curr
        code2 = code2 + dic[last[listSize]] * curr
        curr = curr * len(alph)
        listSize = listSize - 1

    letters = list(dic.keys())
    res = ''
    for i in range(code1 + 1, code2):
        while i != 0:
            temp = i % len(alph) - 1
            res = '{}{}'.format(letters[temp], res)
            i = i // len(alph)
            if temp == -1:
                i = i - 1
        print(res)
        res = ''
