trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

amount_puzzles = puzzles_count * 2.60
amount_dolls = dolls_count * 3
amount_teddy_bears = teddy_bears_count * 4.10
amount_minions = minions_count * 8.20
amount_trucks = trucks_count * 2

total_count = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count
total_amount = amount_puzzles + amount_dolls + amount_teddy_bears + amount_minions + amount_trucks
discount = total_amount * 0.25

if total_count >= 50:
    total_amount = total_amount - discount
else:
    total_amount = total_amount

rent = total_amount * 0.1

profit = total_amount - rent
leftover = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {leftover:.2f} lv left.")
else:
    print(f"Not enough money! {leftover:.2f} lv needed.")

