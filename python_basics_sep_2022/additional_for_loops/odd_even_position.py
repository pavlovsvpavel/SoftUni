import sys
count_numbers = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
count_odd = 0
even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize
count_even = 0
for i in range(1, count_numbers + 1):
    number = float(input())
    if i % 2 != 0:
        count_odd += 1
        odd_sum += number
        if number >= odd_max:
            odd_max = number
        elif number <= odd_min:
            odd_min = number
        if odd_min == sys.maxsize:
            odd_min = odd_max

    elif i % 2 == 0:
        even_sum += number
        count_even += 1
        if number >= even_max:
            even_max = number
        elif number <= even_min:
            even_min = number
        if even_min == sys.maxsize:
            even_min = even_max

print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == - sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == - sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")


# if count_odd == 0 and count_even == 0:
#     even_min = odd_min = "No"
#     even_max = odd_max = "No"
#     print(f"OddSum={odd_sum:.2f},")
#     print(f"OddMin={odd_min},")
#     print(f"OddMax={odd_max},")
#     print(f"EvenSum={even_sum:.2f},")
#     print(f"EvenMin={even_min},")
#     print(f"EvenMax={even_max}")
# elif count_even == 0:
#     even_min = "No"
#     even_max = "No"
#     print(f"OddSum={odd_sum:.2f},")
#     print(f"OddMin={odd_min:.2f},")
#     print(f"OddMax={odd_max:.2f},")
#     print(f"EvenSum={even_sum:.2f},")
#     print(f"EvenMin={even_min},")
#     print(f"EvenMax={even_max}")
#
# else:
#     print(f"OddSum={odd_sum:.2f},")
#     print(f"OddMin={odd_min:.2f},")
#     print(f"OddMax={odd_max:.2f},")
#     print(f"EvenSum={even_sum:.2f},")
#     print(f"EvenMin={even_min:.2f},")
#     print(f"EvenMax={even_max:.2f}")
