from tkinter import *

class BudgetGui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.button_dict = {
            'create': self.create_expense,
            'show': self.show_expenses,
            'edit': self.edit_expense,
            'delete': self.delete_expense
        }
        self.master = master
        self.pack()
        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        Label(self, text='Main Menu').pack(side=TOP)

# create generic toplevel window, use button dict to insert appropriate logic?
    def create_buttons(self):
        for button, func in self.button_dict.items():
            Button(self, text=button.capitalize(), command=lambda button=button, func=func: self.create_toplevel(button, func)).pack(side=TOP)

    def create_toplevel(self, button, func):
        frame = Toplevel(self)
        Label(frame, text=button.capitalize()).pack(side=TOP)
        func()

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
