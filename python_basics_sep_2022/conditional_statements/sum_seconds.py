first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time_sec = first_time + second_time + third_time
time_min = total_time_sec // 60
time_sec = total_time_sec % 60

if time_sec < 10:
    print(f"{time_min}:0{time_sec}")
else:
    print(f"{time_min}:{time_sec}")