budget = float(input())
season = input()

destination = ""
trip_price = 0
place = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip_price = budget * 0.3
        place = "Camp"
    elif season == "winter":
        trip_price = budget * 0.7
        place = "Hotel"
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        trip_price = budget * 0.4
        place = "Camp"
    elif season == "winter":
        trip_price = budget * 0.8
        place = "Hotel"
if budget > 1000:
    destination = "Europe"
    trip_price = budget * 0.9
    place = "Hotel"

print(f"Somewhere in {destination}\n{place} - {trip_price:.2f}")
