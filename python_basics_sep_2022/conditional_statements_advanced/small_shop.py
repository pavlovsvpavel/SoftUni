product = input()
city = input()
quantity = float(input())
amount = 0

if city in ["Sofia", "Plovdiv", "Varna"] and product in ["coffee", "water", "beer", "sweets", "peanuts"]:
    if city == "Sofia":
        if product == "coffee":
            amount = quantity * 0.50
        elif product == "water":
            amount = quantity * 0.80
        elif product == "beer":
            amount = quantity * 1.20
        elif product == "sweets":
            amount = quantity * 1.45
        elif product == "peanuts":
            amount = quantity * 1.60

    elif city == "Plovdiv":
        if product == "coffee":
            amount = quantity * 0.40
        elif product == "water":
            amount = quantity * 0.70
        elif product == "beer":
            amount = quantity * 1.15
        elif product == "sweets":
            amount = quantity * 1.30
        elif product == "peanuts":
            amount = quantity * 1.50

    elif city == "Varna":
        if product == "coffee":
            amount = quantity * 0.45
        elif product == "water":
            amount = quantity * 0.70
        elif product == "beer":
            amount = quantity * 1.10
        elif product == "sweets":
            amount = quantity * 1.35
        elif product == "peanuts":
            amount = quantity * 1.55
    print(amount)
else:
    print("Wrong input!")


