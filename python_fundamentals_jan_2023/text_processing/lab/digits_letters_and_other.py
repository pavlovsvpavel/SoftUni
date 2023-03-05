string = input()
digits = []
letters = []
other_characters = []
for el in string:
    if el.isdigit():
        digits.append(el)
    elif el.isalpha():
        letters.append(el)
    else:
        other_characters.append(el)

print("".join(digits))
print("".join(letters))
print("".join(other_characters))
