lines = int(input())

counter = 0

for i in range(lines):
    user_input = input()

    if user_input == ")":
        counter -= 1
        break

    if user_input == "(":
        counter += 1

if counter == 0:
    print("BALANCED")
else:
    print("UNBALANCED")

