expected_amount = int(input())

input_line = input()
counter = 0
counter_cash = 0
counter_card = 0
total_amount = 0
cash_amount = 0
card_amount = 0
flag = False
while input_line != "End":
    input_line = int(input_line)
    counter += 1
    if counter % 2 != 0:
        if input_line <= 100:
            total_amount += input_line
            cash_amount += input_line
            counter_cash += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    elif counter % 2 == 0:
        if input_line >= 10:
            total_amount += input_line
            card_amount += input_line
            counter_card += 1
            print("Product sold!")
        else:
            print("Error in transaction!")

    if total_amount >= expected_amount:
        flag = True
        break

    input_line = input()

if counter_cash == 0:
    average_cash = cash_amount
else:
    average_cash = cash_amount / counter_cash

if counter_card == 0:
    average_card = card_amount
else:
    average_card = card_amount / counter_card

if flag:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
else:
    print("Failed to collect required money for charity.")
