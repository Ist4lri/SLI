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
        self.children = {
            1: f"{self.species},{generation}e generation, nommé {self.name}"}  # need initialisation

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

    def where_is_mommy(self, asking) -> None:
        """Asking who is ancestor of the asked animal"""
        if not self.children:  # Dic empty
            print(f"L'espèce {self.species} a besoin de se reproduire avant !")
        else:
            if isinstance(asking, float):
                print(
                    f'\nLe {self.species} numéros {asking} a pour ancêtre(s) :\n')
                if asking >= 1.01:
                    for key, value in self.children.items():
                        if asking > key >= 1:
                            print(
                                f'Ancêtre ID : {str(key)}, {value}')
                else:
                    print(f'Ancêtre {self.children[1.0]}')
            elif isinstance(asking, str):
                print(
                    f'\nLe {self.species} nommé {asking} a pour ancêtre(s) :\n')
                for key, value in self.children.items():
                    print(f'Enfant ID : {str(key)}, nom : {value}')
                    # The Value of the first entry of Dict is not a object ! Need to avoid it
                    if key != 1:
                        if asking.capitalize() in value.name:
                            break
            else:
                print("Please put a float or a string.")

    def where_is_charlie(self, asking) -> None:
        """Asking who is child of the asked animal"""
        if not self.children:
            print(
                f"L'espèce {self.species} a besoin de se reproduire avant !")
        else:
            if isinstance(asking, float):
                print(
                    f'\nLe {self.species} numéros {asking} a pour enfant(s) :\n')
                for key, value in self.children.items():
                    if key > asking:
                        print(f'Enfant ID : {str(key)}, nom : {value}')
            elif isinstance(asking, str):
                print(
                    f'\nLe {self.species} nommé {asking} a pour enfant(s) :\n')
                saved_id = 0
                for key, value in self.children.items():
                    # The Value of the first entry of Dict is not a object ! Need to avoid it
                    if key != 1:
                        if asking.capitalize() in value.name:
                            saved_id = key
                        # When the key is reached, print all animal that is after
                        elif saved_id != 0:
                            print(f'Enfant ID : {str(key)}, nom : {value}')
            else:
                print("Please put a float or a string.")


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
    Chat.where_is_mommy("Yumi")
    Chat.where_is_mommy(1.02)
    Chat.where_is_charlie(1.02)
    Chat.where_is_charlie("Yumi")
