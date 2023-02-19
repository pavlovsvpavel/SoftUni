price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
command = input()

entry_value = price_ratings[entry_point]
left_items = []
right_items = []
if command == "cheap":
    for index, item in enumerate(price_ratings):
        if item < entry_value and index < entry_point:
            left_items.append(item)
        elif item < entry_value and index > entry_point:
            right_items.append(item)
elif command == "expensive":
    for index, item in enumerate(price_ratings):
        if item >= entry_value and index < entry_point:
            left_items.append(item)
        elif item >= entry_value and index > entry_point:
            right_items.append(item)

if sum(left_items) >= sum(right_items):
    print(f"Left - {sum(left_items)}")
else:
    print(f"Right - {sum(right_items)}")

