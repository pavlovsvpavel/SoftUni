age = int(input())
price_wash_machine = float(input())
toy_price = int(input())

money_per_birthday = 0
money_all_birthdays = 0
count_toys = 0
total_money = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys += 1
    else:
        money_per_birthday += 10
        money_all_birthdays += money_per_birthday

brother_money = age - count_toys
total_money = (count_toys * toy_price + money_all_birthdays - brother_money)
diff = abs(total_money - price_wash_machine)
if total_money >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
