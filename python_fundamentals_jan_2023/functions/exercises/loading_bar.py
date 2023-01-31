def loading_bar(number):
    loading_list = []
    total_progress_bar = 10
    current_progress = number // 10

    for i in range(current_progress):
        loading_list.append("%")
    for k in range(total_progress_bar - current_progress):
        loading_list.append(".")
    result = "".join(loading_list)
    if current_progress == total_progress_bar:
        return f"{number}% Complete!\n[{result}]"
    else:
        return f"{number}% [{result}]\nStill loading..."


integer = int(input())
print(loading_bar(integer))
