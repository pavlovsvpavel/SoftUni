from math import ceil
guests_count = int(input())
budget = int(input())

easter_bread_count = ceil(guests_count / 3)
eggs_count = guests_count * 2

amount_easter_bread = easter_bread_count * 4
amount_eggs = eggs_count * 0.45
total_amount = amount_eggs + amount_easter_bread

diff = abs(total_amount - budget)

if total_amount <= budget:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
