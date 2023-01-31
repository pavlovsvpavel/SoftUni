def sum_numbers(n1, n2):
    return n1 + n2


def subtract(res, n3):
    return res - n3


def add_and_subtract(n1, n2, n3):
    sum_of_n1_and_n_2 = sum_numbers(n1, n2)
    result = subtract(sum_of_n1_and_n_2, n3)
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(add_and_subtract(num_1, num_2, num_3))




