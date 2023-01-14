destination = input()


while destination != "End":
    total_amount = 0
    budget = float(input())
    while True:

        amount = float(input())
        total_amount += amount

        if total_amount >= budget:
            print(f"Going to {destination}!")
            destination = input()
            break




