secret_word = ""
counter_c = 0
counter_o = 0
counter_n = 0
word = ""

input_line = input()
while input_line != "End":
    input_line = ord(input_line)

    if input_line in range(65, 91) or input_line in range(97, 123):
        input_line = chr(input_line)
    else:
        input_line = input()
        continue

    if input_line == "c" and counter_c == 0:
        counter_c += 1
    elif input_line == "o" and counter_o == 0:
        counter_o += 1
    elif input_line == "n" and counter_n == 0:
        counter_n += 1
    else:
        word += input_line

    if counter_c + counter_o + counter_n == 3:
        secret_word += word
        secret_word += " "
        word = ""
        counter_c = 0
        counter_o = 0
        counter_n = 0

    input_line = input()

print(secret_word)
