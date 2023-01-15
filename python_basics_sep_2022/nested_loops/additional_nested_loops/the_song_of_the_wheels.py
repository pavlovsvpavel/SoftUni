number = int(input())
counter = 0
unique_password = ""
current_password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and (a * b) + (c * d) == number:
                    current_password = str(f"{a}{b}{c}{d}")
                    counter += 1
                    print(current_password, end=" ")

                    if counter == 4:
                        unique_password = current_password
print()
if 0 <= counter < 4:
    print(f"No!")
else:
    print(f"Password: {unique_password}")
