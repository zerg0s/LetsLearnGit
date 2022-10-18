from alphabet import printIterationOverStringsAlphabetically

if __name__ == "__main__":
    print("Alphabet task has started :)")
    start = input("Enter a start string: ")  # aaa
    finish = input("Enter where to finish: ")  # aba

    print("First solution")
    printIterationOverStringsAlphabetically(start, finish)
