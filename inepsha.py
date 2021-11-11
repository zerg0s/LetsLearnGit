# Created by Ilya Nepsha
#
# Task Name: Алфавит

def alphabet(str1, str2):
    arrCh1 = list(map(ord, str1.lower()))
    arrCh2 = list(map(ord, str2.lower()))
    lastCh = len(str1) - 1
    if len(arrCh1) == len(arrCh2):

        print(''.join(map(chr, arrCh1)))
        while (''.join(map(chr, arrCh1)) != ''.join(map(chr, arrCh2))):
            if arrCh1[-1] == 122:
                j = lastCh
                while arrCh1[j] == 122:
                    arrCh1[j] = 97
                    j -= 1
                arrCh1[j] += 1
            else:
                arrCh1[-1] += 1
            print(''.join(map(chr, arrCh1)))
    else:
        print("ERROR!")

if __name__ == "__main__":
    print("hello world")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aax
    alphabet(start, finish) 