def get_next(str1):
    i= 1
    if str1[-1] != 'z':
        return str1[:-i] + chr(ord(str1[-1]) + 1)
    while str1[-i] == 'z':
        i+= 1
    if i== len(str1) + 1:
        return ""
    retval= str1[:-i+ 1]
    retval= get_next(retval)
    retval+= 'a' * (i-1)
    return retval
def containNumbers(value):
    if value.isalpha():
            return 0
    return 1
def generalFunc(str1,str2):
    if containNumbers(str1) == 1 or containNumbers(str2) == 1:
            print('введенные значения содержат цифры/или отсутствуют значения')
    elif str1 == str2:
            print('Значения строк равны!')
    else:
        try:
            if len(str1) == len(str2):
                tmp= get_next(str1)
                while tmp!= str2:
                        print(tmp)
                        tmp= get_next(tmp)
            else:
                    print('Error: Разные длины строк ')
        except IndexError:
            print('Error: Индекс за пределами ')

