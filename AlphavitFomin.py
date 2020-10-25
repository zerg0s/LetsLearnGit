"""Алфавитный таймер"""
# Выполнил Кузнецов Андрей и Дмитрий Фомин


def input_(msg):
    input_data = input(msg)
    if not input_data.isalpha():
        return input_("Ошибка: ")
    return input_data

def ticker(lstr1, lstr2, num=0):
    masStr1 = []
    masStr2 = []
    alphavit = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(lstr1)):
        masStr1.append(alphavit.find(lstr1[i]))
        masStr2.append(alphavit.find(lstr2[i]))
    while lstr1 < lstr2 and lstr1[num] < 26:
        if len(lstr1)-1 != num:
            ticker(lstr1, lstr2, num+1)
        if num == len(lstr1)-1:
            for i in range(len(lstr1)):
                print(alphavit[lstr1[i]], end="")
            print("")
        lstr1[num] += 1
    lstr1[num] = 0
    if(num == 0):
        print(str2)


str1 = str(input_(''))
str2 = str(input_(''))
while len(str1) != len(str2):
    print('Длина первой строки отличается от длины второй строки, повторите ввод: ')
    str2 = str(input_(''))
try:
    ticker(str1, str2)
except ValueError:
    print("некорректный ввод")
