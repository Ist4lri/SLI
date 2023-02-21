from vue1 import Application
from model import Model


class Controller():
    def __init__(self):

        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.display_something()
        self.view.view_window()

    def lb_display(self):
        for key in self.model.dico_animaux.keys():
            self.view.display_lb(self.model.dico_animaux[key])

    def add_animal(self, dict_animal):
        self.model.save(dict_animal)

    def get_model_entries(self):
        return self.model.get_attributes()

    def quit_window(self):
        print("close app")
        self.model.close()
        self.view.destroy()


if __name__ == "__main__":
    C = Controller()
