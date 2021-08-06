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
        self.menu_image = ImageTk.PhotoImage(file='money.jpg')
        self.show_amount_image = ImageTk.PhotoImage(file='money_bag.jpg')
        self.edit_amount_image = ImageTk.PhotoImage(file='money_roll.jpg')
        self.create_expense_image = ImageTk.PhotoImage(file='dollar_bill.jpg')
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
        self.quit_button(frame=self)

    def create_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Please enter an expense to create:').pack(side=TOP, fill=X)
        Label(frame, image=self.create_expense_image).pack(side=TOP)
        create_text = StringVar()
        Entry(frame, textvariable=create_text).pack(side=TOP)
        Button(frame, text='Add Amount', command=lambda: self.add_amount(frame, create_text)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.add_amount(frame, create_text))        
        
        
    def add_amount(self, frame, create_text):
        Label(frame, text='Please enter amount').pack(side=TOP)
        add_amount_text = StringVar()
        Entry(frame, textvariable=add_amount_text).pack(side=TOP)
        Button(frame, text='Add Frequency', command=lambda: self.expense_frequency_calc(frame, create_text, add_amount_text)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.expense_frequency_calc(frame, create_text, add_amount_text))        

    def expense_frequency_calc(self, frame, create_text, add_amount_text):
        Label(frame, text='Please select expense frequency').pack(side=TOP)
        freq_value = IntVar()
        for freq, value in self.expense_frequency.items():
            Radiobutton(frame, text=freq, variable=freq_value, value=value).pack(side=TOP)
        Button(frame, text='Save', command=lambda: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value))        
        self.back_button(frame)
        self.quit_button(frame)

    def calculate_yearly_expense(self, frame, create_text, add_amount_text, freq_value):
        frame.destroy()
        expense_amount = int(add_amount_text.get()) * freq_value.get()
        self.yearly_expense_dict[create_text.get().capitalize()] = expense_amount
        print(self.yearly_expense_dict)
        

    def show_expenses(self):
        frame = Toplevel()
        frame.grab_set()
        Label(frame, text='Total Yearly Expenses').pack(side=TOP)
        Label(frame, image=self.show_amount_image).pack(side=TOP)
        for key, value in self.yearly_expense_dict.items():
            Label(frame, text=f'{key}: ${value}').pack(side=LEFT, fill=X)
        self.back_button(frame)
        
    def edit_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Edit Expenses').pack(side=TOP)
        Label(frame, image=self.edit_amount_image).pack(side=TOP)
        selection = StringVar()
        for expense_type in self.yearly_expense_dict:
            Radiobutton(frame, text=expense_type, variable=selection, value=expense_type).pack(side=TOP)
        Button(frame, text='Edit Expense', command=lambda: self.add_amount(frame, selection)).pack(anchor=SE)
        self.back_button(frame)

    def delete_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()

    def quit_button(self, frame):
        Button(frame, text='Quit', command=self.quit).pack(anchor=SE)

    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).pack(anchor=SE)


if __name__ == '__main__':
    root = Tk()
    root.title('Budget App')
    app = BudgetGui(root)
    app.mainloop()
