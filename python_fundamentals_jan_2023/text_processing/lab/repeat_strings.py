text = input().split(" ")

for idx in range(len(text)):
    text_length = len(text[idx])
    print(f"{text[idx] * text_length}", end="")

