days = int(input())

total_money = 0
total_wins = 0
total_loses = 0

for i in range(1, days + 1):
    money_per_day = 0
    wins_per_day = 0
    loses_per_day = 0
    while True:
        sport = input()

        if sport == "Finish":
            break

        result = input()

        if result == "win":
            money_per_day += 20
            wins_per_day += 1
        elif result == "lose":
            loses_per_day += 1

    if wins_per_day > loses_per_day:
        money_per_day = money_per_day * 1.1
        total_money += money_per_day
        total_wins += wins_per_day
        total_loses += loses_per_day
    else:
        total_money += money_per_day
        total_wins += wins_per_day
        total_loses += loses_per_day

if total_wins > total_loses:
    total_money = total_money * 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

