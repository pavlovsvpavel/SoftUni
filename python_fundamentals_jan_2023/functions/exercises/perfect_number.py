def perfect_number(num):
    divisors_list = []
    for i in range(1, num):
        if num % i == 0:
            divisors_list.append(i)

    if sum(divisors_list) == num:
        return "We have a perfect number!"

    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
