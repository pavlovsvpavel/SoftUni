def factorial(number):
    current_result = 1
    for current_number in range(1, number + 1):
        current_result *= current_number
    return current_result


first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial(second_number)
result = first_factorial / second_factorial
print(f"{result:.2f}")
