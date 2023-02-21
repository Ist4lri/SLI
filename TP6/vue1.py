from tkinter import *
from tkinter.messagebox import showinfo, showerror


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
        self.list_box.delete(0, 'end')
        for att in self.attributes:
            self.entries[att].delete(0, 'end')

    def resett_app(self):
        self.label_species.forget()
        self.list_box.forget()
        self.modify_b.forget()
        self.delete_b.forget()
        for att in self.attributes:
            self.entries_label[att].forget()
            self.entries[att].forget()
        self.add_b.forget()
        self.quit_b.forget()

    def display_lb(self, value):
        self.counter += 1
        self.list_box.insert(
            self.counter, f"{value.name}, {value.species}")

    def get_line(self, action):
        if not self.list_box.curselection():
            showerror(title="ERROR", message="Select a entity, please !")
        else:
            lb_index = self.list_box.curselection()
            string_result = self.list_box.get(lb_index)
            to_send = string_result.split(',')[0]
            if action == "modify":
                print(to_send)
            else:
                self.controller.to_delete(to_send)

    def quit_window(self):
        self.controller.quit_window()

    def add_animal(self):
        dict_animal = {}
        for key in self.entries:
            dict_animal[key] = self.entries[key].get()
        self.controller.add_animal(dict_animal)
        showinfo(
            title="For your information", message="Entry was added to file successfully")

    def view_window(self):
        self.title("Ma Première App :-)")
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.view_window()
