sum_prime = 0
sum_non_prime = 0

while True:
    number = input()

    if number == "stop":
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    counter = 0

    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1

    if counter > 2:
        sum_non_prime += number
    else:
        sum_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")


