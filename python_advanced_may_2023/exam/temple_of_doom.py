from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_tool * current_substance

    if result not in challenges:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1

        if current_substance == 0:
            continue

        substances.append(current_substance)

    else:
        challenges.remove(result)


if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substances:
    print(f"Substances: {', '.join(map(str, substances))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
