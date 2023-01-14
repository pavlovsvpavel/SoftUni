easter_bread = int(input())
eggs = int(input())
cookies_kg = int(input())

eggs_for_paint = eggs * 12
amount_egg_paint = eggs_for_paint * 0.15
amount_cookies = cookies_kg * 5.40
amount_easter_bread = easter_bread * 3.20
amount_eggs = eggs * 4.35

total_amount = amount_eggs + amount_easter_bread + amount_cookies + amount_egg_paint

print(f"{total_amount:.2f}")




