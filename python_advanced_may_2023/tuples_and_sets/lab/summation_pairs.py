from timeit import default_timer as timer

numbers = [int(x) for x in input().split(" ")]
target = int(input())

start = timer()
my_dict = {}
for num in numbers:
    if num not in my_dict:
        my_dict[num] = 0

    my_dict[num] += 1

for number, occurrences in my_dict.items():
    for _ in range(occurrences):
        needed_number = target - number
        my_dict[number] -= 1
        if needed_number in my_dict.keys() and my_dict[needed_number] > 0:
            print(f"{number} + {needed_number} = {target}")
            my_dict[needed_number] -= 1

end = timer()
diff = end - start
print(f"Time range: {diff:.2f}")


# numbers = [int(x) for x in input().split(" ")]
# target = int(input())
#
# start = timer()
# targets = set()
# values_map = {}
# for value in numbers:
#     if value in targets:
#         targets.remove(value)
#         pair = values_map[value]
#         del values_map[value]
#         print(f"{pair} + {value} = {target}")
#     else:
#         resulting_number = target - value
#         targets.add(resulting_number)
#         values_map[resulting_number] = value
#
# end = timer()
# diff = end - start
# print(f"Time range: {diff:.2f}")
