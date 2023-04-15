from collections import deque

names = input().split(" ")
skips = int(input())
while len(names) > 1:
    names = deque(names)
    names.rotate(- skips)
    print(f"Removed {names.pop()}")

print(f"Last is {names[0]}")
