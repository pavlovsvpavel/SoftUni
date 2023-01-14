budget = float(input())
category = input()
people_in_group = int(input())

transport = 0
tickets_price = 0
if category == "VIP":
    tickets_price = people_in_group * 499.99
    if people_in_group <= 4:
        transport = budget * 0.75
    elif 5 <= people_in_group <= 9:
        transport = budget * 0.60
    elif 10 <= people_in_group <= 24:
        transport = budget * 0.50
    elif 25 <= people_in_group <= 49:
        transport = budget * 0.40
    elif people_in_group > 49:
        transport = budget * 0.25
if category == "Normal":
    tickets_price = people_in_group * 249.99
    if people_in_group <= 4:
        transport = budget * 0.75
    elif 5 <= people_in_group <= 9:
        transport = budget * 0.60
    elif 10 <= people_in_group <= 24:
        transport = budget * 0.50
    elif 25 <= people_in_group <= 49:
        transport = budget * 0.40
    elif people_in_group > 49:
        transport = budget * 0.25

total_price = tickets_price + transport
diff = abs(total_price - budget)
if total_price <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
