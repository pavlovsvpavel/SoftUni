from collections import deque

COMMAND_PAID = "Paid"
COMMAND_END = "End"
queue = deque()
while True:
    name = input()
    if name == COMMAND_END:
        print(f"{len(queue)} people remaining.")
        break
    elif name == COMMAND_PAID:
        while queue:
            print(f"{queue.popleft()}")
    else:
        queue.append(name)

