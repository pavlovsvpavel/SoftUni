mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

bonito_amount = bonito_kg * (mackerel_price * 1.6)
safrid_amount = safrid_kg * (sprinkle_price * 1.8)
mussels_amount = mussels_kg * 7.50

total_amount = bonito_amount + safrid_amount + mussels_amount

print(f"{total_amount:.2f}")
