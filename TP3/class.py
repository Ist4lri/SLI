# coding:utf-8

class Animal():
    def __init__(self, species, age, diet) -> None:
        self.species = species
        self.age = age
        self.diet = diet

    def set_name(self, name):
        self.name = name

    def set_foot_number(self, number):
        self.foot_number = number

    def __str__(self) -> str:
        return f"{self.species}, qui a {self.age} an, et il est {self.diet}"


class Chat(Animal):
    def __init__(self, age, cute) -> None:
        super().__init__("Chat", age, "Carnivore")
        self.cute = cute

    def __str__(self) -> str:
        return super().__str__() + f' Un {self.species} est toujours cute, surtout si il est jeune et lui a {self.age} ans, Baka'


class Serpent(Animal):
    def set_name(self, name):
        self.name = name

    def set_foot_number(self, number):
        self.foot_number = 0


if __name__ == "__main__":
    chat = Chat(5, True)
    chat.set_name("Robin")
    homme = Animal("Homme", 35, "Omnivore")
    snake = Serpent("Serpent", 4, "carnivore")
    snake.set_foot_number(0)

    print(chat)
    print(homme)
    print(snake)
