def reverse_text(text):
    s_idx = 0
    e_idx = len(text) - 1

    while s_idx <= e_idx:
        yield text[e_idx]

        e_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
