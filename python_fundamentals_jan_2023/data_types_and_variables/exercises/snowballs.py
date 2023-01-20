from sys import maxsize
count_snowballs = int(input())

value_snowball = 0
highest_value = - maxsize
best_result = []

for i in range(count_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value_snowball = int((weight / time) ** quality)
    if value_snowball > highest_value:
        highest_value = value_snowball
        best_result = f"{weight} : {time} = {highest_value} ({quality})"

print(best_result)
