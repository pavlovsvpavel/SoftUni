lines = int(input())

total_sum = 0
for i in range(lines):
    letter = input()
    letter_ascii = ord(letter)
    total_sum += letter_ascii

print(f"The sum equals: {total_sum}")

