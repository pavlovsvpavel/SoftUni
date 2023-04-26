n = int(input())

reservations_list = set()
for _ in range(n):
    reservations_list.add(input())

while True:
    visited_guest = input()
    if visited_guest == "END":
        break

    reservations_list.remove(visited_guest)

print(len(reservations_list))

for guest in sorted(reservations_list):
    print(guest)
