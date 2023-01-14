chicken_menus = int(input())
fish_menus = int(input())
vegi_menus = int(input())
amount_chicken_menus = chicken_menus * 10.35
amount_fish_menus = fish_menus * 12.40
amount_vegi_menus = vegi_menus * 8.15
amount_all_menus = amount_chicken_menus + amount_fish_menus + amount_vegi_menus
amount_desert = amount_all_menus * 0.2
amount_for_delivery = float(2.50)
total_amount = amount_all_menus + amount_desert + amount_for_delivery
print(total_amount)
