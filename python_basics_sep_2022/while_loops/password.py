username = input()
password = input()

input_line = input()

while input_line != password:
    input_line = input()
print(f"Welcome {username}!")

