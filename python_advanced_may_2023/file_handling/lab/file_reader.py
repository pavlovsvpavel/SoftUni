numbers = open("numbers.txt", "r")

nums = []
for num in numbers:
    nums.append(int(num))

print(sum(nums))
