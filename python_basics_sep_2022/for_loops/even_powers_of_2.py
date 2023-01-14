number = int(input())

for current_num in range(number + 1):
    if current_num % 2 == 0:
        final_number = 2 ** current_num
        print(final_number)

