def start_playing(object):
    return object.play()


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))
