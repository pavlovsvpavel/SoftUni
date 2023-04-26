def check_indexes(first_start, second_start, first_end, second_end):
    intersection = []
    if first_start <= second_start:
        intersection.append(second_start)
    else:
        intersection.append(first_start)

    if first_end >= second_end:
        intersection.append(second_end)
    else:
        intersection.append(first_end)

    return intersection


n = int(input())
all_intersections = {}
for _ in range(n):
    first, second = input().split("-")

    first_intersection = [int(x) for x in first.split(",")]
    second_intersection = [int(x) for x in second.split(",")]

    current_intersection = check_indexes(first_intersection[0], second_intersection[0],
                                         first_intersection[1], second_intersection[1])

    start = current_intersection[0]
    end = current_intersection[1]
    result = []
    for num in range(start, end + 1):
        result.append(num)

    length = len(result)
    if length in all_intersections:
        continue
    else:
        all_intersections[length] = result

longest_intersection = max(all_intersections.keys())
print(f"Longest intersection is "
      f"{all_intersections[longest_intersection]} with length "
      f"{longest_intersection}")
