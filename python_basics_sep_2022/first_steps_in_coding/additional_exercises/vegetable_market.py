vegetables_price = float(input())
fruits_price = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

amount_vegetables = vegetables_price * total_kg_vegetables
amount_fruits = fruits_price * total_kg_fruits

total_amount_bgn = amount_vegetables + amount_fruits
total_amount_eur = total_amount_bgn / 1.94

print(f"{total_amount_eur:.2f}")