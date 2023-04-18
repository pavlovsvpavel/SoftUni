n = int(input())
result = []
for el in range(n):
    command_args = [int(x) for x in input().split(" ")]
    command = command_args[0]
    if command == 1:
        number = command_args[1]
        result.append(number)
    if result:
        if command == 2:
            result.pop()
        elif command == 3:
            print(max(result))
        elif command == 4:
            print(min(result))

my_stack = []
for _ in range(len(result)):
    my_stack.append(result.pop())

print(*my_stack, sep=", ")
