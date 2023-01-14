fuel_type = input()
fuel_litres = float(input())
club_card = input()

gas_price = 0.93
gasoline_price = 2.22
diesel_price = 2.33
gas_amount = fuel_litres * gas_price
gasoline_amount = fuel_litres * gasoline_price
diesel_amount = fuel_litres * diesel_price
gas_card_discount = fuel_litres * 0.08
gasoline_card_discount = fuel_litres * 0.18
diesel_card_discount = fuel_litres * 0.12
amount_fuel = 0
wrong_input = True
wrong_fuel_type = fuel_type == "Gas" or fuel_type == "Gasoline" or fuel_type == "Diesel"
wrong_card_input = club_card == "Yes" or club_card == "No"

if not wrong_fuel_type:
    print("Invalid fuel type!")
# # # if fuel_type != "Gas" and fuel_type != "Gasoline" and fuel_type != "Diesel":
# # #     print("Invalid fuel type!")
if not wrong_card_input:
    print("Wrong input for card!")
# # # if club_card != "Yes" and club_card != "No":
# # #     print("Wrong input for card!")

if club_card == "Yes" and fuel_type == "Gas" and fuel_litres < 20:
    amount_fuel = gas_amount - gas_card_discount
elif club_card == "Yes" and fuel_type == "Gas" and 20 <= fuel_litres <= 25:
    amount_fuel = (gas_amount - gas_card_discount - (gas_amount - gas_card_discount) * 0.08)
elif club_card == "Yes" and fuel_type == "Gas" and fuel_litres > 25:
    amount_fuel = (gas_amount - gas_card_discount - (gas_amount - gas_card_discount) * 0.1)
elif club_card == "No" and fuel_type == "Gas" and fuel_litres < 20:
    amount_fuel = gas_amount
elif club_card == "No" and fuel_type == "Gas" and 20 <= fuel_litres <= 25:
    amount_fuel = gas_amount - (gas_amount * 0.08)
elif club_card == "No" and fuel_type == "Gas" and fuel_litres > 25:
    amount_fuel = gas_amount - (gas_amount * 0.1)

elif club_card == "Yes" and fuel_type == "Gasoline" and fuel_litres < 20:
    amount_fuel = gasoline_amount - gasoline_card_discount
elif club_card == "Yes" and fuel_type == "Gasoline" and 20 <= fuel_litres <= 25:
    amount_fuel = (gasoline_amount - gasoline_card_discount - (gasoline_amount - gasoline_card_discount) * 0.08)
elif club_card == "Yes" and fuel_type == "Gasoline" and fuel_litres > 25:
    amount_fuel = (gasoline_amount - gasoline_card_discount - (gasoline_amount - gasoline_card_discount) * 0.1)
elif club_card == "No" and fuel_type == "Gasoline" and fuel_litres < 20:
    amount_fuel = gasoline_amount
elif club_card == "No" and fuel_type == "Gasoline" and 20 <= fuel_litres <= 25:
    amount_fuel = gasoline_amount - (gasoline_amount * 0.08)
elif club_card == "No" and fuel_type == "Gasoline" and fuel_litres > 25:
    amount_fuel = gasoline_amount - (gasoline_amount * 0.1)

elif club_card == "Yes" and fuel_type == "Diesel" and fuel_litres < 20:
    amount_fuel = diesel_amount - diesel_card_discount
elif club_card == "Yes" and fuel_type == "Diesel" and 20 <= fuel_litres <= 25:
    amount_fuel = (diesel_amount - diesel_card_discount - (diesel_amount - diesel_card_discount) * 0.08)
elif club_card == "Yes" and fuel_type == "Diesel" and fuel_litres > 25:
    amount_fuel = (diesel_amount - diesel_card_discount - (diesel_amount - diesel_card_discount) * 0.1)
elif club_card == "No" and fuel_type == "Diesel" and fuel_litres < 20:
    amount_fuel = diesel_amount
elif club_card == "No" and fuel_type == "Diesel" and 20 <= fuel_litres <= 25:
    amount_fuel = diesel_amount - (diesel_amount * 0.08)
elif club_card == "No" and fuel_type == "Diesel" and fuel_litres > 25:
    amount_fuel = diesel_amount - (diesel_amount * 0.1)
else:
    print("Wrong data!")
    wrong_input = False
if wrong_input:
    print(f"{amount_fuel:.2f} lv.")
