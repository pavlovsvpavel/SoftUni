char_1 = input()
char_2 = input()
text = input()

start = ord(char_1)
end = ord(char_2)
total_sum = 0
for char in text:
    if ord(char) in range(start + 1, end):
        total_sum += ord(char)

print(total_sum)
