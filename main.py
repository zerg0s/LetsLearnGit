import abcStartFinish

if __name__ == '__main__':
    start = str(input())
    finish = str(input())
    try:
        print(start)
        abcStartFinish.abc(start, finish)
        print(finish)
    except KeyError:
        print("Для перебора вводятся только буквы")
