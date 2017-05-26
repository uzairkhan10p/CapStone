from backend import Database
from store_tk import *
from tkinter import *

class App:
    def __init__(self):
        self.database = Database("books.db")
        self.window = StoreTk("BookStore")
        self.books = BookList(self.database, self.window, height=6, width=35)

    def run(self):
        self.draw()

    def draw(self):
        self.draw_labels()
        self.draw_filters()
        self.draw_book_list()
        self.attach_list_scrollbar()
        self.draw_buttons()
        self.window.mainloop()

    def draw_labels(self):
        self.window.add_label("Title", 0, 0)
        self.window.add_label("Author", 0, 2)
        self.window.add_label("Year", 1, 0)
        self.window.add_label("ISBN", 1, 2)

    def draw_filters(self):
        self.window.add_entry("title", 0, 1)
        self.window.add_entry("author", 0, 3)
        self.window.add_entry("year", 1, 1)
        self.window.add_entry("isbn", 1, 3)

    def draw_book_list(self):
        self.books.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.books.bind('<<ListboxSelect>>', self.books.get_selected_row)

    def attach_list_scrollbar(self):
        sb1 = Scrollbar(self.window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.books.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.books.yview)

    def draw_buttons(self):
        self.window.add_button("View all", self.books.view_command, 2, 3)
        self.window.add_button("Search entry", self.books.search_command, 3, 3)
        self.window.add_button("Add entry", self.books.add_command, 4, 3)
        self.window.add_button("Update selected", self.books.update_command, 5, 3)
        self.window.add_button("Delete selected", self.books.delete_command, 6, 3)
        self.window.add_button("Close", self.window.destroy, 7, 3)


app = App()
app.run()