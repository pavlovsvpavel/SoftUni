secret_message = input().split(" ")

for word in secret_message:
    deciphered_message = []
    digits_in_word = list(filter(lambda x: x.isdigit(), word))
    digits_in_word = "".join(digits_in_word)
    digits_to_letter = chr(int(digits_in_word))
    deciphered_message.append(digits_to_letter)

    # letters_word = list(filter(lambda x: x.isalpha(), word))
    letters_word = [x for x in word if x.isalpha()]
    deciphered_message.extend(letters_word)
    deciphered_message[1], deciphered_message[-1] = deciphered_message[-1], deciphered_message[1]

    print("".join(deciphered_message), end=" ")
