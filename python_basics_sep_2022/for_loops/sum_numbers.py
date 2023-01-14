number_of_lines = int(input())

total_sum = 0
for _ in range(1, number_of_lines + 1):
    current_number = int(input())
    total_sum += current_number
print(total_sum)

