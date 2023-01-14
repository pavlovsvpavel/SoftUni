# •	кошничка за яйца (basket) – 1.50 лв.
# •	великденски венец (wreath) – 3.80 лв.
# •	шоколадов заек (chocolate bunny) – 7 лв.


count_customers = int(input())
total_amount = 0
for _ in range(count_customers):
    purchases_per_customer = 0
    amount = 0
    while True:
        type_of_purchase = input()

        if type_of_purchase == "Finish":
            break

        purchases_per_customer += 1

        if type_of_purchase == "basket":
            amount += 1.50
        elif type_of_purchase == "wreath":
            amount += 3.80
        elif type_of_purchase == "chocolate bunny":
            amount += 7.00

    if purchases_per_customer % 2 == 0:
        amount = amount * 0.8

    total_amount += amount

    print(f"You purchased {purchases_per_customer} items for {amount:.2f} leva.")

average_amount = total_amount / count_customers
print(f"Average bill per client is: {average_amount:.2f} leva.")


