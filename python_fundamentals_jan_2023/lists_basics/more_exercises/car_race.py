numbers = [int(x) for x in input().split(" ")]

cars_distance = len(numbers) // 2
left_car = numbers[:cars_distance]
right_car = numbers[cars_distance + 1:]
left_car_time = 0
right_car_time = 0

for time_left in left_car:
    if time_left == 0:
        left_car_time *= 0.8
        left_car_time += time_left
    else:
        left_car_time += time_left

for time_right in reversed(right_car):
    if time_right == 0:
        right_car_time *= 0.8
        right_car_time += time_right
    else:
        right_car_time += time_right

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
