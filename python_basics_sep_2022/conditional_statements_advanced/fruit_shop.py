product = input()
day_of_week = input()
quantity = float(input())

total_sum = 0
if product in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"] and \
        day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if product == "banana":
        total_sum = quantity * 2.5
    elif product == "apple":
        total_sum = quantity * 1.20
    elif product == "orange":
        total_sum = quantity * 0.85
    elif product == "grapefruit":
        total_sum = quantity * 1.45
    elif product == "kiwi":
        total_sum = quantity * 2.70
    elif product == "pineapple":
        total_sum = quantity * 5.50
    elif product == "grapes":
        total_sum = quantity * 3.85
    print(f"{total_sum:.2f}")
elif product in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"] and \
        day_of_week in ["Saturday", "Sunday"]:
    if product == "banana":
        total_sum = quantity * 2.70
    elif product == "apple":
        total_sum = quantity * 1.25
    elif product == "orange":
        total_sum = quantity * 0.90
    elif product == "grapefruit":
        total_sum = quantity * 1.60
    elif product == "kiwi":
        total_sum = quantity * 3.00
    elif product == "pineapple":
        total_sum = quantity * 5.60
    elif product == "grapes":
        total_sum = quantity * 4.20
    print(f"{total_sum:.2f}")
else:
    print("error")
