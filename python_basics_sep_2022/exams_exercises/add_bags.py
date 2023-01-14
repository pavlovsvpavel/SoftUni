luggage_price_over_20_kg = float(input())
luggage_kg = float(input())
days_till_trip = int(input())
count_luggage = int(input())

luggage_price = 0

if luggage_kg < 10:
    luggage_price = luggage_price_over_20_kg * 0.2
    if days_till_trip > 30:
        luggage_price = luggage_price * 1.1
    elif 7 <= days_till_trip <= 30:
        luggage_price = luggage_price * 1.15
    else:
        luggage_price = luggage_price * 1.4
elif 10 <= luggage_kg <= 20:
    luggage_price = luggage_price_over_20_kg * 0.5
    if days_till_trip > 30:
        luggage_price = luggage_price * 1.1
    elif 7 <= days_till_trip <= 30:
        luggage_price = luggage_price * 1.15
    else:
        luggage_price = luggage_price * 1.4
elif luggage_kg > 20:
    luggage_price = luggage_price_over_20_kg
    if days_till_trip > 30:
        luggage_price = luggage_price * 1.1
    elif 7 <= days_till_trip <= 30:
        luggage_price = luggage_price * 1.15
    else:
        luggage_price = luggage_price * 1.4

total_price = luggage_price * count_luggage

print(f"The total price of bags is: {total_price:.2f} lv.")

