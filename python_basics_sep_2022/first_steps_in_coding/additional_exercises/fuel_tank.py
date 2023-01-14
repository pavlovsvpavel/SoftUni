fuel_type = input().capitalize()
available_litres_fuel = float(input())

needed_litres_fuel = 25
diff = available_litres_fuel - needed_litres_fuel

if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")
elif fuel_type == "Diesel" and diff >= 0:
    print(f"You have enough {fuel_type.lower()}.")
elif fuel_type == "Gas" and diff >= 0:
    print(f"You have enough {fuel_type.lower()}.")
elif fuel_type == "Gasoline" and diff >= 0:
    print(f"You have enough {fuel_type.lower()}.")
else:
    print(f"Fill your tank with {fuel_type.lower()}!")
