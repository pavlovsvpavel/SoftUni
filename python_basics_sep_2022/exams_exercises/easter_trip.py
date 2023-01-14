destination = input()
dates = input()
nights_count = int(input())

trip_price = 0

if destination == "France" and dates == "21-23":
    trip_price = nights_count * 30
elif destination == "France" and dates == "24-27":
    trip_price = nights_count * 35
elif destination == "France" and dates == "28-31":
    trip_price = nights_count * 40

if destination == "Italy" and dates == "21-23":
    trip_price = nights_count * 28
elif destination == "Italy" and dates == "24-27":
    trip_price = nights_count * 32
elif destination == "Italy" and dates == "28-31":
    trip_price = nights_count * 39

if destination == "Germany" and dates == "21-23":
    trip_price = nights_count * 32
elif destination == "Germany" and dates == "24-27":
    trip_price = nights_count * 37
elif destination == "Germany" and dates == "28-31":
    trip_price = nights_count * 43

print(f"Easter trip to {destination} : {trip_price:.2f} leva.")
