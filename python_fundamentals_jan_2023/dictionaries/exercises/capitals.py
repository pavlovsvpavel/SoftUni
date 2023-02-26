country = input().split(", ")
capital = input().split(", ")

dictionary = {key: value for key, value in zip(country, capital)}

for country, capital in dictionary.items():
    print(f"{country} -> {capital}")
