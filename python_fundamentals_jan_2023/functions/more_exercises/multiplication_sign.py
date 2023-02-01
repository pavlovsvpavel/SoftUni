def calc(n1, n2, n3):
    lst_numbers = [n1, n2, n3]
    result = ""
    if n1 == 0 or n2 == 0 or n3 == 0:
        result = "zero"
    elif min(lst_numbers) > 0:
        result = "positive"
    elif min(lst_numbers) < 0:
        result = "negative"
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(calc(num1, num2, num3))
