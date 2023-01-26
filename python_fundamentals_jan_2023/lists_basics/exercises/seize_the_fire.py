fires_and_cells = input().split("#")
water = int(input())

fire_list = []

total_fire_sum = 0
effort_sum = 0
successful_fires = []

for fire in fires_and_cells:
    fire_list = fire.split(" = ")
    fire_check = False
    current_fire_value = int(fire_list[1])

    if "High" in fire_list and 81 <= current_fire_value <= 125:
        fire_check = True
    elif "Medium" in fire_list and 51 <= current_fire_value <= 80:
        fire_check = True
    elif "Low" in fire_list and 1 <= current_fire_value <= 50:
        fire_check = True

    if fire_check and water >= current_fire_value:
        water -= current_fire_value
        total_fire_sum += current_fire_value
        effort_sum += current_fire_value * 0.25
        successful_fires.append(fire_list[1])
    else:
        continue

print(f"Cells:")

for item in successful_fires:
    print(f" - {item}")

print(f"Effort: {effort_sum:.2f}")
print(f"Total Fire: {total_fire_sum}")
