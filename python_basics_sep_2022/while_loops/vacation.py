trip_money = float(input())
available_money = float(input())

spend_days = 0
total_days = 0
flag = False
while True:
    type_of_action = input()
    amount = float(input())
    if type_of_action == "spend":
        total_days += 1
        spend_days += 1
        available_money -= amount
        if available_money <= 0:
            available_money = 0
        if spend_days == 5:
            flag = True
            break

    if type_of_action == "save":
        total_days += 1
        spend_days = 0
        available_money += amount

    if available_money >= trip_money:
        break

if flag:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")
