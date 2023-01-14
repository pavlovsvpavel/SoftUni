number = int(input())

for special_number in range(1111, 10000):
    special_number_str = str(special_number)
    counter = 0
    number_length = len(special_number_str)

    for index, digit in enumerate(special_number_str):
        if int(digit) == 0:
            continue

        if number % int(digit) == 0:
            counter += 1

    if counter == 4:
        print(special_number, end=" ")
    else:
        continue
