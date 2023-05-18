rows, cols = [int(x) for x in input().split(" ")]

all_palindromes = []
start_letter = ord("a")
middle_letter = start_letter + rows + cols

for i in range(start_letter, start_letter + rows):
    palindromes = []
    char_1 = chr(i)

    for j in range(start_letter, middle_letter - 1):
        char_2 = chr(j)
        letters = char_1 + char_2 + char_1
        palindromes.append(letters)

        if len(palindromes) % cols == 0:
            all_palindromes.append(palindromes)
            start_letter += 1
            break

[print(*inner_list, sep=" ") for inner_list in all_palindromes]


