def characters_range(char_1, char_2):
    char_1 = ord(char_1)
    char_2 = ord(char_2)
    my_list = []
    for i in range(char_1 + 1, char_2):
        i = chr(i)
        my_list.append(i)
    print(" ".join(my_list))
    return


first_char = input()
second_car = input()

characters_range(first_char, second_car)
