# created by Чиж Максим М3О-109М-21
# date 28.10.2021
# description Перебор строк от первой до второй в алфавитном порядке

def changeNextSymbol(index, temp):
    curSymbol = ord(temp[index]) + 1
    if curSymbol <= ord('z'):
        temp = temp[0:len(temp) + index] + chr(curSymbol) + temp[len(temp) + index + 1:]
        return str(temp)
    else:
        temp = temp[0:len(temp) + index] + 'a' + temp[len(temp) + index + 1:]
        temp = changeNextSymbol(index - 1, temp)
        return temp

def IterateStrings(start, finish):
    if start > finish or len(start) != len(finish):
        print("Ошибка! Строки разной длины или не в алфавитном порядке")
    else:
        while start != finish:
            for i in range(ord(start[-1]) + 1, ord('z') + 2):
                print(start)
                start = start[:len(start) - 1] + chr(i)
                if ord(start[-1]) > ord('z'):
                    start = changeNextSymbol(-1, start)
                    start = start[:-1] + 'a'
                if start == finish:
                    print(start)
                    break
