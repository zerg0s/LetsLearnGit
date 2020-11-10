def change_next_symbol(index, temp_str):
    symbol = ord(temp_str[index]) + 1
    if symbol > ord('z'):
        temp_str = temp_str[0:len(temp_str) + index] + 'a' \
                   + temp_str[len(temp_str) + index + 1:]
        temp_str = change_next_symbol(index - 1, temp_str)
        return temp_str
    else:
        temp_str = temp_str[0:len(temp_str) + index] +\
                   chr(symbol) + temp_str[len(temp_str) + index + 1:]
        return str(temp_str)


def alphabet(start_str, end_str):
    while start_str != end_str:
        for i in range(ord(start_str[-1]) + 1, ord('z')+2):
            print(start_str)
            start_str = start_str[:len(start_str)-1] + chr(i)
            if ord(start_str[-1]) > ord('z'):
                start_str = change_next_symbol(-1, start_str)
                start_str = start_str[:-1] + 'a'
            if start_str == end_str:
                print(start_str)
                break
