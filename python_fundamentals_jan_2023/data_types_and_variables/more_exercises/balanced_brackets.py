lines = int(input())

is_balanced = True
has_open_bracket = False

for _ in range(0, lines):
    user_input = input()

    if user_input != '(' and user_input != ')':
        continue

    is_open_bracket = user_input == '('

    if has_open_bracket == is_open_bracket:
        is_balanced = False
        break

    has_open_bracket = is_open_bracket

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

