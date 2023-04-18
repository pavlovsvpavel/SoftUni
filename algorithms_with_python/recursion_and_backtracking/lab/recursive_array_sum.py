def numbers_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + numbers_sum(numbers, idx + 1)


numbers_list = [int(x) for x in input().split(" ")]

print(numbers_sum(numbers_list, 0))
