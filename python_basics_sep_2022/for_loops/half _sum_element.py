import sys
number = int(input())

max_number = - sys.maxsize
total_sum = 0
final_sum = 0
for i in range(1, number + 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number
diff = (total_sum - max_number)
final_sum = abs(max_number - diff)
if total_sum / max_number == 2:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {final_sum}")


