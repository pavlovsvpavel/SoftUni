import re

text_input = input()
pattern = r"(?<=\b\_)([A-Za-z0-9]+)($|(?=\s))"
result = []
matches = re.finditer(pattern, text_input)

for match in matches:
    if match:
        result.append(match[0])

print(",".join(result))
