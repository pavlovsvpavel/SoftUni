data = input()

indexes = []
for idx, el in enumerate(data):
    if el == "(":
        indexes.append(idx)

    elif el == ")":
        start_idx = indexes.pop()
        print(f"{data[start_idx:idx + 1]}")
