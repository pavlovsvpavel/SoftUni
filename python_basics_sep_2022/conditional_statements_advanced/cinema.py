screening_type = input()
rows = int(input())
columns = int(input())

income = 0

if screening_type == "Premiere":
    income = rows * columns * 12
elif screening_type == "Normal":
    income = rows * columns * 7.50
elif screening_type == "Discount":
    income = rows * columns * 5.00
print(f"{income:.2f} leva")
