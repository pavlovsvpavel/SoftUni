budget = float(input())
flour_price_per_kg = float(input())

eggs_pack_price = 1
milk_1l_price = 4
bread_price_per_piece = eggs_pack_price + flour_price_per_kg + (milk_1l_price / 4)
total_amount = 0
remaining_budget = 0
breads_count = 0
colored_eggs = 0

while True:
    total_amount += bread_price_per_piece
    remaining_budget = budget - total_amount

    if remaining_budget < bread_price_per_piece:
        remaining_budget = bread_price_per_piece
        break

    breads_count += 1
    colored_eggs += 3

    if breads_count % 3 == 0:
        colored_eggs -= (breads_count - 2)

print(f"You made {breads_count} loaves of Easter bread! Now you have {colored_eggs} eggs and "
      f"{remaining_budget:.2f}BGN left.")

