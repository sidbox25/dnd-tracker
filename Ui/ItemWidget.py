import tkinter as tk
from .dataProvider import *


class ItemWidget(tk.Label):
    def __init__(self, master, row, name, quantity, ):
        super().__init__(master)
        self.row = row
        self.name = name
        self.quantity = quantity
        self.grid(row=row)
        self.text = tk.StringVar()
        self.__generate_text()
        self.create_widgets()

    def create_widgets(self):
        self.item = tk.Label(self.master)
        self.item["textvariable"] = self.text
        self.item["width"] = width
        self.item["height"] = height
        self.item.grid(row=self.row, column=0)

        self.add_item = tk.Button(self.master)
        self.add_item["text"] = "+"
        self.add_item["width"] = width_small
        self.add_item["height"] = height
        self.add_item["relief"] = relief
        self.add_item["command"] = self.__increase_quantity
        self.add_item.grid(row=self.row, column=1)

        self.minus_item = tk.Button(self.master)
        self.minus_item["text"] = "-"
        self.minus_item["width"] = width_small
        self.minus_item["height"] = height
        self.minus_item["relief"] = relief
        self.minus_item["command"] = self.__decrease_quantity
        self.minus_item.grid(row=self.row, column=2)

    def __increase_quantity(self):
        self.quantity += 1
        self.__generate_text()
        self.master.update()

    def __decrease_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            self.quantity = 0
        self.__generate_text()
        self.master.update()

    def __generate_text(self):
        self.text.set(str(self.quantity) + ": " + self.name)
