clothes_box = [int(x) for x in input().split(" ")]

rack_capacity = int(input())
count_racks = 0
current_rack_capacity = 0
while clothes_box:
    current_clothing = clothes_box.pop()
    current_rack_capacity += current_clothing
    if current_rack_capacity == rack_capacity:
        current_rack_capacity = 0
        count_racks += 1
    elif current_rack_capacity > rack_capacity:
        current_rack_capacity = 0
        count_racks += 1
        current_rack_capacity += current_clothing

if current_rack_capacity > 0:
    count_racks += 1

print(count_racks)
