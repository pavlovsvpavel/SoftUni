def difference_between(lst, wealth):
    diff = 0
    for element in lst:
        if element < wealth:
            diff += wealth - element
    return diff


def wealth_distribution(lst, wealth):
    result = []
    for el in lst:
        if el < wealth:
            el += wealth - el
            result.append(el)
        elif el == max(lst):
            el = lst[-1] - difference_between(population_lst, min_wealth)
            result.append(el)
        else:
            result.append(el)

    return result


population = input().split(", ")
min_wealth = int(input())
population_lst = [int(x) for x in population]

if difference_between(population_lst, min_wealth) + min_wealth <= max(population_lst):
    print(wealth_distribution(population_lst, min_wealth))
else:
    print("No equal distribution possible")
