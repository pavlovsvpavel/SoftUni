a = int(input())
b = int(input())
max_passwords = int(input())

counter = 0

for index1 in range(35, 55):
    for index2 in range(64, 96):
        for index3 in range(1, a + 1):
            for index4 in range(1, b + 1):
                counter += 1
                if counter > max_passwords:
                    exit()
                print(f"{chr(index1)}{chr(index2)}{index3}{index4}{chr(index2)}{chr(index1)}", end="|")
                if index3 == a and index4 == b:
                    exit()
                index1 += 1
                if index1 > 55:
                    index1 = 35
                index2 += 1
                if index2 > 96:
                    index2 = 64
