agency_name = input()
adult_tickets = int(input())
children_tickets = int(input())
price_adult = float(input())
tax = float(input())

price_children = price_adult * 0.3
tax_children = children_tickets * (price_children + tax)
tax_adult = adult_tickets * (price_adult + tax)
total_price = tax_adult + tax_children

price_with_tax = total_price * 0.2

print(f"The profit of your agency from {agency_name} tickets is {price_with_tax:.2f} lv.")

