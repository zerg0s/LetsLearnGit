alphavit = 'abcdefghijklmnopqrstuvwxyz'
finstr = "aaa"


def check(defst, deffn):
    """Проверка входных данных"""
    if len(defst) != len(deffn):
        print("Error: размер строк разный")
        return False
    elif not defst.isalpha() and deffn.isalpha():
        print("Error: один или несколько символов не являются буквами")
        return False
    else:
        return True


def ticker(lstr1, lstr2, num=0):
    """Перебор букв"""
    while lstr1 < lstr2 and lstr1[num] < 26:
        if len(lstr1)-1 != num:
            ticker(lstr1, lstr2, num+1)
        if num == len(lstr1)-1:
            for j in range(len(lstr1)):
                print(alphavit[lstr1[j]], end="")
            print("")
        lstr1[num] += 1
    lstr1[num] = 0
    if num == 0:
        print(finstr)


def abc(str1: str, str2: str):
    """Главный метод"""
    if check(str1, str2):
        global finstr
        finstr = str2
        masStr1 = []
        masStr2 = []
        for i in range(len(str1)):
            masStr1.append(alphavit.find(str1[i]))
            masStr2.append(alphavit.find(str2[i]))
        ticker(masStr1, masStr2)