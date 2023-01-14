animal_name = input()
animal_type = 0

if animal_name in ["dog"]:
    animal_type = "mammal"
elif animal_name in ["crocodile", "tortoise", "snake"]:
    animal_type = "reptile"
else:
    animal_type = "unknown"

print(animal_type)
