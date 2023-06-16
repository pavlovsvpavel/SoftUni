def flights(*args):
    flights_dict = {}
    lst = []

    for el in args:
        lst.append(el)

    destination = ""
    for pos, element in enumerate(lst):
        if element == "Finish":
            break

        if pos % 2 == 0:
            if element not in flights_dict.keys():
                flights_dict[element] = 0

            destination = element

        else:
            flights_dict[destination] = flights_dict.get(destination, 0) + element

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
