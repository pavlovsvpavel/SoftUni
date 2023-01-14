h = int(input())
x = int(input())
y = int(input())

if (x > h or x == 0) and y > h:
    print("outside")

elif x == h or y == h or y == 0:
    print("border")

else:
    print("inside")



