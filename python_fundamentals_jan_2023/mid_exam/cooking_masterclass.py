from math import ceil
budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
price = 0

for student in range(1, students + 1):
    price += flour_price + 10 * egg_price
    if student % 5 == 0:
        price -= flour_price

aprons = ceil(students * 1.2) * apron_price
total_price = price + aprons
diff = abs(budget - total_price)

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")
