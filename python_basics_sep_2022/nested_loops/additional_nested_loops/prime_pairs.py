a = int(input())
b = int(input())
a_end = a + int(input())
b_end = b + int(input())

flag_1 = True
flag_2 = True

for pair_1 in range(a, a_end + 1):
    for pair_2 in range(b, b_end + 1):
        flag_1 = True
        flag_2 = True
        for i in range(2, (pair_1 // 2) + 1):
            if pair_1 % i == 0:
                flag_1 = False
                break
        for j in range(2, (pair_2 // 2) + 1):
            if pair_2 % j == 0:
                flag_2 = False
                break
        if flag_1 and flag_2:
            print(f"{pair_1}{pair_2}")


