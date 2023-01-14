moves = int(input())

points = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_number = 0
for i in range(1, moves + 1):
    number = int(input())
    if 0 <= number <= 9:
        points += (number * 0.2)
        from_0_to_9 += 1
    elif 10 <= number <= 19:
        points += (number * 0.3)
        from_10_to_19 += 1
    elif 20 <= number <= 29:
        points += (number * 0.4)
        from_20_to_29 += 1
    elif 30 <= number <= 39:
        points += 50
        from_30_to_39 += 1
    elif 40 <= number <= 50:
        points += 100
        from_40_to_50 += 1
    else:
        points = points / 2
        invalid_number += 1

print(f"{points:.2f}")
print(f"From 0 to 9: {from_0_to_9 / moves * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19 / moves * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / moves * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / moves * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid_number / moves * 100:.2f}%")
