annual_fee = int(input())
shoes_amount = annual_fee * 0.6
outfit_amount = (shoes_amount - (shoes_amount * 0.2))
ball_amount = outfit_amount / 4
accessories_amount = ball_amount / 5
total_amount = annual_fee + shoes_amount + outfit_amount + ball_amount + accessories_amount
print(total_amount)