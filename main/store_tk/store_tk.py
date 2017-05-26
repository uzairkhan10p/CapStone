from collections import OrderedDict
from tkinter import *


class StoreTk(Tk):

    labels_index = 1
    buttons_index = 1
    entries = {}
    labels = {}
    buttons = {}

    def __init__(self, storeName, screenName=None, baseName=None, className='Tk',
                 useTk=1, sync=0, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.wm_title(storeName)
        self.entries = OrderedDict({})

    def add_label(self, text, row=0, column=0):
        self.labels[self.labels_index] = Label(self, text=text)
        self.labels[self.labels_index].grid(row=row, column=column)
        self.labels_index += 1

    def add_button(self, text, command=None, row=0, column=0, width=12):
        self.buttons[self.buttons_index] = Button(self, text=text, width=width, command=command)
        self.buttons[self.buttons_index].grid(row=row, column=column)
        self.buttons_index += 1

    def add_entry(self, name, row=0, column=0):
        self.entries[name] = {'text': StringVar()}
        self.entries[name]['box'] = Entry(self, textvariable=self.entries[name]['text'])
        self.entries[name]['box'].grid(row=row, column=column)

    def load_entries_from_tuple(self, selected_tuple):
        i = 1
        for entry in self.entries.values():
            entry['box'].delete(0, END)
            entry['box'].insert(END, selected_tuple[i])
            i += 1

    def get_entries_text(self, return_dict=True):
        if return_dict:
            return {name: entry['text'].get() for name, entry in self.entries.items()}
        else:
            return tuple(entry['text'].get() for name, entry in self.entries.items())
