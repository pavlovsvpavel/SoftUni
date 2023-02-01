def data_types(string, string_2):
    if string == "int":
        string_2 = int(string_2)
        result = string_2 * 2
        return result
    elif string == "real":
        string_2 = float(string_2)
        result = string_2 * 1.5
        return f"{result:.2f}"
    elif string == "string":
        return f"${string_2}$"


user_input = input()
user_input_2 = input()
print(data_types(user_input, user_input_2))
