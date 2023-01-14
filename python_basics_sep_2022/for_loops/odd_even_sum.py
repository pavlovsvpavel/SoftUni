numbers_count = int(input())
even_sum = 0
odd_sum = 0

for i in range(1, numbers_count + 1):
    numbers = int(input())
    if i % 2 == 0:
        even_sum += numbers
    else:
        odd_sum += numbers
diff = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    print(f"No\nDiff = {diff}")
