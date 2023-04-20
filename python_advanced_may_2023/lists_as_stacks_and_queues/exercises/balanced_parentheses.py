sequence = input()

opening_brackets = ["{", "[", "("]
closing_brackets = ["}", "]", ")"]
brackets = []
flag = False

for el in sequence:
    if el in opening_brackets:
        brackets.append(el)
    if brackets:
        if el in closing_brackets:
            closing_index = closing_brackets.index(el)
            current_opening_bracket = brackets.pop()
            opening_index = opening_brackets.index(current_opening_bracket)
            if closing_index == opening_index:
                flag = True
            else:
                flag = False
                break
    else:
        flag = False
        break

if flag and not brackets:
    print("YES")
else:
    print("NO")
