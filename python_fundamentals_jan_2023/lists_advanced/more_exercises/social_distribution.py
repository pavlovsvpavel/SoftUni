def difference_below_min_wealth(lst, wealth):
    total_diff = 0
    for element in lst:
        if element < wealth:
            total_diff += wealth - element
    return total_diff


def difference_above_min_wealth(lst, wealth):
    total_diff = 0
    for element in lst:
        if element > wealth:
            total_diff += element - wealth
    return total_diff


population = input().split(", ")
min_wealth = int(input())
population_lst = [int(x) for x in population]

for idx in range(len(population_lst)):
    current_num = population_lst[idx]
    if current_num < min_wealth:
        diff = min_wealth - current_num
        current_num += diff
        population_lst[idx] = current_num
        max_num_idx = population_lst.index(max(population_lst))
        population_lst[max_num_idx] -= diff

if difference_above_min_wealth(population_lst, min_wealth) >= difference_below_min_wealth(population_lst, min_wealth):
    print(population_lst)
else:
    print("No equal distribution possible")
