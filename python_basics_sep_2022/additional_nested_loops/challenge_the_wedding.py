men = int(input())
women = int(input())
tables = int(input())

counter = 0
for m in range(1, men + 1):
    if counter == tables:
        break

    for w in range(1, women + 1):
        counter += 1
        print(f"({m} <-> {w})", end=" ")

        if counter == tables:
            break

