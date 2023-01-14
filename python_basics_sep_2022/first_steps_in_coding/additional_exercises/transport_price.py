trip_in_km = int(input())
day_type = input()
wrong_data = True

sum_for_trip = 0
sum_for_trip_taxi_day = 0.7 + (trip_in_km * 0.79)
sum_for_trip_taxi_night = 0.7 + (trip_in_km * 0.90)
sum_for_trip_bus = trip_in_km * 0.09
sum_for_trip_train = trip_in_km * 0.06

if trip_in_km < 20 and day_type == "day":
    sum_for_trip = sum_for_trip_taxi_day
elif trip_in_km < 20 and day_type == "night":
    sum_for_trip = sum_for_trip_taxi_night
elif 20 <= trip_in_km < 100:
    sum_for_trip = sum_for_trip_bus
elif trip_in_km >= 100:
    sum_for_trip = sum_for_trip_train

if day_type == "day" or day_type == "night":
    print(f"{sum_for_trip:.2f}")
else:
    print("Wrong data!")
    wrong_data = False
