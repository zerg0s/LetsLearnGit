# Created by Ilya Nepsha
#
# Task Name: Алфавит

def alphabet(str1, str2):
    arrCh1 = list(map(ord, str1))
    arrCh2 = list(map(ord, str2))
    i = len(str1) - 1
    print(''.join(map(chr, arrCh1)))
    while (i != -1):
        if arrCh1[i - 1] != arrCh2[i - 1]:
            while (arrCh1[i] != 122):
                arrCh1[i] += 1
                print(''.join(map(chr, arrCh1)))
            print(''.join(map(chr, arrCh1)))
            arrCh1[i] += 97
            arrCh1[i - 1] += 1
        else:
            i -=1
        print(''.join(map(chr, arrCh1)))
    return 1

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    alphabet(start, finish)