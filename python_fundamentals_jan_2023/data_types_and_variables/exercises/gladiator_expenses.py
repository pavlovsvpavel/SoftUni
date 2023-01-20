lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
counter = 0
for lost_game in range(1, lost_fights + 1):
    if lost_game % 2 == 0:
        expenses += helmet_price

    if lost_game % 3 == 0:
        expenses += sword_price
        if lost_game % 2 == 0:
            expenses += shield_price
            counter += 1

if counter >= 2:
    expenses += int(counter / 2) * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
