town = input()
sales = float(input())

commission = 0

# if town != "Sofia" and town != "Plovdiv" and town != "Varna" or sales < 0:
#     print("error")
if town not in ["Sofia", "Plovdiv", "Varna"] or sales < 0:
    print("error")
elif town == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    print(f"{commission:.2f}")
elif town == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
    print(f"{commission:.2f}")
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    print(f"{commission:.2f}")
