count_strings = int(input())

for _ in range(count_strings):
    string_name = input()

    if "," in string_name or "." in string_name or "_" in string_name:
        print(f"{string_name} is not pure!")
    else:
        print(f"{string_name} is pure.")
