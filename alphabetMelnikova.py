def abc(a, b):
    if len(a) != len(b):
        exit(1)

    alist = list(a)
    blist = list(b)

    print(a)
    while 1:
        m = len(alist) - 1
        if alist == blist:
            break
        if ord(alist[m]) < 122:
            alist[m] = chr(ord(alist[m]) + 1)
            result = str()
            for z in alist:
                result += str(z)
            print(result)
        elif ord(alist[m]) == 122:
            while 1:
                if m >= 0:
                    if ord(alist[m]) < 122:
                        alist[m] = chr(ord(alist[m]) + 1)
                        m += 1
                        break
                    else:
                        m -= 1
            while m < len(alist):
                alist[m] = chr(97)
                m += 1
            result = str()
            for z in alist:
                result += str(z)
            print(result)