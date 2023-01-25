from sys import maxsize
my_list = [int(num) for num in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    smallest_num = maxsize

    for element in my_list:
        if element < smallest_num:
            smallest_num = element

    my_list.remove(smallest_num)

print(", ".join(map(str, my_list)))

