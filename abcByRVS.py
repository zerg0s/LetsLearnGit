# Назовём это точкой входа в функцию
# На вход принимает два данных типа string - это firstWord и secondWord.
# Все проверки делает сам пользователь перед входом в функцию
# После входа мы узнаём размер двух слов и заносим каждую букву в массив, после чего
# переходим в функцию countWords
def alphabet(firstWord, secondWord):
    lenOffFstString, lenOffSecString = len(firstWord), len(secondWord)
    resultStringFst, resultStringSec = [0] * lenOffFstString, [0] * lenOffSecString
    for i in range(0, len(firstWord)):
        resultStringFst[i] = ord(firstWord[i])
    for j in range(0, len(secondWord)):
        resultStringSec[j] = ord(secondWord[j])
    countWords(resultStringFst, 0, resultStringSec, lenOffSecString)

# Рекурсивная функция
# Вызывает саму себя с целью найти конечную букву и выйти в предыдущую рекурсию
# На вход получает 4 переменных - arrayToChange, position, finalArray, length
# arrayToChange - массив, в котором будут происходить изменения
# position - позиция старта
# finalArray - массив, с которым мы будем сравнивать
# length - длина массива
# В функции имеются проверки для выхода.
def countWords(arrayToChange, position, finalArray, length):
    while arrayToChange[position] != 123:
        if position != length - 1:  # Сравниваем размер данных в двух массивах
            position += 1
            countWords(arrayToChange, position, finalArray, length)
            if arrayToChange[position] == finalArray[position]:
                return
        elif position == length - 1:    # Для вывода символа на печать
            for ij in range(0, position + 1):
                print(chr(arrayToChange[ij]), end='')
            print()
        elif arrayToChange[position] == finalArray[position]:   # Если дошли до конечной точки
            position -= 1
            return
        if arrayToChange[position] == finalArray[position] and\
                arrayToChange[position - 1] == finalArray[position - 1]:
            return
        arrayToChange[position] += 1
    arrayToChange[position] = 97
    return
