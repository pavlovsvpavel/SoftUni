pens_count = int(input())
markers_count = int(input())
detergent_litres = int(input())
discount_percent = int(input())
amount_pens = pens_count * 5.80
amount_markers = markers_count * 7.20
amount_detergent_liters = detergent_litres * 1.20
total_amount = amount_pens + amount_markers + amount_detergent_liters
total_discount = total_amount * discount_percent/100
print(total_amount - total_discount)
