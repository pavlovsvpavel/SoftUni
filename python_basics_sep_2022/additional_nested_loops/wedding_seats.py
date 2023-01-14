last_sector = input()
count_rows = int(input())
odd_seats = int(input())
even_seats = odd_seats + 2
first_sector = "A"
first_sector = ord(first_sector)
last_sector = ord(last_sector)
first_row = "a"
first_row = ord(first_row)
counter = 0

for sector in range(first_sector, last_sector + 1):
    sector = chr(sector)
    for row in range(1, count_rows + 1):
        if row % 2 == 0:
            for seat in range(first_row, first_row + even_seats):
                seat = chr(seat)
                counter += 1
                print(f"{sector}{row}{seat}")
        else:
            for seat in range(first_row, first_row + odd_seats):
                seat = chr(seat)
                counter += 1
                print(f"{sector}{row}{seat}")

    count_rows += 1

print(counter)
