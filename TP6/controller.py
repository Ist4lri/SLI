from vue1 import Application
from model import Model


class Controller():
    def __init__(self):

        self.reading_file()
        self.view = Application(self)
        self.lb_display()
        self.view.view_window()

    def reading_file(self):
        self.model = Model("a.txt")
        self.model.read_file()

    def lb_display(self):
        for key in self.model.dico_animaux.keys():
            self.view.display_lb(self.model.dico_animaux[key])

    def to_modify(self, key_dict):
        print("Nike yoi")

    def to_delete(self, key_dict):
        del self.model.dico_animaux[key_dict]
        self.view.resett_app()
        self.view.initiate_widgets()
        self.lb_display()

    def add_animal(self, dict_animal):
        self.view.counter = 0
        self.model.save(dict_animal)
        self.view.refresh()
        self.model.close()
        self.reading_file()
        self.lb_display()

    def get_model_entries(self):
        return self.model.get_attributes()

    def quit_window(self):
        print("close app")
        self.model.close()
        self.view.destroy()


if __name__ == "__main__":
    C = Controller()
