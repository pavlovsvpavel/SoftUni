from collections import deque

green_light_duration_sec = int(input())
free_window_sec = int(input())
cars_queue = deque()
counter = 0
crash = False
while True:
    if crash:
        break

    command = input()

    if command == "END":
        break

    if command == "green":
        current_green_light = green_light_duration_sec
        for _ in range(len(cars_queue)):
            if current_green_light > 0:
                current_car = cars_queue.popleft()
                car_length = len(current_car)
                current_green_light -= car_length
                if current_green_light >= 0:
                    counter += 1
                else:
                    if current_green_light + free_window_sec >= 0:
                        counter += 1
                    else:
                        passed_chars = car_length + current_green_light + free_window_sec
                        hit_char = current_car[passed_chars]
                        print(f"A crash happened!")
                        print(f"{current_car} was hit at {hit_char}.")
                        crash = True
                        break

    else:
        car_name = command
        cars_queue.append(car_name)

if not crash:
    print(f"Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")
