input_operator = input()
n1 = int(input())
n2 = int(input())


def calculation(operator):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return int(n1 / n2)
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


print(calculation(input_operator))
