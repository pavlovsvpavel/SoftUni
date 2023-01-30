numbers = list(map(float, input().split(" ")))


def calc(n):
    return abs(n)


result = map(calc, numbers)
print(list(result))
