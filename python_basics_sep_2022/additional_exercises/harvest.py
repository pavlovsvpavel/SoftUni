from math import ceil
from math import floor
vineyard_area = int(input())
grape_kg_per_sqm = float(input())
needed_wine_lt = int(input())
workers = int(input())

total_grape_kg = vineyard_area * grape_kg_per_sqm
grape_for_wine_kg = total_grape_kg * 0.4
total_wine_lt = grape_for_wine_kg / 2.5

wine_for_workers = total_wine_lt - needed_wine_lt
wine_lt_per_worker = wine_for_workers / workers
diff = abs(needed_wine_lt - total_wine_lt)

if total_wine_lt < needed_wine_lt:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
elif total_wine_lt >= needed_wine_lt:
    print(f"Good harvest this year! Total wine: {floor(total_wine_lt)} liters."
          f"\n{ceil(diff)} liters left -> {ceil(wine_lt_per_worker)} liters per person.")
