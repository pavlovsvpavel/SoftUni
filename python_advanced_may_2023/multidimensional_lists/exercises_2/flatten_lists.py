data = [x.split() for x in input().split("|")]

for row in range(len(data) - 1, - 1, - 1):
    for col in range(len(data[row])):
        current_el = data[row][col]
        print(current_el, end=" ")

