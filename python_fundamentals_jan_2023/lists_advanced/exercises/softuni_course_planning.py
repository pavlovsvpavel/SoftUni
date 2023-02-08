def add(lst, title):
    if title not in lst:
        lst.insert(len(lst), title)
    return lst


def insert(lst, title, idx):
    if title not in lst:
        lst.insert(idx, title)
    return lst


def remove(lst, title):
    if title in lst:
        rem_index = lst.index(title)
        lst.remove(title)
    if f"Exercise-{title}" in lst:
        rem_index_exe = lst.index(f"Exercise-{title}")
        lst.remove(f"Exercise-{title}")
    return lst


def swap(lst, title_1, title_2):
    idx_1 = lst.index(title_1)
    idx_2 = lst.index(title_2)
    title_1_exe = f"{title_1}-Exercise"
    title_2_exe = f"{title_2}-Exercise"
    if title_1 in lst and title_2 in lst:
        lst[idx_1], lst[idx_2] = lst[idx_2], lst[idx_1]
    if title_1_exe in lst:
        rem_index_exe = lst.index(f"{title_1}-Exercise")
        element = lst.pop(rem_index_exe)
        new_idx_1 = lst.index(title_1)
        lst.insert(new_idx_1 + 1, title_1_exe)
        # lst[rem_index_exe], lst[idx_1] = lst[idx_1], lst[rem_index_exe]
    if title_2_exe in lst:
        rem_index_exe = lst.index(f"{title_2}-Exercise")
        element = lst.pop(rem_index_exe)
        new_idx_2 = lst.index(title_2)
        lst.insert(new_idx_2 + 1, title_2_exe)
        # lst[rem_index_exe], lst[idx_2] = lst[idx_2], lst[rem_index_exe]
    return lst


def add_exe(lst, title, exe_title):
    if title not in lst:
        lst.insert(len(lst), title)
    title_idx = lst.index(title)
    if title in lst and exe_title not in lst:
        lst.insert(title_idx + 1, exe_title)
    return lst


lessons = input().split(", ")

while True:
    command_list = input().split(":")
    current_command = command_list[0]
    if current_command == "course start":
        break

    if current_command == "Add":
        lesson_title = command_list[1]
        add(lessons, lesson_title)
    elif current_command == "Insert":
        lesson_title = command_list[1]
        index = int(command_list[2])
        insert(lessons, lesson_title, index)
    elif current_command == "Remove":
        lesson_title = command_list[1]
        remove(lessons, lesson_title)
    elif current_command == "Swap":
        lesson_title_1 = command_list[1]
        lesson_title_2 = command_list[2]
        swap(lessons, lesson_title_1, lesson_title_2)
    elif current_command == "Exercise":
        lesson_title = command_list[1]
        exercise_title = f"{lesson_title}-Exercise"
        add_exe(lessons, lesson_title, exercise_title)

[print(f"{i}.{lessons[i - 1]}") for i in range(1, len(lessons) + 1)]



