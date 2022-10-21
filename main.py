import sys

from alphabet import create_next_string

if __name__ == "__main__":
    def main():
        s1 = input()
        s2 = input()

        if len(s1) != len(s2):
            sys.exit(1)

        else:
            print(s1)
            while s1 != s2:
                s1 = create_next_string(s1)
                print(s1)

