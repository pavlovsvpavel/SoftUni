from project.everland import Everland
from project.people.child import Child
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren

everland = Everland()

young_couple = YoungCouple("Johnsons", 150, 205)

child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

everland.add_room(young_couple)
everland.add_room(young_couple_with_children)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())


