def add_elements_to_set(my_set, element):
    my_set.add(element)
    return my_set


n, m = [int(x) for x in input().split(" ")]

set_1 = set()
set_2 = set()
for _ in range(n):
    add_elements_to_set(set_1, input())

for _ in range(m):
    add_elements_to_set(set_2, input())

unique_elements = set_1.intersection(set_2)

[print(element) for element in unique_elements]

