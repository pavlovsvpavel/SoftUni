try:
    some_text = input()
    times = int(input())
    result = some_text * times
    print(result)

except ValueError:
    print("Variable times must be an integer")
