from tkinter import *

class BudgetGui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.create_menu()
        self.button_dict = {
            'create': self.create_expense,
            'show': self.show_expenses,
            'edit': self.edit_expense,
            'delete': self.delete_expense
        }
        self.create_buttons()
        
    def create_menu(self):
        Label(self, text='Main Menu').pack(side=TOP)

    def show_expenses(self):
        pass

    def create_expense(self):
        pass

    def edit_expense(self):
        pass

    def delete_expense(self):
        pass

    def create_buttons(self):
        for button, func in self.button_dict.items():
            Button(self, text=button.capitalize(), command=func).pack(side=TOP)



if __name__ == '__main__':
    root = Tk()
    app = BudgetGui(root)
    app.mainloop()