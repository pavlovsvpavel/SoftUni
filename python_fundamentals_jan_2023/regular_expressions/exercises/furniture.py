import re

all_furniture = []
total_sum = 0
while True:
    purchase_input = input()
    if purchase_input == "Purchase":
        break

    pattern = r"\>\>[a-zA-Z]+\<\<\d+\.*\d+\!\d+"
    valid_input = re.findall(pattern, purchase_input)

    if valid_input:
        furniture_name = re.findall(r"[A-Za-z]+", valid_input[0])
        all_furniture.append("".join(furniture_name))
        price = re.findall(r"(?<=\<\<)\d+\.*\d+", valid_input[0])
        price = float("".join(price))
        quantity = re.findall(r"(?<=\!)\d+", valid_input[0])
        quantity = int("".join(quantity))
        total_sum += quantity * price

print("Bought furniture:")
for el in all_furniture:
    print(el)
print(f"Total money spend: {total_sum:.2f}")


# all_furniture = []
# total_sum = 0
# while True:
#     purchase_input = input()
#     if purchase_input == "Purchase":
#         break
#
#     pattern = r"\>\>(?P<name>[a-zA-Z]+)\<\<(?P<price>\d+\.*\d+)!(?P<quantity>\d+)"
#     valid_input = re.finditer(pattern, purchase_input)
#
#     if valid_input:
#         for el in valid_input:
#             all_furniture.append(el["name"])
#             price = float(el["price"])
#             quantity = int(el["quantity"])
#             total_sum += price * quantity
#
# print("Bought furniture:")
# for el in all_furniture:
#     print(el)
# print(f"Total money spend: {total_sum:.2f}")

