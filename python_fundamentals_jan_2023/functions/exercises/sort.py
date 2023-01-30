def sorting_numbers(num):
    numbers_list = [int(x) for x in num.split(" ")]
    return sorted(numbers_list)


user_input = input()
print(sorting_numbers(user_input))
