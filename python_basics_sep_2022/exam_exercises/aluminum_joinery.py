count_joinery = int(input())
joinery_type = input()
delivery_type = input()

total_price = 0

if joinery_type == "90X130":
    total_price = count_joinery * 110
    if 30 < count_joinery <= 60:
        total_price = total_price * 0.95
    elif count_joinery > 60:
        total_price = total_price * 0.92

if joinery_type == "100X150":
    total_price = count_joinery * 140
    if 40 < count_joinery <= 80:
        total_price = total_price * 0.94
    elif count_joinery > 80:
        total_price = total_price * 0.90

if joinery_type == "130X180":
    total_price = count_joinery * 190
    if 20 < count_joinery <= 50:
        total_price = total_price * 0.93
    elif count_joinery > 50:
        total_price = total_price * 0.88

if joinery_type == "200X300":
    total_price = count_joinery * 250
    if 25 < count_joinery <= 50:
        total_price = total_price * 0.91
    elif count_joinery > 50:
        total_price = total_price * 0.86

if delivery_type == "With delivery":
    total_price = total_price + 60
else:
    total_price = total_price

if count_joinery > 99:
    total_price = total_price * 0.96

if count_joinery <= 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
