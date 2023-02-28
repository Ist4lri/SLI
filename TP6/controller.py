"""All the controller of the app, wich means to excahnge with different part of the app"""

from vue import Application
from model import Model


class Controller():
    """Controller class"""

    def __init__(self):
        """Init of the Controller"""
        self.model = Model("a.txt", "r+")
        self.model.read_file()
        self.view = Application(self)
        self.lb_display()
        self.view.view_window()

    def lb_display(self):
        """Access of the Dic, and Going to Display the List-Box"""
        for key in self.model.dico_animaux.keys():
            self.view.display_lb(self.model.dico_animaux[key])

    def to_modify_delete(self, mode, key_dict="", dict_animal={'data': 'value'}):
        """When we want to modify or delete an Entry"""
        if mode == "delete":
            del self.model.dico_animaux[key_dict]
            self.model.update_line_file(key_dict, "a.txt", 'delete')
        else:
            name_to_swap = dict_animal['name']
            if name_to_swap in self.model.dico_animaux:
                if self.model.dico_animaux[name_to_swap].species != dict_animal['species']:
                    self.model.dico_animaux[name_to_swap].species = dict_animal['species']
                if self.model.dico_animaux[name_to_swap].age != dict_animal['age']:
                    self.model.dico_animaux[name_to_swap].age = dict_animal['age']
                if self.model.dico_animaux[name_to_swap].foot != dict_animal['foot']:
                    self.model.dico_animaux[name_to_swap].foot = dict_animal['foot']
                if self.model.dico_animaux[name_to_swap].diet != dict_animal['diet']:
                    self.model.dico_animaux[name_to_swap].diet = dict_animal['diet']
                self.model.update_line_file(key_dict, "a.txt", 'modify')
            else:
                self.add_animal(dict_animal)
        self.model = Model("a.txt", "r+")
        self.model.read_file()
        self.view.resett_app()
        self.view.initiate_widgets()
        self.lb_display()

    def to_display(self, key_dict):
        """Display the Entry to be modified"""
        self.view.display_to_modify(self.model.dico_animaux[key_dict])

    def add_animal(self, dict_animal):
        """Adding an character to the file"""
        self.model.save(dict_animal)
        self.view.refresh()
        self.model.read_file()
        self.lb_display()

    def get_model_entries(self):
        """To have the different Attributes"""
        return self.model.get_attributes()

    def quit_window(self):
        """Bye Bye App"""
        print("close app")
        self.model.close()
        self.view.destroy()


if __name__ == "__main__":
    C = Controller()
