def discount_calculation(amount):
    if price == "special":
        result = amount * 0.9
        return result
    else:
        result = amount
        return result


customer = ["special", "regular"]
total_price = 0
while True:
    price = input()
    if price in customer:
        break
    price = float(price)
    if price < 0:
        print("Invalid price!")
        continue
    total_price += price

price_with_taxes = total_price * 1.2
taxes = price_with_taxes - total_price
if discount_calculation(price_with_taxes) > 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$\n-----------")
    print(f"Total price: {discount_calculation(price_with_taxes):.2f}$")
else:
    print("Invalid order!")
