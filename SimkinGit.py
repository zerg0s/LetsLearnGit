# Kirill Simkin
# Task 6

def change_iteration(l1: str, l2: str):
    l1 = list(l1)
    l2 = list(l2)
    idx = last_index(l1)
    previousIdx = idx - 1

    while l1 != l2:
        if l1[previousIdx] == "z" and l1[idx] == "z":
            l1[idx] = "a"
            l1[previousIdx] = "a"
            l1[previousIdx - 1] = next_alpha(l1[previousIdx - 1])
            print("".join(l1))

        if l1[idx] < "z":
            l1[idx] = next_alpha(l1[idx])
            print("".join(l1))

        elif l1[idx] == "z":
            l1[idx] = "a"
            l1[previousIdx] = next_alpha(l1[previousIdx])
            print("".join(l1))


def last_index(word):
    return len(word) - 1


def next_alpha(c):
    return chr(((ord(c.upper()) + 1 - 65) % 26 + 65)).lower()
