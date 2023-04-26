n = int(input())

unique_elements = set()
for _ in range(n):
    elements = input().split(" ")
    unique_elements.update(elements)

[print(el) for el in unique_elements]
