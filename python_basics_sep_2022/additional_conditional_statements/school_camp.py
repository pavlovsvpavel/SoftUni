season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())

sport = ""
price = 0

if season == "Winter" and group_type == "mixed":
    price = count_nights * 10 * count_students
    sport = "Ski"
if season == "Winter" and group_type in ["boys", "girls"]:
    price = count_nights * 9.60 * count_students
    if group_type == "boys":
        sport = "Judo"
    elif group_type == "girls":
        sport = "Gymnastics"
if season == "Spring" and group_type == "mixed":
    price = count_nights * 9.50 * count_students
    sport = "Cycling"
if season == "Spring" and group_type in ["boys", "girls"]:
    price = count_nights * 7.20 * count_students
    if group_type == "boys":
        sport = "Tennis"
    elif group_type == "girls":
        sport = "Athletics"
if season == "Summer" and group_type == "mixed":
    price = count_nights * 20 * count_students
    sport = "Swimming"
if season == "Summer" and group_type in ["boys", "girls"]:
    price = count_nights * 15 * count_students
    if group_type == "boys":
        sport = "Football"
    elif group_type == "girls":
        sport = "Volleyball"
if count_students >= 50:
    price = price * 0.50
elif 20 <= count_students < 50:
    price = price * 0.85
elif 10 <= count_students < 20:
    price = price * 0.95

print(f"{sport} {price:.2f} lv.")
