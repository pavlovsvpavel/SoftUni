count_juniors = int(input())
count_seniors = int(input())
type_of_competition = input()

count_all = count_juniors + count_seniors
price_juniors = 0
price_seniors = 0
if type_of_competition == "trail":
    price_juniors = count_juniors * 5.50
    price_seniors = count_seniors * 7
elif type_of_competition == "cross-country":
    price_juniors = count_juniors * 8
    price_seniors = count_seniors * 9.50
elif type_of_competition == "downhill":
    price_juniors = count_juniors * 12.25
    price_seniors = count_seniors * 13.75
elif type_of_competition == "road":
    price_juniors = count_juniors * 20
    price_seniors = count_seniors * 21.50

total_price = price_seniors + price_juniors
if type_of_competition == "cross-country" and count_all >= 50:
    total_price = total_price * 0.75

costs = total_price * 0.05
final_price = total_price - costs

print(f"{final_price:.2f}")
