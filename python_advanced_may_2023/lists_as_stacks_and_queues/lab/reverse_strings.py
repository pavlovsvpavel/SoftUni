data = list(input())

my_stack = []

for i in range(len(data)):
    my_stack.append(data.pop())

print("".join(my_stack))
