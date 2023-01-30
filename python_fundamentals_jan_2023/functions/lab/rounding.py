def numbers_rounding(num):
    return round(num)


user_list = list(map(float, input().split(" ")))
result = []
for i in user_list:
    result.append(numbers_rounding(i))

print(result)


