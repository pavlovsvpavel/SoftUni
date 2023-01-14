first_number = int(input())
second_number = int(input())
operator = input()

result = 0
even_odd = ""

if operator in ["+", "-", "*"]:
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    if result % 2 == 0:
        even_odd = "even"
    elif result % 2 != 0:
        even_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {result} - {even_odd}")
if operator == "/" and second_number != 0:
    result = first_number / second_number
    print(f"{first_number} {operator} {second_number} = {result:.2f}")
if operator == "%" and second_number != 0:
    result = first_number % second_number
    print(f"{first_number} {operator} {second_number} = {result}")
if operator in ["/", "%"] and second_number == 0:
    print(f"Cannot divide {first_number} by zero")
