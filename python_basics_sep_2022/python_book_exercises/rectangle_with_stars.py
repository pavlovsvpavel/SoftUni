n = int(input())

rows = n
print("%" * (2 * n))
if n % 2 == 0:
    rows -= 1

for i in range(1, rows + 1):
    print("%" + (" " * (n * 2 - 4) / 2) + (2 * "*") + "%" + (" " * (n * 2 - 4) / 2))

print("%" * (2 * n))