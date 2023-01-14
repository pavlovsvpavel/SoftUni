budget = float(input())
flour_price_per_kg = float(input())

eggs_pack_price = flour_price_per_kg * 0.75
milk_1l_price = flour_price_per_kg * 1.25
bread_price_per_piece = eggs_pack_price + flour_price_per_kg + (milk_1l_price / 4)

breads_count = 0
colored_eggs = 0

while bread_price_per_piece <= budget:
    budget -= bread_price_per_piece
    breads_count += 1
    colored_eggs += 3

    if breads_count % 3 == 0:
        colored_eggs -= (breads_count - 2)

print(f"You made {breads_count} loaves of Easter bread! Now you have {colored_eggs} eggs and "
      f"{budget:.2f}BGN left.")

