numbers = input()
numbers_list = [int(x) for x in numbers.split(", ")]
indices_list = [x for x in range(len(numbers_list)) if numbers_list[x] % 2 == 0]

print(indices_list)
