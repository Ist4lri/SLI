# coding:utf-8
"""How to make a Zoo in POO ?"""


class Animal():
    def __init__(self, species, generation=1) -> None:
        self.species = species
        self.generation = generation
        self.age = 358
        self.children = {}

    def __repr__(self) -> str:
        return "{}, {}e génération.".format(self.species, self.generation)

    def make_a_children(self, species, new_generation) -> None:
        if species.upper() != self.species.upper():
            print("Not the same species, check this out first.")
        if new_generation in self.children:
            max_float = max(self.children.keys())+0.01
            self.children[max_float] = Animal(
                species, new_generation)
            print(f'Reproduction effectuée !')
        else:
            self.children[float(new_generation)] = Animal(
                species, new_generation)
            print(f'Reproduction effectuée !')


if __name__ == "__main__":
    Chat = Animal("Chat")
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 1)
    print(Chat.children)
