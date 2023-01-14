count_chrysanthemums = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
holiday = input()

count_all = count_roses + count_tulips + count_chrysanthemums
price_for_flowers = 0
arrangement = 2
bouquet_price = 0
if season in ["Spring", "Summer"]:
    price_for_flowers = count_roses * 4.10 + count_tulips * 2.50 + count_chrysanthemums * 2.00
elif season in ["Autumn", "Winter"]:
    price_for_flowers = count_roses * 4.50 + count_tulips * 4.15 + count_chrysanthemums * 3.75
if holiday == "Y":
    price_for_flowers = price_for_flowers * 1.15

if season == "Spring" and count_tulips > 7:
    price_for_flowers = price_for_flowers * 0.95
elif season == "Winter" and count_roses >= 10:
    price_for_flowers = price_for_flowers * 0.90
if count_all > 20:
    price_for_flowers = price_for_flowers * 0.80

bouquet_price = price_for_flowers + arrangement
print(f"{bouquet_price:.2f}")
