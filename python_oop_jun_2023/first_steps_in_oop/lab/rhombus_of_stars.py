def create_triangle(n):
    for row in range(n):
        print(f"{' ' * (n - 1 - row)}", end="")
        print(f"{'* ' * (row + 1)}")


def create_reversed_triangle(n):
    for row in range(n - 1, 0, - 1):
        print(f"{' ' * (n - row)}", end="")
        print(f"{'* ' * row}")


n = int(input())
create_triangle(n)
create_reversed_triangle(n)
