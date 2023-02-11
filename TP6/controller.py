from vue import Application
from model import Model

class Controller() :
    def __init__(self):

        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)

        self.view.view_window()

    def display(self, value):
        self.view.display_label(self.model.dico_animaux[value])

    def add_animal(self, dict_animal):
        self.model.save(dict_animal)

    def get_model_entries(self):
        return self.model.get_attributes()


    def quit_window(self):
        print("close app")
        self.model.close()
        self.view.destroy()

if __name__ == "__main__" :
    C = Controller()