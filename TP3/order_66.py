# coding:utf-8
"""How to make a Zoo in POO ?"""


class Animal():
    def __init__(self, species, generation=1) -> None:
        self.species = species
        self.generation = generation
        self.age = 358
        self.children = []

    def __str__(self) -> str:
        return f'{self.children}'

    def __repr__(self) -> str:
        return "Espèce {}, enfant ayant l'id suivant : {}, la mère étant : {}".format(self.species, self.generation, "coucou")

    def make_a_children(self, species, new_generation) -> None:
        if species.upper() != self.species.upper():
            print("Not the same species, check this out first.")
            return None
        if self.generation+1 != new_generation:
            print(
                f"Give a valid generation, actual generation is {self.genetation}")
            return None
        self.children.append(Animal(species, new_generation))
        self.children.append(Animal(species, new_generation+1))
        self.children.append(Animal(species, new_generation+2))


if __name__ == "__main__":
    koala = Animal("Koala")
    koala.make_a_children("Koala", 2)
    print(koala)
