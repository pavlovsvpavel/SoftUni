import re
count_line = int(input())

for _ in range(count_line):
    text = input()

    regex_name = r"@(?P<name>[A-Za-z]+)\|"
    regex_age = r"#(?P<age>\d+)\*"
    name = re.findall(regex_name, text)
    age = re.findall(regex_age, text)
    print(f"{name[0]} is {age[0]} years old.")
