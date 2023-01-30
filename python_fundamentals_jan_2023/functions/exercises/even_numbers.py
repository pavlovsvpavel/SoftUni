def even_numbers(num):
    numbers_list = [int(x) for x in num.split(" ")]
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
    return list(filter(lambda x: x % 2 == 0, numbers_list))


user_input = input()
# numbers_list = [int(x) for x in user_input.split(" ")]
# result = filter(even_numbers, numbers_list)
# print(list(result))
print(even_numbers(user_input))
