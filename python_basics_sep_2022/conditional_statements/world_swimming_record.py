world_rekord = float(input())
distance = float(input())
time_in_sec_1m = float(input())

total_time = distance * time_in_sec_1m
delay_in_sec = (distance // 15) * 12.5

final_time = total_time + delay_in_sec
diff = abs(world_record - final_time)

if final_time >= world_record:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
