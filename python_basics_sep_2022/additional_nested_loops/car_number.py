start_interval = int(input())
end_interval = int(input())

for n1 in range(start_interval, end_interval + 1):
    for n2 in range(start_interval, end_interval + 1):
        for n3 in range(start_interval, end_interval + 1):
            for n4 in range(start_interval, end_interval + 1):
                if n1 % 2 == 0 and n4 % 2 != 0 and n1 > n4 and (n2 + n3) % 2 == 0:
                    print(f"{n1}{n2}{n3}{n4}", end=" ")
                elif n1 % 2 != 0 and n4 % 2 == 0 and n1 > n4 and (n2 + n3) % 2 == 0:
                    print(f"{n1}{n2}{n3}{n4}", end=" ")
