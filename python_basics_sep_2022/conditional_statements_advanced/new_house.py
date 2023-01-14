type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

total_sum = 0

if type_of_flowers not in ["Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"]:
    print("error")

if type_of_flowers == "Roses":
    total_sum = flowers_count * 5
    if flowers_count > 80:
        total_sum = total_sum * 0.90
elif type_of_flowers == "Dahlias":
    total_sum = flowers_count * 3.8
    if flowers_count > 90:
        total_sum = total_sum * 0.85
elif type_of_flowers == "Tulips":
    total_sum = flowers_count * 2.80
    if flowers_count > 80:
        total_sum = total_sum * 0.85
elif type_of_flowers == "Narcissus":
    total_sum = flowers_count * 3
    if flowers_count < 120:
        total_sum = total_sum * 1.15
elif type_of_flowers == "Gladiolus":
    total_sum = flowers_count * 2.5
    if flowers_count < 80:
        total_sum = total_sum * 1.2

diff = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
