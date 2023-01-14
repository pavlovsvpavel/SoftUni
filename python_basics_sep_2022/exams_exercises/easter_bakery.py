flour_price_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
yeast = int(input())

sugar_price_kg = flour_price_kg * 0.75
egg_price = flour_price_kg * 1.10
yeast_price = sugar_price_kg * 0.2

amount_flour = kg_flour * flour_price_kg
amount_sugar = kg_sugar * sugar_price_kg
amount_eggs = eggs * egg_price
amount_yeast = yeast * yeast_price

total_amount = amount_yeast + amount_eggs + amount_sugar + amount_flour

print(f"{total_amount:.2f}")

