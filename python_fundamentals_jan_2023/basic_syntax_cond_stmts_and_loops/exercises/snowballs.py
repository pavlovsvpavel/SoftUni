from sys import maxsize
count_snowballs = int(input())

value_snowball = 0
highest_value = - maxsize
highest_weight = 0
highest_time = 0
highest_quality = 0

for i in range(count_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value_snowball = int((weight / time) ** quality)
    if value_snowball > highest_value:
        highest_value = value_snowball
        highest_weight = weight
        highest_time = time
        highest_quality = quality

print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")
