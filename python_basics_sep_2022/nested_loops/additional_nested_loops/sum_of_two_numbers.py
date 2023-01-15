first_num = int(input())
last_num = int(input())
magic_num = int(input())

sum_of_num = 0
counter = 0
flag = False
for i in range(first_num, last_num + 1):
    for j in range(first_num, last_num + 1):
        sum_of_num = i + j
        counter += 1
        if sum_of_num == magic_num:
            flag = True
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            exit()

if not flag:
    print(f"{counter} combinations - neither equals {magic_num}")

