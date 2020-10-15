# This is only an example
# Not a good solution of a task

def abc(start, finish):
    for symbol in range(ord(start[-1]), ord(finish[-1])):
        print(f"{start[:-1]}{chr(symbol)}")
