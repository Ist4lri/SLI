# coding:utf-8
"""How to make a Zoo in POO ?"""


class Animal():
    def __init__(self, species, age=0, location="Espace", sterile=False) -> None:
        self.species = species
        self.age = age
        self.location = location
        self.steril = sterile
        self.children = []

    def __str__(self) -> str:
        return f'This Animal is steril ? {self.steril}, How many children ? {self.children}'

    def make_a_children(self, species, sterile=False) -> None:
        self.children.append(Animal(species).species)


koala = Animal("koala")
koala.make_a_children("koala1")
print(koala)
