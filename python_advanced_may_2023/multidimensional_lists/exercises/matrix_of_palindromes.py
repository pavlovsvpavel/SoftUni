def print_matrix(numbers, n):
    result = ''
    for k in range(len(numbers)):
        result += f"{numbers[k]} "
        if (k + 1) % n == 0:
            result += '\n'
    return result


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
            all_palindromes.extend(palindromes)
            start_letter += 1
            break

print(print_matrix(all_palindromes, cols))


