from tkinter import *
from PIL import ImageTk

class BudgetGui(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.button_dict = {
            'Create Expense': self.create_expense,
            'Show Expenses': self.show_expenses,
            'Edit Expenses': self.edit_expense,
            'Delete Expenses': self.delete_expense
        }
        self.expense_frequency = {
            'Daily': 365,
            'Weekly': 52,
            'Monthly': 12,
            'Yearly': 1
        }
        self.yearly_expense_dict = {}
        self.master = master
        self.menu_image = ImageTk.PhotoImage(file='C:\\Users\Chris\Documents\\VS_CODE_LEARNING\\BudgetApp\\money.jpg')
        self.pack()
        self.create_menu()
        self.create_buttons()

    def create_menu(self):
        Label(self, text='Budget App').pack(side=TOP, fill=BOTH)       
        Label(self, image=self.menu_image).pack()
        
        

# create buttons for root window from __init__ parameters
    def create_buttons(self):
        for button_name, func in self.button_dict.items():
            Button(self, text=button_name, command=func).pack(side=TOP, fill=X)

    def create_expense(self):
        frame = Toplevel()
        frame.focus()
        Label(frame, text='Please enter an expense to create:').pack(side=TOP, fill=X)
        create_text = StringVar()
        Entry(frame, textvariable=create_text).pack(side=TOP)
        Button(frame, text='Add Amount', command=lambda: self.add_amount(frame, create_text)).pack(anchor=SE)
        
    def add_amount(self, frame, create_text):
        Label(frame, text='Please enter amount').pack(side=TOP)
        print(create_text.get())
        add_amount_text = StringVar()
        Entry(frame, textvariable=add_amount_text).pack(side=TOP)
        Button(frame, text='Add Frequency', command=lambda: self.expense_frequency_calc(frame, create_text, add_amount_text)).pack(anchor=SE)

    def expense_frequency_calc(self, frame, create_text, add_amount_text):
        Label(frame, text='Please select expense frequency').pack(side=TOP)
        print(add_amount_text.get())
        freq_value = IntVar()
        for freq, value in self.expense_frequency.items():
            Radiobutton(frame, text=freq, variable=freq_value, value=value).pack(side=TOP)
        Button(frame, text='Save', command=lambda: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value)).pack(anchor=SE)
        

    def calculate_yearly_expense(self, frame, create_text, add_amount_text, freq_value):
        frame.destroy()
        expense_amount = int(add_amount_text.get()) * freq_value.get()
        self.yearly_expense_dict[create_text.get().capitalize()] = expense_amount
        print(self.yearly_expense_dict)
        

    def show_expenses(self):
        frame = Toplevel()
        for key, value in self.yearly_expense_dict.items():
            Label(frame, text=f'{key}: {value}').pack(side=TOP, fill=X)
        
    def edit_expense(self):
        frame = Toplevel()
        frame.focus()

    def delete_expense(self):
        frame = Toplevel()
        frame.focus()

    def quit_button(self):
        pass


if __name__ == '__main__':
    root = Tk()
    app = BudgetGui(root)
    app.mainloop()
