from collections import deque

times_values = deque(int(x) for x in input().split())
tasks_values = deque(int(x) for x in input().split())

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times_values:
    current_time, current_task = times_values.popleft(), tasks_values.pop()
    calc_time = current_time * current_task

    if 0 <= calc_time <= 60:
        ducks["Darth Vader Ducky"] += 1

    elif 61 <= calc_time <= 120:
        ducks["Thor Ducky"] += 1

    elif 121 <= calc_time <= 180:
        ducks["Big Blue Rubber Ducky"] += 1

    elif 181 <= calc_time <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1

    else:
        tasks_values.append(current_task - 2)
        times_values.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, count in ducks.items():
    print(f"{duck}: {count}")
