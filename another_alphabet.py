# created by abdulla begimkulov
# date 13.09.2021
# description вывести в лексикографическом порядке строки от start_str до end_str


def get_next_str(input):
    inp_list = list(input)
    is_chaged = False
    for i in range(len(inp_list) - 1, -1, -1):
        if ord(inp_list[i]) < 122:
            inp_list[i] = chr(ord(inp_list[i]) + 1)
            inp_list[i+1:] = ['a' for _ in range(len(inp_list) - 1, i, -1)]
            is_chaged = True
            break
    if is_chaged == False:
        return -1
    return "".join(inp_list)


def print_strings_lexicographically(start_str, end_str):
    if len(start_str) != len(end_str) or start_str > end_str:
        print("Строки должны быть одинаковой длинны и введены в алфавитном порядке")
        return
    for_print = start_str
    while for_print != -1:
        print(for_print)
        if hash(for_print) == hash(end_str) and for_print == end_str:
            break
        for_print = get_next_str(for_print)
