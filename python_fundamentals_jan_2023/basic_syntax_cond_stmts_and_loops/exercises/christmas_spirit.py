decorations_quantity = int(input())
days_to_christmas = int(input())
budget = 0
spirit_points = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

for i in range(1, days_to_christmas + 1):
    if i % 11 == 0:
        decorations_quantity += 2

    if i % 2 == 0:
        budget += ornament_set * decorations_quantity
        spirit_points += 5

    if i % 3 == 0:
        budget += tree_skirt * decorations_quantity + tree_garland * decorations_quantity
        spirit_points += 13

    if i % 5 == 0:
        budget += tree_lights * decorations_quantity
        spirit_points += 17
        if i % 3 == 0:
            spirit_points += 30

    if i % 10 == 0:
        spirit_points -= 20
        budget += tree_skirt + tree_garland + tree_lights


if days_to_christmas % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")

