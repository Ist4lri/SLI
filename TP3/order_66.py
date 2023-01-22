# coding:utf-8
"""How to make a Zoo in POO ?"""


class Animal():
    def __init__(self, species, generation=1) -> None:
        self.species = species
        self.generation = generation
        self.age = 358
        self.children = {}

    def __str__(self) -> str:
        return f'{[self.children[i] for i in range(len(self.children))]}'

    def __repr__(self) -> str:
        return "Espèce {}, enfant ayant l'id suivant : {}, la mère étant : {}".format(self.species, self.generation, "coucou")

    def make_a_children(self, species, new_generation) -> None:
        if species.upper() != self.species.upper():
            print("Not the same species, check this out first.")
        if self.children[new_generation]:
            print("ici")
        else:
            self.children[new_generation] = Animal(species, new_generation)


if __name__ == "__main__":
    Chat = Animal("Chat")
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 4)
    Chat.make_a_children("Chat", 5)

    print(Chat)
