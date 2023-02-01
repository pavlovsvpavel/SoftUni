def calculation(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return calculation(n - 1) + calculation(n - 2) + calculation(n - 3)


def result(num):
    for i in range(1, num + 1):
        print(calculation(i), "", end="")


number = int(input())
result(number)



