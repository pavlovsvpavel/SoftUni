locations = int(input())


for i in range(1, locations + 1):
    expected_avg_mining_per_day = float(input())
    days_per_location = int(input())

    total_mined_gold_per_location = 0

    for j in range(1, days_per_location + 1):
        mined_gold = float(input())

        total_mined_gold_per_location += mined_gold

    avg_mined_gold_per_location = total_mined_gold_per_location / days_per_location
    diff = abs(expected_avg_mining_per_day - avg_mined_gold_per_location)

    if avg_mined_gold_per_location >= expected_avg_mining_per_day:
        print(f"Good job! Average gold per day: {avg_mined_gold_per_location:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")




