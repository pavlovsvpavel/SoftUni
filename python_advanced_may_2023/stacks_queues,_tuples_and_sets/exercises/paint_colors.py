from collections import deque


def check_for_sec_colors(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    if len(set1.intersection(set2)) == 2:
        return True
    return False


data = deque(input().split(" "))
all_colors = "red", "yellow", "blue", "orange", "purple", "green"
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}
found_colors = []
while data:
    if len(data) == 1:
        left_color = data.pop()
        if left_color in all_colors:
            found_colors.append(left_color)
        continue
    first, last = data.popleft(), data.pop()
    if first + last in all_colors:
        found_colors.append(first + last)
    elif last + first in all_colors:
        found_colors.append(last + first)
    else:
        first, last = first[:-1], last[:-1]
        middle = len(data) // 2
        if first != "":
            data.insert(middle, first)
        if last != "":
            data.insert(middle, last)

for color in found_colors:
    if color in secondary_colors.keys() and not check_for_sec_colors(found_colors, secondary_colors[color]):
        found_colors.remove(color)

print(found_colors)
