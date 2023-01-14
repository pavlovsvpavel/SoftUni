total_sum = 0

while True:
    money = input()

    if money == "NoMoreMoney":
        break

    money = float(money)

    if money >= 0:
        total_sum += money
        print(f"Increase: {money:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {total_sum:.2f}")
