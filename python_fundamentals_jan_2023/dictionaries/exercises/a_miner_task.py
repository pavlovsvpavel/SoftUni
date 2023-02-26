dictionary = {}

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    if resource not in dictionary.keys():
        dictionary[resource] = quantity
    elif resource in dictionary.keys():
        dictionary[resource] += quantity

for resource, quantity in dictionary.items():
    print(f"{resource} -> {quantity}")
