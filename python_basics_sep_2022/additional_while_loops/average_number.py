number = int(input())
total_sum = 0
for i in range(1, number + 1):
    input_line = int(input())
    total_sum += input_line

average = total_sum / number
print(f"{average:.2f}")
