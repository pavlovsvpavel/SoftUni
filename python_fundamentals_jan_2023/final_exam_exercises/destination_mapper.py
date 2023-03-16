import re

places = input()
pattern = r"(\=|\/)(?P<place>[A-Z]{1}[A-Za-z]{2,})\1"

valid_places = re.finditer(pattern, places)
travel_points = 0
places_list = []
for place in valid_places:
    travel_points += len(place["place"])
    places_list.append(place["place"])

print(f'Destinations: {", ".join(places_list)}')
print(f"Travel Points: {travel_points}")
