fuel = input()
quantity_fuel = float(input())
club_card = input()
price = 0
total = 0
gasoline_per_litre = 2.22
diesel_per_litre = 2.33
gas_per_litre = 0.93
if fuel == "Gas":
    if club_card == "Yes":
        price = gas_per_litre - 0.08
        total = quantity_fuel * price
    elif club_card == "No":
        total = quantity_fuel * gas_per_litre
elif fuel == "Gasoline":
    if club_card == "Yes":
        price = gasoline_per_litre - 0.18
        total = quantity_fuel * price
    elif club_card == "No":
        total = quantity_fuel * gasoline_per_litre
elif fuel == "Diesel":
    if club_card == "Yes":
        price = diesel_per_litre - 0.12
        total = quantity_fuel * price
    elif club_card == "No":
        total = quantity_fuel * diesel_per_litre
if 25 >= quantity_fuel >= 20:
    total = total * 0.92
elif quantity_fuel > 25:
    total = total * 0.90
print(f"{total:.2f} lv.")
