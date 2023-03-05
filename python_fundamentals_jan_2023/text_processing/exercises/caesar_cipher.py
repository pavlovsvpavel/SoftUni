text = input()
encrypted_text = []
for el in text:
    encrypted_el = ord(el) + 3
    encrypted_text.append(chr(encrypted_el))

print("".join(encrypted_text))
