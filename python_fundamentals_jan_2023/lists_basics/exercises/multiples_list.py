factor = int(input())
count = int(input())

my_list = []

for number in range(1, count + 1):
    number *= factor
    my_list.append(number)

print(my_list)
