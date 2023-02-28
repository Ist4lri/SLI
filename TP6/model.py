"""Model, for the file manipulation and updating"""

from Animal import Animal


class Model():
    """Model Class"""

    def __init__(self, filename, opening):
        """Init of the class"""
        self.filename = filename
        self.file = open(self.filename, f'{opening}', encoding='utf8')
        self.dico_animaux = {}

    def read_file(self):
        """Reading the file and to put all data in dic"""
        self.file.seek(0)
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            if tab != ['']:
                animal = Animal(tab[0], tab[1], tab[2], tab[3], tab[4])
                self.dico_animaux[animal.name] = animal

    def update_line_file(self, search, name, mode):
        """Delete OR modify the Entry in the file (Refreshing all)"""
        self.file.seek(0)
        if mode == 'delete':
            stock_of_line = []
            for line in self.file.readlines():
                stock_of_line.append(line)
            self.file.close()
            self.file = open(name, 'w', encoding='utf8')
            for line in stock_of_line:
                if search not in line:
                    self.file.write(line)
        if mode == 'modify':
            self.file.close()
            self.file = open(name, 'w', encoding='utf8')
            for value in self.dico_animaux.values():
                self.file.write(str(value))
                self.file.write("\n")
        self.file.close()

    def save(self, dict_animal):
        """Save the new Character in the file"""
        self.file.write(dict_animal["species"]+","+dict_animal["age"]+"," +
                        dict_animal["diet"]+","+dict_animal["foot"]+","+dict_animal["name"]+"\n")

    def close(self):
        """Close File"""
        self.file.close()

    def get_attributes(self) -> list:
        """Get All Attributes of the class"""
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr
