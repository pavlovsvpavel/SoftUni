from collections import defaultdict


def start_spring(**kwargs):
    type_dict = defaultdict(list)
    result = []

    for spring_object, object_type in kwargs.items():
        type_dict[object_type].append(spring_object)

    for key, values in sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0], x[1])):
        result.append(f"{key}:")

        for value in sorted(values, reverse=False):
            result.append(f"-{value}")

    return "\n".join(result)


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower", }
# print(start_spring(**example_objects))


# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

