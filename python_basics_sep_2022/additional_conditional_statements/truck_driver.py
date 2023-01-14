season = input()
km_per_month = float(input())

km_per_season = km_per_month * 4
salary = 0
if km_per_month <= 5000 and season in ["Spring", "Autumn"]:
    salary = km_per_season * 0.75
elif 5000 < km_per_month <= 10000 and season in ["Spring", "Autumn"]:
    salary = km_per_season * 0.95

if km_per_month <= 5000 and season == "Summer":
    salary = km_per_season * 0.90
elif 5000 < km_per_month <= 10000 and season == "Summer":
    salary = km_per_season * 1.10

if km_per_month <= 5000 and season == "Winter":
    salary = km_per_season * 1.05
elif 5000 < km_per_month <= 10000 and season == "Winter":
    salary = km_per_season * 1.25

if km_per_month > 10000:
    salary = km_per_season * 1.45

taxes = salary * 0.10

print(f"{salary - taxes:.2f}")

