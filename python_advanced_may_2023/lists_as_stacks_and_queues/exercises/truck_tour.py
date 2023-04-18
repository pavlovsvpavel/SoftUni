from collections import deque
pumps = int(input())

visited_pumps = deque()
# consumption per 1 kilometer is 1 liter of petrol

for _ in range(pumps):
    pump_info = [int(x) for x in input().split(" ")]
    visited_pumps.append(pump_info)

for pump_idx in range(pumps):
    total_petrol = 0
    full_circle = True
    for litres_of_petrol, distance_to_next_pump in visited_pumps:
        total_petrol += litres_of_petrol
        if distance_to_next_pump > total_petrol:
            full_circle = False
            break
        else:
            total_petrol -= distance_to_next_pump
    if full_circle:
        print(pump_idx)
        break
    else:
        visited_pumps.append(visited_pumps.popleft())
