text = input()

for idx, char in enumerate(text):
    if char == ":":
        print(f"{char}{text[idx + 1]}")
