def characters_range(char_1, char_2):
    list_characters = []
    for i in range(ord(char_1) + 1, ord(char_2)):
        list_characters.append(chr(i))

    return list_characters


first_char = input()
second_char = input()

result = characters_range(first_char, second_char)
print(" ".join(result))
