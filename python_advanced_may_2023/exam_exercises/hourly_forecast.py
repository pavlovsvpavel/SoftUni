def forecast(*args):
    cities_dict = {}
    result = []

    for city, weather in args:
        position = 0

        if weather == "Sunny":
            position = 1

        elif weather == "Cloudy":
            position = 2

        elif weather == "Rainy":
            position = 3

        cities_dict[city] = weather, position

    for city_name, type_of_weather in sorted(cities_dict.items(), key=lambda x: (x[1][1], x[0])):
        result.append(f"{city_name} - {type_of_weather[0]}")

    return "\n".join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
