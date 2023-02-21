class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, names):
        if species == "mammal":
            self.mammals.append(names)
        elif species == "fish":
            self.fishes.append(names)
        elif species == "bird":
            self.birds.append(names)

        zoo.__animals += 1

    def get_info(self, type_of_species):
        if type_of_species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif type_of_species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {self.__animals}"
        elif type_of_species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {self.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
count_animals = int(input())
for el in range(count_animals):
    species, names = input().split(" ")
    zoo.add_animal(species, names)

info_species = input()
print(zoo.get_info(info_species))
