"""The part of the code, to make the visual part of the app"""

from tkinter import Listbox, Button, Tk, Label, Entry
from tkinter.messagebox import showinfo, showerror


class Application(Tk):
    """The Application himself, the design of the App"""

    def __init__(self, controller) -> None:
        """ Init of the App class """
        Tk.__init__(self)
        self.counter = 0
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.initiate_widgets()

    def initiate_widgets(self):
        """Init of all Widget of the app"""
        self.list_box = Listbox(self)
        self.label_species = Label(
            self, text="Selectionnez l'individu souhaité")
        self.modify_b = Button(self, text="Modifier",
                               command=lambda: [self.get_line("modify")])
        self.delete_b = Button(self, text="Supprimer", command=lambda: [
                               self.get_line("delete")])
        self.add_b = Button(self, text="Add", command=self.add_animal)
        self.quit_b = Button(
            self, text="Quitter", command=self.quit_window)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        self.label_species.pack()
        self.list_box.pack()
        self.modify_b.pack()
        self.delete_b.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.add_b.pack()
        self.quit_b.pack()

    def refresh(self):
        """for refreshing after clicking on button"""
        self.list_box.delete(0, 'end')
        for att in self.attributes:
            self.entries[att].delete(0, 'end')
        self.add_b['text'] = "Add"

    def resett_app(self):
        """label erased after a click on "Add" Button"""
        self.label_species.forget()
        self.list_box.forget()
        self.modify_b.forget()
        self.delete_b.forget()
        for att in self.attributes:
            self.entries_label[att].forget()
            self.entries[att].forget()
        self.add_b.forget()
        self.quit_b.forget()

    def display_lb(self, animal_object):
        """To Display the List-box"""
        self.counter += 1
        self.list_box.insert(
            self.counter, f"{animal_object.name}, {animal_object.species}")

    def display_to_modify(self, animal_object):
        """Display on the entry textfield, to modify"""
        self.entries["species"].insert(0, animal_object.species)
        self.entries["name"].insert(0, animal_object.name)
        self.entries["age"].insert(0, animal_object.age)
        self.entries["diet"].insert(0, animal_object.diet)
        self.entries["foot"].insert(0, animal_object.foot)

    def get_line(self, action):
        """to get the selected character on list-box"""
        if not self.list_box.curselection():
            showerror(title="ERROR", message="Select a entity, please !")
        else:
            string_result = self.list_box.get(self.list_box.curselection())
            to_send = string_result.split(',')[0]
            if action == "modify":
                self.controller.to_display(to_send)
                self.add_b['text'] = "Update"
            else:
                self.controller.to_modify_delete('delete', key_dict=to_send)

    def quit_window(self):
        """Exit WIndow"""
        self.controller.quit_window()

    def add_animal(self):
        """When clicking on add animal (Or update) to add, or modify a character"""
        dict_animal = {}
        for single_entry in self.entries:
            dict_animal[single_entry] = self.entries[single_entry].get()
        if self.add_b['text'] == "Add":
            showinfo(
                title="For your information", message="Entry was added to file successfully")
            self.controller.add_animal(dict_animal)
        else:
            showinfo(
                title="For your information", message="Entry was modified successfully")
            self.controller.to_modify_delete('modify', dict_animal=dict_animal)

    def view_window(self):
        """Launch the Window"""
        self.title("LES PAGES JAUNES")
        self.mainloop()
