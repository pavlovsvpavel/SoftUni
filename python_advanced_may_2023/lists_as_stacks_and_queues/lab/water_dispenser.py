from collections import deque

water_qty = int(input())
COMMAND_START = "Start"
COMMAND_REFILL = "refill"
COMMAND_END = "End"
queue = deque()
while True:
    name = input()
    if name == COMMAND_END:
        print(f"{water_qty} liters left")
        break
    elif name == COMMAND_START:
        while queue:
            command = input()
            if command.startswith(COMMAND_REFILL):
                command_args = command.split(" ")
                refill_qty = int(command_args[1])
                water_qty += refill_qty
            else:
                liters = int(command)
                if liters <= water_qty:
                    print(f"{queue.popleft()} got water")
                    water_qty -= liters
                else:
                    print(f"{queue.popleft()} must wait")
    else:
        queue.append(name)
