import re

pattern = r"\d+"
list_numbers = []
while True:
    text = input()
    if text:
        matches = re.findall(pattern, text)
        for num in matches:
            list_numbers.append(num)
    else:
        break

print(" ".join(list_numbers))
