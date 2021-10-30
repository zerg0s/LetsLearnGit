#Sedenkov Nikita М30-122М-21

def get_next_string(current_string: str) -> str:
    char_index_to_change = len(current_string) - 1
    while True:
        if current_string[char_index_to_change] == 'z':
            current_string = current_string[:char_index_to_change] \
                          + 'a' \
                          + current_string[char_index_to_change + 1:]
            char_index_to_change -= 1
        else:
            current_string = current_string[:char_index_to_change] \
                          + chr(ord(current_string[char_index_to_change]) + 1) \
                          + current_string[char_index_to_change + 1:]
            break
    return current_string

def enumerate_strings_from_to(start_string: str, end_string: str) -> None:

    if len(start_string) != len(end_string):
        print("Error! String must be the same length")
        return
    if start_string > end_string:
        print("Error! `start_string` must be lexicographically less then `end_string`")
        return


    current_string = start_string

    while current_string <= end_string:
        print(current_string)
        current_string = get_next_string(current_string)
