'''
Task #889099
Task #891338
Алфавит
Кириченко Виктор
М3О-121М-20
'''

def function_(beginning, ending, begin_with, first_iteration):
    if beginning[0] != ending[0]:
        for symbol in range(ord(beginning[0]), ord(ending[0])+1):
            if symbol == ord(ending[0]):
                alphabetV2(beginning[1:], ending[1:], \
                    memory = ('' if begin_with == None else begin_with) + beginning[:1], \
                    first_iter = first_iteration, last_iter=True)
            else:
                alphabetV2(beginning[1:], ending[1:], \
                    memory = ('' if begin_with == None else begin_with) + beginning[:1], \
                    first_iter = first_iteration, last_iter=False)
            first_iteration = False
            beginning = chr(ord(beginning[0]) + 1) + beginning[1:]
    else:
        alphabetV2(beginning[1:], ending[1:], memory = begin_with + beginning[0])

def alphabetV2(start, finish, memory = '', first_iter = True, last_iter = None):
    if first_iter and (len(start) != len(finish) or len(start) == 0):
        return

    lenght = len(start)

    if last_iter == None and lenght != 1:
        function_(start, finish, memory, first_iter)
        return

    if last_iter == False:
        finish = 'z' * lenght

    if first_iter == False:
        start = 'a' * lenght

    if lenght == 1:
        for symbol in range(ord(start[0]), ord(finish[0])+1):
            print(f'{memory}{chr(symbol)}')
        return

    function_(start, finish, memory, first_iter)
    return
