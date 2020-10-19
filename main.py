import abcExample

if __name__ == '__main__':
    start = str(input())
    finish = str(input())
    try:
        print(start)
        abcWithStartAndFinish.abc(start, finish)
        print(finish)
    except KeyError:
        print("Для перебора вводятся только буквы")
