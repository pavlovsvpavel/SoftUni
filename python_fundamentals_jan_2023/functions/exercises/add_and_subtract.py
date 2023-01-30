def add_and_subtract(n1, n2, n3):
    return add_and_subtract(num_1, num_2, num_3)


def sum_numbers(n1, n2):
    return n1 + n2


def subtract(n3):
    return sum_numbers(n1=num_1, n2=num_2) - n3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(subtract(num_3))
