hundreds_upper_num = int(input())
tens_upper_num = int(input())
ones_upper_num = int(input())

for idx_1 in range(1, hundreds_upper_num + 1):
    if idx_1 % 2 == 0:
        for idx_2 in range(2, tens_upper_num + 1):
            for i in range(2, int(idx_2 / 2) + 1):
                if idx_2 % i == 0:
                    break
            else:
                for idx_3 in range(1, ones_upper_num + 1):
                    if idx_3 % 2 == 0:
                        print(f"{idx_1} {idx_2} {idx_3}")
