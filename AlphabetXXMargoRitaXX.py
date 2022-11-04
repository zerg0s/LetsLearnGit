# Амелина Маргарита
# М3О-109М-22

def character_checking(line):
    # Проверка, что введенная строка состоит только из строчных символов латиницы
    for symbol in line:
        if symbol < 'a' or symbol > 'z':
            raise ValueError


def alphabet_printing(start_line, finish_line):
    try:
        if len(start_line) != len(finish_line) or start_line > finish_line:
            raise ValueError
        character_checking(start_line)
        character_checking(finish_line)

        while start_line != finish_line:
            print(start_line)
            if start_line[-1] != 'z':
                start_line = start_line[:-1] + chr(ord(start_line[-1]) + 1)
            else:
                count = 1
                while start_line[-count] == 'z':
                    count += 1
                if (count - 1) == len(start_line):  # если уже все 'z'
                    break
                start_line = start_line[:-count + 1]  # убираем все последние 'z'
                start_line = start_line[:-1] + chr(ord(start_line[-1]) + 1)  # + 1 к последнему символу
                start_line += 'a' * (count - 1)  # добавляем в конец нужное количество 'a'

        print(start_line)

    except ValueError:
        print("ERROR")
