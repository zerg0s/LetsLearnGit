def gen_next(s):
    if ' ' in s:  # если gen_next работает не первый раз, s имеет вид a b ... a то есть между символами пробелы
        s = s.split(' ')
    else:  # иначе s имеет виде ab..a, нужно сделать список ['a','b',...,'a']
        s = list(s)

    # цикл идет с последного символа s
    # диапазон len(s)-1, -1, -1 означет начать с последного индекса len(s)-1 до -1 не включительно
    for i in range(len(s) - 1, -1, -1):
        while s[i] == 'z':  # если строка имеет например вид azzz, символы 'z' нужно заменить на 'a'
            s[i] = 'a'
            i -= 1

        # для примера выше на этом этапе s = aaaa
        # i = 0
        s[i] = chr(ord(s[i]) + 1)  # запишем след. символ в вместо первого символа не равного 'z' в строке azzz
        # тут уже s = baaa
        break

    return ''.join(map(str, s))  # вернем результат, сделав из списка строку
    


def gen_generation(s1, s2):
#проверка на совпадение длины, если их длины не совпадают выводим сообщение
    if len(s1) != len(s2):
        print("Строки разной длины") 
    
    else:
        print('\n' + s1)
        while s1 != s2:  # пока они не равны
            s1 = gen_next(s1)  # найдем строку, которая идет после s1 по словарю
            print(s1)
            