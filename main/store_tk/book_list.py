from tkinter import *


class BookList(Listbox):

    def __init__(self, db, master=None, cnf={}, **kw):
        self.db = db
        self.selected_tuple = ()
        super().__init__(master, cnf, **kw)

    def get_selected_row(self, event):
        index = self.curselection()[0]
        self.selected_tuple = self.get(index)
        self.master.load_entries_from_tuple(self.selected_tuple)

    def view_command(self):
        self.delete(0, END)
        for row in self.db.view():
            self.insert(END, row)

    def search_command(self):
        self.delete(0, END)
        for row in self.db.search(**self.master.get_entries_text()):
            self.insert(END, row)

    def add_command(self):
        id = self.db.insert(**self.master.get_entries_text())
        self.delete(0, END)
        self.insert(END, id, self.master.get_entries_text(False))

    def delete_command(self):
        self.db.delete(self.selected_tuple[0])

    def update_command(self):
        self.db.update(self.selected_tuple[0], **self.master.get_entries_text())
