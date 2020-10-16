'''
Task #889099
Task #891338
Алфавит
Кириченко Виктор
М3О-121М-20
'''

def function_(start__, finish__, memory__, first_iter__):
    if start__[0]!=finish__[0]:
        for symbol in range(ord(start__[0]), ord(finish__[0])+1):
            if symbol == ord(finish__[0]):
                alphabetV2(start__[1:], finish__[1:], \
                    memory=('' if memory__ == None else memory__)+start__[:1], \
                    first_iter=first_iter__, last_iter=True)
            else:
                alphabetV2(start__[1:], finish__[1:], \
                    memory=('' if memory__ == None else memory__)+start__[:1], \
                    first_iter=first_iter__, last_iter=False)
            first_iter__ = False
            start__ = chr(ord(start__[0])+1)+start__[1:]
    else:
        alphabetV2(start__[1:], finish__[1:], memory=memory__+start__[0])

def alphabetV2(start, finish, memory = '', first_iter = True, last_iter = None):
    if first_iter and (len(start)!=len(finish) or len(start)==0):
        return

    lenght = len(start)

    if last_iter == None and lenght!=1:
        function_(start, finish, memory, first_iter)
        return

    if last_iter == False:
        finish = 'z'*lenght

    if first_iter == False:
        start = 'a'*lenght

    if lenght == 1:
        for symbol in range(ord(start[0]), ord(finish[0])+1):
            print(f'{memory}{chr(symbol)}')
        return

    function_(start, finish, memory, first_iter)
    return
