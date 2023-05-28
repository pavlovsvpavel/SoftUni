import re

even_lines = []
pattern = r"-|,|, |\.|\!|\?"

with open("files/text.txt", "r") as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            current_line = line.strip()
            current_line = re.sub(pattern, "@", current_line)
            even_lines.append(current_line.split()[::-1])

[print(" ".join(el)) for el in even_lines]
