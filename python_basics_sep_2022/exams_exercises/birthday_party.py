rent = float(input())

cake_price = rent * 0.20
drinks = cake_price * 0.55
animator = rent / 3

budget = rent + cake_price + drinks + animator

print(f"{budget:.1f}")
