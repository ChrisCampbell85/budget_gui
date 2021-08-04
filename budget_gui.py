from tkinter import *
from dataclasses import dataclass

@dataclass
class AppConfig:
    pass

class BudgetGui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.create_menu()

    def create_menu(self):
        Label(self, text='Main Menu').pack()

    def show_expenses(self):
        pass

    def create_expense(self):
        pass

    def edit_expense(self):
        pass

    def delete_expense(self):
        pass



if __name__ == '__main__':
    root = Tk()
    app = BudgetGui(root)
    app.mainloop()