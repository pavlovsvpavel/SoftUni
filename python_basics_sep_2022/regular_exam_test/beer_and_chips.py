import math
name = input()
budget = float(input())
beers = int(input())
chips = int(input())

amount_beers = beers * 1.2
amount_chips = math.ceil(chips * (amount_beers * 0.45))
total_amount = amount_beers + amount_chips

diff = abs(total_amount - budget)

if total_amount <= budget:
    print(f"{name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name} needs {diff:.2f} more leva!")
