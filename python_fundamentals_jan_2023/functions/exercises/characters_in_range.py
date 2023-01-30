def characters_range(char_1, char_2):
    for i in range(char_1 + 1, char_2):
        i = chr(i)
        print(i, end=" ")
    return


first_char = ord(input())
second_car = ord(input())

characters_range(first_char, second_car)
