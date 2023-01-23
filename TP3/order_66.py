# coding:utf-8
"""How to make a Zoo in POO ?"""
from decimal import getcontext, Decimal


class Animal():
    """Animal class, to do the homework"""

    def __init__(self, species, name, generation=1) -> None:
        """Class initiation with Species, Generation, Children, and name"""
        self.species = species
        self.generation = generation
        self.name = name
        self.children = {}

    def __repr__(self) -> str:
        """This is for transforming object into a string who describe it."""
        return f"{self.species}, {self.generation}e génération, nommé {self.name}"

    def make_a_children(self, species, name, new_generation) -> None:
        """It's not like in real life, but it's for reproduction of the animal"""
        if species.upper() != self.species.upper():
            print("Not the same species, check this out first.")
        else:
            if new_generation in self.children:
                getcontext().prec = 3
                max_float = Decimal(max(self.children.keys()))+Decimal(0.01)
                # Make a ID with 3 decimal.
                # To have more children than one...
                self.children[max_float] = Animal(
                    species, name, new_generation)
                print('Reproduction effectuée !')
            else:
                self.children[float(new_generation)] = Animal(
                    species, name, new_generation)
                print('Reproduction effectuée !')

    def where_is_mommy(self, asking_generation) -> None:
        """Asking who is ancestor of the asked animal"""
        if not self.children:
            print(f"L'espèce {self.species} a besoin de se reproduire avant !")
        else:
            print(
                f'\nLe {self.species} numéros {asking_generation} a pour ancêtre :\n')
            if asking_generation >= 2.0:
                for key, value in self.children.items():
                    if asking_generation > key >= 1:
                        print(
                            f'Ancêtre ID : {str(key)}, {value}')
            else:
                print(f'Ancêtre {self.children[1.0]}')

    def where_is_charlie(self, asking_generation) -> None:
        """Asking who is child of the asked animal"""
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
    Chat = Animal("Chat", "Chaton")
    Chat.where_is_mommy(1.3)
    Chat.make_a_children("Chat", "Miaou", 1)
    Chat.make_a_children("Chat", "Yumi", 1)
    Chat.make_a_children("Chat", "Talion", 2)
    Chat.make_a_children("Chat", "Xerath", 2)
    Chat.make_a_children("Chat", "Thresh", 3)
    Chat.make_a_children("Chat", "Leona", 3)
    Chat.make_a_children("Chat", "Fizz", 3)
    Chat.make_a_children("Chat", "Veigar", 3)
    Chat.make_a_children("Chat", "Zed", 3)
    Chat.make_a_children("Chat", "Udyr", 3)
    Chat.make_a_children("Chat", "Lux", 3)
    Chat.where_is_mommy(2.01)
    Chat.where_is_charlie(2.01)
