record_in_sec = float(input())
distance = float(input())
time_sec_1m = float(input())

all_time_sec = distance * time_sec_1m
delay_times = distance // 50
delay_sec = delay_times * 30

final_time_sec = all_time_sec + delay_sec
diff_sec = abs(record_in_sec - final_time_sec)

if final_time_sec < record_in_sec:
    print(f"Yes! The new record is {final_time_sec:.2f} seconds.")
else:
    print(f"No! He was {diff_sec:.2f} seconds slower.")
