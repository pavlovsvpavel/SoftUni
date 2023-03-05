text_1 = input()
text_2 = input()

while text_1 in text_2:
    text_2 = text_2.replace(text_1, "")

print(text_2)
