from tkinter import *
from tkinter.messagebox import showinfo


class Application(Tk):
    def __init__(self, controller) -> None:
        Tk.__init__(self)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.initiate_widgets()

    def initiate_widgets(self):
        self.list_box = Label(self, text="")
        self.search_species = Label(self, text="Recherche")
        self.search_entry = Entry(self)
        self.fill_lb = Button(self, text="Afficher", command=self.fill_listBox)
        self.quit_button = Button(
            self, text="Quitter", command=self.quit_window)
        self.add = Button(self, text="Add", command=self.add_animal)
        self.entries = {}
        self.entries_label = {}
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)

        self.search_species.pack()
        self.search_entry.pack()
        self.fill_lb.pack()
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.add.pack()
        self.quit_button.pack()

    def refresh(self):
        for att in self.attributes:
            self.entries[att].delete(0, 'end')

    def fill_listBox(self):
        print("oui")

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
