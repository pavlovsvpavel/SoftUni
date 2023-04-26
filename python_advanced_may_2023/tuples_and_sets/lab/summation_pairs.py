numbers = [int(x) for x in input().split(" ")]
target = int(input())

my_dict = {}

for num in numbers:
    if num not in my_dict:
        my_dict[num] = 0

    my_dict[num] += 1

for number, occurrences in my_dict.items():
    if occurrences > 0:
        needed_number = target - number
        if needed_number in my_dict.keys():
            print(f"{number} + {needed_number} = {target}")
            my_dict[number] -= 1
            my_dict[needed_number] -= 1


