months = int(input())

total_amount = 0
electricity_amount = 0
water_amount = months * 20
internet_amount = months * 15
others_amount = 0

for _ in range(1, months + 1):
    electricity = float(input())
    electricity_amount += electricity

others_amount = (electricity_amount + water_amount + internet_amount) * 1.20
total_amount += electricity_amount + water_amount + internet_amount + others_amount
print(f"Electricity: {electricity_amount:.2f} lv")
print(f"Water: {water_amount:.2f} lv")
print(f"Internet: {internet_amount:.2f} lv")
print(f"Other: {others_amount:.2f} lv")
print(f"Average: {total_amount / months:.2f} lv")
