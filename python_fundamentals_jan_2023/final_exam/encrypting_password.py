import re

count_passwords = int(input())
for _ in range(count_passwords):
    password = input()

    pattern = r"(\S+)>([\d]{3,}\|[a-z]{3,}\|[A-Z]{3,}\|\S+)<\1"

    matches = re.findall(pattern, password)
    if matches:
        encrypted_password = matches[0][1]
        encrypted_password = encrypted_password.replace("|", "")
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")
