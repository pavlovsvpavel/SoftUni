def submissions_count(my_dict, lang):
    if lang not in my_dict.keys():
        my_dict[lang] = my_dict.get(lang, 0)
    my_dict[lang] += 1


exam_results = {}
submissions = {}
while True:
    data = input()

    if data == "exam finished":
        break

    data_args = data.split("-")
    user_name = data_args[0]
    language = data_args[1]

    if language == "banned":
        exam_results.pop(user_name)
        break

    points = int(data_args[2])
    submissions_count(submissions, language)
    if user_name not in exam_results.keys():
        exam_results[user_name] = exam_results.get(user_name, points)
    else:
        if exam_results[user_name] < points:
            exam_results[user_name] = points

print("Results:")
for user, points in exam_results.items():
    print(f"{user} | {points}")

print("Submissions:")
for language, submission in submissions.items():
    print(f"{language} - {submission}")

