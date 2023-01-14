init_money = float(input())
year = int(input())

age = 18
spend_money = 0
for i in range(1800, year + 1):
    if i % 2 == 0:
        spend_money += 12000
        age = age + 1
    else:
        spend_money += 12000 + (50 * age)
        age = age + 1

diff = abs(spend_money - init_money)

if spend_money <= init_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")


