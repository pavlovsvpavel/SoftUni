def min_max_sum(num):
    numbers_list = [int(x) for x in num.split(" ")]
    minimum_number = min(numbers_list)
    maximum_number = max(numbers_list)
    sum_of_numbers = sum(numbers_list)
    return f"The minimum number is {minimum_number}\n" \
           f"The maximum number is {maximum_number}\n" \
           f"The sum number is: {sum_of_numbers}"


user_input = input()
print(min_max_sum(user_input))
