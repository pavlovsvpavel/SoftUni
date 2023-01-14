num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
sum_all_p = 0
for i in range(1, num + 1):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number <= 399:
        p2 += 1
    elif current_number <= 599:
        p3 += 1
    elif current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1
sum_all_p = p1 + p2 + p3 + p4 + p5
p1_result = p1 / sum_all_p * 100
p2_result = p2 / sum_all_p * 100
p3_result = p3 / sum_all_p * 100
p4_result = p4 / sum_all_p * 100
p5_result = p5 / sum_all_p * 100

print(f"{p1_result:.2f}%")
print(f"{p2_result:.2f}%")
print(f"{p3_result:.2f}%")
print(f"{p4_result:.2f}%")
print(f"{p5_result:.2f}%")
