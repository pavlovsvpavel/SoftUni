string = input()
needed_coffees = 0

while string != "END":

    if string.lower() not in ["dog", "cat", "coding", "movie"]:
        string = input()
        continue

    if string.isupper():
        needed_coffees += 1 * 2
    else:
        needed_coffees += 1

    string = input()

if needed_coffees > 5:
    print("You need extra sleep")
else:
    print(needed_coffees)
