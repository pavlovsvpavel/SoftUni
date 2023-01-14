hours = int(input())
minutes = int(input())

hours_in_minutes = hours * 60
all_minutes = hours_in_minutes + minutes + 15
total_hours = all_minutes // 60
total_minutes = all_minutes % 60

if total_hours > 23:
    total_hours = 0

if total_minutes < 10:
    total_minutes = f"0{total_minutes}"

print(f"{total_hours}:{total_minutes}")

