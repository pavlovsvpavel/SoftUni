def even_odd_digit(num):
    digits_list = [int(x) for x in num]
    even_sum = 0
    odd_sum = 0
    for num in digits_list:
        if num % 2 == 0:
            even_sum += num
        elif num % 2 != 0:
            odd_sum += num
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(even_odd_digit(number))
