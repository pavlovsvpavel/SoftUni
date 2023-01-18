num = int(input())

for i in range(1, num + 1):
    first_digit = i // 10
    second_digit = i % 10
    sum_of_digits = first_digit + second_digit
    if str(sum_of_digits) in ["5", "7", "11"]:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

