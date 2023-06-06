from collections import deque

eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))

filled_boxes = 0
BAD_LUCK_EGG = 13
BOX_SIZE = 50

while eggs and papers:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    elif current_egg == BAD_LUCK_EGG:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()

    wrapped_egg = current_egg + current_paper

    if 0 < wrapped_egg <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")

else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")

if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")
