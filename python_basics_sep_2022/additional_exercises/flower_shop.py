from math import floor
from math import ceil
magnolia_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

sum_magnolia = magnolia_count * 3.25
sum_hyacinth = hyacinth_count * 4
sum_roses = roses_count * 3.5
sum_cactus = cactus_count * 8
total_sum = sum_magnolia + sum_hyacinth + sum_roses + sum_cactus
taxes = total_sum * 0.05

profit = total_sum - taxes
diff = abs(profit - gift_price)

if profit >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
