from Animal import Animal


class Model():
    def __init__(self, filename, opening):
        self.filename = filename
        self.file = open(self.filename, f'{opening}')
        self.dico_animaux = {}

    def read_file(self):
        self.file.seek(0)
        for line in self.file:
            line = line.strip()
            tab = line.split(",")
            a = Animal(tab[0], tab[1], tab[2], tab[3], tab[4])
            self.dico_animaux[a.name] = a

    def check_line(self, search, mode):
        self.file.seek(0)
        stock_file = self.file.read()
        self.file.truncate()
        for line in stock_file:
            if search not in stock_file:
                if mode == "delete":
                    self.file.write(line)

        # Le code ici est bien pour faire du remplacement, quand il faut modifier les entry.
        # a trouver : Un moyen de supriomer ce qu'on veut pas.

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
