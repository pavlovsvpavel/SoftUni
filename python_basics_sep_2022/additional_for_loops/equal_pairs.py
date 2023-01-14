pairs_count = int(input())
previous_sum = int(input()) + int(input())
max_diff = 0

for _ in range(1, pairs_count):
    current_sum = int(input()) + int(input())
    if abs(current_sum - previous_sum) > max_diff:
        max_diff = abs(current_sum - previous_sum)

    previous_sum = current_sum
if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")
