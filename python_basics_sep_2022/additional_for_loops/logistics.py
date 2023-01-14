count_cargos = int(input())

price = 0
total_weight = 0
bus = 0
truck = 0
train = 0
for i in range(1, count_cargos + 1):
    cargo_weight = int(input())
    total_weight += cargo_weight
    if cargo_weight <= 3:
        price += cargo_weight * 200
        bus += cargo_weight
    elif cargo_weight <= 11:
        price += cargo_weight * 175
        truck += cargo_weight
    else:
        price += cargo_weight * 120
        train += cargo_weight

print(f"{price / total_weight:.2f}")
print(f"{bus / total_weight * 100:.2f}%")
print(f"{truck / total_weight * 100:.2f}%")
print(f"{train / total_weight * 100:.2f}%")
