data = input().split(" ")

reversed_data = []

for idx in range(len(data) - 1, - 1, - 1):
    reversed_data.append(data[idx])

print(" ".join(reversed_data))
