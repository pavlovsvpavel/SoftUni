from sys import maxsize
init_eggs_count = int(input())

sold_eggs = 0

for _ in range(maxsize):
    buy_or_fill = input()

    if buy_or_fill == "Close":
        print(f"Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break

    eggs_count = int(input())

    if buy_or_fill == "Fill":
        init_eggs_count += eggs_count
        continue

    if buy_or_fill == "Buy" and eggs_count <= init_eggs_count:
        init_eggs_count -= eggs_count
        sold_eggs += eggs_count
    else:
        print("Not enough eggs in store!")
        print(f"You can buy only {init_eggs_count}.")
        break






