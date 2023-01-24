count_lines = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
my_list = []
filtered_list = []

for _ in range(count_lines):
    current_number = int(input())
    my_list.append(current_number)

command = input()

for i in my_list:
    filtered_passes = (
        (command == COMMAND_EVEN and i % 2 == 0) or
        (command == COMMAND_ODD and i % 2 != 0) or
        (command == COMMAND_NEGATIVE and i < 0) or
        (command == COMMAND_POSITIVE and i >= 0)
    )
    if filtered_passes:
        filtered_list.append(i)

print(filtered_list)
