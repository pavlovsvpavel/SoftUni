width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
input_line = input()
boxes = 0
flag = False
while input_line != "Done":
    input_line = int(input_line)
    boxes += input_line

    if boxes >= total_space:
        break

    input_line = input()

    if input_line == "Done":
        flag = True
        break

diff = abs(boxes - total_space)
if flag:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")


