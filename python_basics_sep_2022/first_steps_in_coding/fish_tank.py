length = int(input())
width = int(input())
height = int(input())
percent_accessories = float(input())
tank_capacity = length * width * height
total_capacity_litres = tank_capacity / 1000
capacity_accessories = (total_capacity_litres * (percent_accessories/100))
capacity_without_accessories = (total_capacity_litres - capacity_accessories)
print(capacity_without_accessories)
