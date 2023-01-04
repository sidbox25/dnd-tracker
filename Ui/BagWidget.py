import tkinter as tk
from .dataProvider import *
from .ItemWidget import ItemWidget

class BagWidget(tk.Frame):
    def __init__(self, master, text):
        super().__init__(master)
        self.master = master
        self.text = text
        self.freeRow = 1
        self.pack(side="left", anchor="n")
        self.create_widgets()
        self.list_of_items = []

    def create_widgets(self):
        self.title = tk.Label(self)
        self.title["text"] = self.text
        self.title["borderwidth"] = borderwidth
        self.title["relief"] = relief
        self.title["width"] = (width+width_small*2)+4
        self.title["height"] = height
        self.title.grid(row=0, columnspan=3)

    def create_item(self, name, quantity):
        self.list_of_items.append(ItemWidget(self, self.freeRow, name, quantity))
        self.freeRow += 1


