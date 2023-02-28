"""Animal Class"""


class Animal():
    """Animal Class"""

    def __init__(self, species, age, diet, foot, name):
        """Init of the animal"""
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.name = name

    def __str__(self):
        """To Have a propoer display"""
        return self.species + ","+str(self.age) + ","+self.diet + ","+str(self.foot) + ","+self.name
