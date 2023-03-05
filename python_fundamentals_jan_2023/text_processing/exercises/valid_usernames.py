def check_username(user):
    flag = False
    length = len(user)
    allowed_characters = ["-", "_"]
    if 3 <= length <= 16:
        for char in user:
            if char in allowed_characters or char.isalpha() or char.isdigit():
                flag = True
            else:
                flag = False
                break
    return flag


usernames = input().split(", ")
for username in usernames:
    if check_username(username):
        print(username)
    else:
        continue
