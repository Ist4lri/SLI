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
        return f"{self.species}, {self.generation}e génération."

    def make_a_children(self, species, new_generation) -> None:
        if species.upper() != self.species.upper():
            print("Not the same species, check this out first.")
        else:
            if new_generation in self.children:
                getcontext().prec = 3
                max_float = Decimal(max(self.children.keys()))+Decimal(0.01)
                self.children[max_float] = Animal(
                    species, new_generation)
                print('Reproduction effectuée !')
            else:
                self.children[float(new_generation)] = Animal(
                    species, new_generation)
                print('Reproduction effectuée !')

    def where_is_mommy(self, asking_generation) -> None:
        if not self.children:
            print(f"L'espèce {self.species} a besoin de se reproduire avant !")
        else:
            print(
                f'\nLe {self.species} numéros {asking_generation} a pour ancêtre :\n')
            if asking_generation >= 2.0:
                for key, value in self.children.items():
                    if asking_generation > key >= 1:
                        print(f'Ancêtre ID : {str(key)}, nom : {value}')
            else:
                print(f'Ancêtre {self.children[1.0]}')

    def where_is_charlie(self, asking_generation) -> None:
        if not self.children:
            print(
                f"L'espèce {self.species} a besoin de se reproduire avant !")
        else:
            print(
                f'\nLe {self.species} numéros {asking_generation} a pour enfant :\n')
            for key, value in self.children.items():
                if key > asking_generation:
                    print(f'Enfant ID : {str(key)}, nom : {value}')


if __name__ == "__main__":
    Chat = Animal("Chat")
    Chat.where_is_mommy(1.3)
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 1)
    Chat.make_a_children("Chat", 2)
    Chat.make_a_children("Chat", 2)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.make_a_children("Chat", 3)
    Chat.where_is_mommy(2.01)
    Chat.where_is_charlie(2.01)
