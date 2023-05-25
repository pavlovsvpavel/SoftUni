def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        for first_letter, age in kwargs.items():
            if name.startswith(first_letter):
                result.append(f"{name} is {age} years old.")

    return "\n".join(sorted(result, reverse=False))


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))