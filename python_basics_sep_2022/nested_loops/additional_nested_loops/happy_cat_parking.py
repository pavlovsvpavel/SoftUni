days = int(input())
hours_per_day = int(input())
tax_1 = 2.50
tax_2 = 1.25
tax_3 = 1
total_tax = 0
tax_per_day = 0
for count_day in range(1, days + 1):
    for count_hour in range(1, hours_per_day + 1):
        if count_day % 2 == 0:
            if count_hour % 2 != 0:
                tax_per_day += tax_1
            else:
                tax_per_day += tax_3

        elif count_day % 2 != 0:
            if count_hour % 2 == 0:
                tax_per_day += tax_2
            else:
                tax_per_day += tax_3

    print(f"Day: {count_day} - {tax_per_day:.2f} leva")

    total_tax += tax_per_day
    tax_per_day = 0

print(f"Total: {total_tax:.2f} leva")
