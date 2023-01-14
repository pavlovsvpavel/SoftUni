import sys
divisor = int(input())
boundary_num = int(input())

max_number = -sys.maxsize

for i in range(1, boundary_num + 1):
    if i % divisor == 0:
        max_number = i
    else:
        continue

    if i > max_number:
        max_number = i

print(max_number)
