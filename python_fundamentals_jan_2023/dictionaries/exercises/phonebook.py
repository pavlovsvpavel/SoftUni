phonebook = {}

while True:
    info = input()
    if info.isdigit():
        break
    name, phone = info.split("-")
    phonebook[name] = phone

for _ in range(int(info)):
    contact = input()
    if contact not in phonebook:
        print(f"Contact {contact} does not exist.")

    else:
        print(f"{contact} -> {phonebook[contact]}")


