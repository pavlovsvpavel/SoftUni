from itertools import zip_longest

string_1, string_2 = input().split(" ")
total_sum = 0
for (char_1, char_2) in zip_longest(string_1, string_2, fillvalue=0):
    if char_1 != 0 and char_2 != 0:
        total_sum += ord(char_1) * ord(char_2)
    elif char_1 == 0:
        total_sum += char_1 + ord(char_2)
    else:
        total_sum += ord(char_1) + char_2

print(total_sum)
