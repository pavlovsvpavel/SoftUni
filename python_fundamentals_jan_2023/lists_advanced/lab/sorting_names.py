names = input()
names_list = names.split(", ")

sorted_names = sorted(names_list, key=lambda x: (-len(x), x))  # "-" sorting by descending order
print(sorted_names)
