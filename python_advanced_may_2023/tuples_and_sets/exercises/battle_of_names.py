def ascii_calc(word, row):
    sum_of_ascii_values = 0
    for ch in word:
        sum_of_ascii_values += ord(ch)

    return sum_of_ascii_values // row


n = int(input())

even_set = set()
odd_set = set()
for current_row in range(1, n + 1):
    name = input()

    if ascii_calc(name, current_row) % 2 == 0:
        even_set.add(ascii_calc(name, current_row))
    else:
        odd_set.add(ascii_calc(name, current_row))

even_sum = sum(even_set)
odd_sum = sum(odd_set)
result = []
if even_sum == odd_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
elif even_sum < odd_sum:
    result = odd_set.difference(even_set)

print(", ".join(map(str, result)))
