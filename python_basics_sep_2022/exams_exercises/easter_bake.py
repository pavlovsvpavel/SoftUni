from math import ceil
from sys import maxsize
easter_breads = int(input())

sugar_total = 0
flour_total = 0

max_sugar = - maxsize
max_flour = - maxsize

for i in range(1, easter_breads + 1):
    sugar = int(input())
    flour = int(input())
    sugar_total += sugar
    flour_total += flour
    if sugar >= max_sugar:
        max_sugar = sugar
    if flour >= max_flour:
        max_flour = flour

packets_sugar = ceil(sugar_total / 950)
packets_flour = ceil(flour_total / 750)

print(f"Sugar: {packets_sugar}")
print(f"Flour: {packets_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")


