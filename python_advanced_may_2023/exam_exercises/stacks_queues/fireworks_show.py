from collections import deque


def check_for_fireworks_target(my_dict):
    for qty in my_dict.values():
        if qty < 3:
            return False

    return True


effects = deque(int(x) for x in input().split(", "))
power = deque(int(x) for x in input().split(", "))


fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

flag = False
while effects and power:

    current_effect = effects.popleft()
    current_power = power.pop()

    if current_effect <= 0:
        power.append(current_power)
        continue

    if current_power <= 0:
        effects.appendleft(current_effect)
        continue

    firework = current_effect + current_power

    if firework % 3 == 0 and firework % 5 != 0:
        fireworks["Palm Fireworks"] += 1

    elif firework % 5 == 0 and firework % 3 != 0:
        fireworks["Willow Fireworks"] += 1

    elif firework % 5 == 0 and firework % 3 == 0:
        fireworks["Crossette Fireworks"] += 1

    else:
        current_effect -= 1
        effects.append(current_effect)
        power.append(current_power)

    if check_for_fireworks_target(fireworks):
        flag = True
        break

if flag:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")

if power:
    print(f"Explosive Power left: {', '.join(map(str, power))}")

for k, v in fireworks.items():
    print(f"{k}: {v}")
