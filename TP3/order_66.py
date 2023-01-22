# coding:utf-8
"""How to make a Zoo in POO ?"""
from decimal import getcontext, Decimal


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
        else:
            if new_generation in self.children:
                max_float = max(self.children.keys())+0.01
                self.children[max_float] = Animal(
                    species, new_generation)
                print(f'Reproduction effectuée !')
            else:
                self.children[float(new_generation)] = Animal(
                    species, new_generation)
                print(f'Reproduction effectuée !')

    def where_is_mummy(self, asking_generation) -> None:
        if self.children == {}:
            print(f"L'espèce {self.species} a besoin de se reproduire avant !")
        else:
            if asking_generation >= 2.0:
                list_of_ancestor = []
                counter = 0
                getcontext().prec = 2
                temp_ask_generation = Decimal(asking_generation)
                while temp_ask_generation != 1:
                    if ((temp_ask_generation - Decimal(0.01)) in self.children):
                        counter += 1
                        getcontext().prec = 2
                        temp_ask_generation -= Decimal(0.01)

                print("out")
                while counter != 0:
                    list_of_ancestor.append(
                        self.children[asking_generation-0.01])
                    asking_generation -= 0.01
                    counter -= 1
                print(list_of_ancestor)
            else:
                print(f'Ancêtre {self.children[1.0]}')


if __name__ == "__main__":
    Chat = Animal("Chat")
    Chat.where_is_mummy(1.3)
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 2)
    Chat.make_a_children("Chat", 2)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.where_is_mummy(2.06)

    print(Chat.children)
