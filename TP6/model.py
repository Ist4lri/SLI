from Animal import Animal


class Model():
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "r+")
        self.dico_animaux = {}

    def read_file(self):
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0], tab[1], tab[2], tab[3], tab[4])
            self.dico_animaux[a.name] = a

    def save(self, dict_animal):
        self.file.write("\n"+dict_animal["species"]+","+dict_animal["age"]+"," +
                        dict_animal["diet"]+","+dict_animal["foot"]+","+dict_animal["name"])

    def close(self):
        self.file.close()

    def get_attributes(self) -> list:
        attr = []
        # get first key of the dict no mater what is it
        first_key = next(iter(self.dico_animaux))
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr


if __name__ == "__main__":
    model = Model("a.txt")
    model.read_file()
    model.close()
