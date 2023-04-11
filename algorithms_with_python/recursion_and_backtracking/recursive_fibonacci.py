def fib(number):
    if number <= 1:
        return 1

    return fib(number - 1) + fib(number - 2)


num = int(input())  # with big numbers, the program will hang
print(fib(num))


def fib(number):
    fib0 = 1
    fib1 = 1
    result = 0

    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


num = int(input())
print(fib(num))
