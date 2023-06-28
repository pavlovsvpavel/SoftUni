from project.blade_knight import BladeKnight
from project.elf import Elf
from project.hero import Hero
from project.wizard import Wizard

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print()
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
print()
blade_knight = BladeKnight("W", 45)
print(str(blade_knight))
print(blade_knight.__class__.__bases__[0].__name__)
print(blade_knight.username)
print(blade_knight.level)
