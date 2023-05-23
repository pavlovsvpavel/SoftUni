def even_odd(*args):
    nums = list(filter(lambda x: type(x) == int, args))
    command = [el for el in args if type(el) == str]
    evens = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    if command[0] == "even":
        return evens
    else:
        return odds


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
