budget = float(input())
statists = int(input())
costume_price = float(input())

decor_amount = budget * 0.1
costumes_amount = statists * costume_price

if statists > 150:
    costumes_amount = costumes_amount - (costumes_amount * 0.1)
else:
    costumes_amount = costumes_amount

total_amount = decor_amount + costumes_amount
diff = abs(budget - total_amount)

if budget < total_amount:
    print(f"Not enough money!\nWingard needs {diff:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {diff:.2f} leva left.")