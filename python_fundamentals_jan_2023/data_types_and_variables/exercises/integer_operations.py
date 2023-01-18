my_list = []
count_numbers = 4

for i in range(count_numbers):
    num = int(input())
    my_list.append(num)

result = (my_list[0] + my_list[1]) // my_list[2] * my_list[3]

print(f"{result:.0f}")
