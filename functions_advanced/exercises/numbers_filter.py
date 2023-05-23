def even_odd_filter(**kwargs):
    my_dict = {}

    for key, values in kwargs.items():
        if key == "even":
            my_dict[key] = list(filter(lambda x: x % 2 == 0, values))
        else:
            my_dict[key] = list(filter(lambda x: x % 2 != 0, values))

    return dict(sorted(my_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

