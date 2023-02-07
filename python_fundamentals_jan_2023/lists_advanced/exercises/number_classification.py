def num_to_string(lst):
    lst = list(map(str, lst))
    result = ", ".join(lst)
    return result


numbers = input()
num_list = [int(x) for x in numbers.split(", ")]

positive_numbers = list(filter(lambda num: num >= 0, num_list))
negative_numbers = list(filter(lambda num: num < 0, num_list))
even_numbers = list(filter(lambda num: num % 2 == 0, num_list))
odd_numbers = list(filter(lambda num: num % 2 != 0, num_list))


print(f"Positive: {num_to_string(positive_numbers)}")
print(f"Negative: {num_to_string(negative_numbers)}")
print(f"Even: {num_to_string(even_numbers)}")
print(f"Odd: {num_to_string(odd_numbers)}")

