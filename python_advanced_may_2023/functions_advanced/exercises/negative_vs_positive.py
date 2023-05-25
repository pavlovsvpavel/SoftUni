def split_nums(nums):
    positive_nums = []
    negative_nums = []
    for num in nums:
        if num >= 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)

    return sum(positive_nums), sum(negative_nums)


numbers = [int(x) for x in input().split()]

positive_sum, negative_sum = split_nums(numbers)

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
