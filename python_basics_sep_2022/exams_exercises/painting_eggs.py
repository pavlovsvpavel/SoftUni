eggs_size = input()
color = input()
batches = int(input())

amount = 0

if eggs_size == "Large" and color == "Red":
    amount = batches * 16
elif eggs_size == "Large" and color == "Green":
    amount = batches * 12
elif eggs_size == "Large" and color == "Yellow":
    amount = batches * 9

if eggs_size == "Medium" and color == "Red":
    amount = batches * 13
elif eggs_size == "Medium" and color == "Green":
    amount = batches * 9
elif eggs_size == "Medium" and color == "Yellow":
    amount = batches * 7

if eggs_size == "Small" and color == "Red":
    amount = batches * 9
elif eggs_size == "Small" and color == "Green":
    amount = batches * 8
elif eggs_size == "Small" and color == "Yellow":
    amount = batches * 5

profit = amount * 0.65

print(f"{profit:.2f} leva.")
