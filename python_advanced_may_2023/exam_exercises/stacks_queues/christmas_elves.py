from collections import deque

elves = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())

toys = 0
used_energy = 0
counter = 0

while elves and materials:
    current_elf = elves.popleft()
    current_material = materials[-1]

    if current_elf < 5:
        continue

    counter += 1
    needed_power = current_material
    created_toys = 0

    if current_elf >= needed_power:
        if counter % 3 == 0:
            needed_power *= 2
            if current_elf >= needed_power:
                created_toys += 1
            else:
                elves.append(current_elf * 2)
                continue

        created_toys += 1

        if counter % 5 == 0:
            toys -= created_toys
            current_elf -= 1

        materials.pop()
        toys += created_toys
        used_energy += needed_power
        elves.append(current_elf - needed_power + 1)

    else:
        elves.append(current_elf * 2)


print(f"Toys: {toys}")
print(f"Energy: {used_energy}")

if elves:
    print(f"Elves left: {', '.join(map(str, elves))}")

if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
