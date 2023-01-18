count_times_to_pour = int(input())
water_tank_capacity = 255
total_liters = 0
for _ in range(count_times_to_pour):
    liters = int(input())
    total_liters += liters
    if total_liters > water_tank_capacity:
        print("Insufficient capacity!")
        total_liters -= liters
        continue

print(total_liters)
