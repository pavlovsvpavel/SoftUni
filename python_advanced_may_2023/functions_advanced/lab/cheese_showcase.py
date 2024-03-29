def sorting_cheeses(**cheeses_dictionary):
    cheeses_dictionary = sorted(
        cheeses_dictionary.items(), key=lambda x: (-len(x[1]), x[0])
    )
    result = []
    for (cheese, quantities) in cheeses_dictionary:
        result.append(cheese)
        quantities = sorted(quantities, reverse=True)
        result.extend(quantities)

    return "\n".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print()
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
