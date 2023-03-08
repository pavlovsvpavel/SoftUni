main_string = input()
final_result = ""
result = ""
unique_symbols = []
number = ""
for pos, char in enumerate(main_string):
    if not char.isdigit():
        result += char.upper()
    elif char.isdigit():
        number += char
        if pos + 1 < len(main_string):
            if main_string[pos + 1].isdigit():
                continue

        final_result += result * int(number)
        result = ""
        number = ""

for el in final_result:
    if el not in unique_symbols:
        unique_symbols.append(el)

print(f"Unique symbols used: {len(unique_symbols)}")
print(final_result)
