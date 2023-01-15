coins_1_lv = int(input())
coins_2_lv = int(input())
coins_5_lv = int(input())
amount = int(input())

for i in range(coins_1_lv + 1):
    for j in range(coins_2_lv + 1):
        for k in range(coins_5_lv + 1):
            calc_amount = i * 1 + j * 2 + k * 5
            if calc_amount == amount:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {amount} lv.")
                continue
