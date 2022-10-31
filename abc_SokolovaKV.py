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
def containNumbers(value, l):
    for i in l:
        if i in value:
            return 1
    return 0
def main():
    list_ = ["0","1","2","3","4","5","6","7","8","9"]
    try:
        str1 = str(input())
        str2 = str(input())
        if containNumbers(str1, list_) == 1 or containNumbers(str2, list_) == 1:
            print('введенные значения содержат цифры')
        elif str1 == str2:
            print('Значения строк равны!')
        else:
            if len(str1) == len(str2):
                tmp= get_next(str1)
                while tmp!= str2:
                    print(tmp)
                    tmp= get_next(tmp)
            else:
                print('Error: Разные длины строк ')
    except IndexError:
        print('Error: Индекс за пределами ')
