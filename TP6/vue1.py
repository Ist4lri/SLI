from tkinter import *
from tkinter.messagebox import showinfo


class Application(Tk):
    def __init__(self, controller) -> None:
        Tk.__init__(self)
        self.counter = 0
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.initiate_widgets()

    def initiate_widgets(self):
        self.list_box = Listbox(self)
        self.label_species = Label(
            self, text="Selectionnez l'individu souhaité")
        self.fill_lb = Button(self, text="Afficher")
        self.quit_button = Button(
            self, text="Quitter", command=self.quit_window)
        self.add = Button(self, text="Add", command=self.add_animal)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        self.label_species.pack()
        self.list_box.pack()
        self.fill_lb.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.add.pack()
        self.quit_button.pack()

    def refresh(self):
        for att in self.attributes:
            self.entries[att].delete(0, 'end')

    def display_something(self):
        self.controller.lb_display()

    def display_lb(self, value):
        self.counter += 1
        self.list_box.insert(
            self.counter, f"{value.name}, {value.species}")

    def quit_window(self):
        self.controller.quit_window()

    def add_animal(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
        self.controller.add_animal(dict_animal)
        showinfo(
            title="For your information", message="Entry was added to file successfully")
        self.refresh()

    def view_window(self):
        self.title("Ma Première App :-)")
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.view_window()
