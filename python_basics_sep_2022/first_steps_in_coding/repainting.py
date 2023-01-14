nylon_qty = int(input())
paint_qty = int(input())
paint_thinner_qty = int(input())
hours_for_repainting = int(input())
amount_nylon = ((nylon_qty + 2) * 1.5)
amount_paint = ((paint_qty + paint_qty * 0.1) * 14.5)
amount_paint_thinner = paint_thinner_qty * 5.00
amount_for_bags = float(0.40)
total_amount = amount_nylon + amount_paint + amount_paint_thinner + amount_for_bags
workers_fee_per_hour = total_amount * 0.3
total_workers_fee = workers_fee_per_hour * hours_for_repainting
print(total_amount + total_workers_fee)