from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from save_to_db import pickle_expenses, unpickle_expenses

# create export to csv function
# create income input and budgeting functionality i.e. desired savings, savings totals etc

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
        self.fonts = {'button': ('Devanagari MT', 15, 'bold'),
                        'title': ('Chalkboard SE', 20, 'bold'),
                        'regular': ('Copperplate Gothic Light', 15, 'bold')
        }
        self.yearly_expenses = {'Total': 0}
        self.master = master
        self.menu_image = ImageTk.PhotoImage(file='money.jpg')
        self.show_amount_image = ImageTk.PhotoImage(file='money_bag.jpg')
        self.edit_amount_image = ImageTk.PhotoImage(file='money_roll.jpg')
        self.create_expense_image = ImageTk.PhotoImage(file='dollar_bill.jpg')
        self.delete_expense_image = ImageTk.PhotoImage(file='burning_money.jpg')
        self.pack()
        self.create_menu('Budget App')
        self.create_buttons()

    def create_menu(self, name):
        Label(self, text=name, font=self.fonts['title']).pack(side=TOP, fill=BOTH)
        Label(self, image=self.menu_image).pack()
        Button(self, text='Open File', command=self.open_budget).pack(anchor=NE)
        Button(self, text='Save File', command=self.save_budget).pack(anchor=NE)
        

    def open_budget(self):
        filename = filedialog.askopenfilename()
        if filename:
            file_load = unpickle_expenses(filename)
            self.yearly_expenses = file_load

    def save_budget(self):
        frame = Toplevel()
        Label(frame, text='Type in filename').pack(side=TOP)
        ent_var = StringVar()
        Entry(frame, textvariable=ent_var).pack(side=TOP)
        Button(frame, text='Save', command=lambda: pickle_expenses(self.yearly_expenses, ent_var.get(), frame)).pack(anchor=SE)
        
# create buttons for root window from __init__ parameters
    def create_buttons(self):
        for button_name, func in self.button_dict.items():
            Button(self, text=button_name, font=self.fonts['button'], command=func).pack(side=TOP, fill=X)
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
            Radiobutton(frame, text=freq, variable=freq_value, value=value).pack(side=TOP, fill=Y)
        Button(frame, text='Save', command=lambda: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value))        
        self.back_button(frame)
        self.quit_button(frame)

    def calculate_yearly_expense(self, frame, create_text, add_amount_text, freq_value):
        frame.destroy()
        expense_amount = int(add_amount_text.get()) * freq_value.get()
        self.yearly_expenses[create_text.get().capitalize()] = expense_amount
        

    def show_expenses(self):
        frame = Toplevel()
        frame.grab_set()
        Label(frame, text='Total Yearly Expenses', font=self.fonts['title']).pack(side=TOP)
        Label(frame, image=self.show_amount_image).pack(side=TOP)
        for key, value in self.yearly_expenses.items():
            Label(frame, text=f'{key}: ${value}', font=self.fonts['regular']).pack(side=TOP, fill=X, padx=10)
        self.back_button(frame)
        
    def edit_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Edit Expenses').pack(side=TOP)
        Label(frame, image=self.edit_amount_image).pack(side=TOP)
        selection = StringVar()
        for expense_type in self.yearly_expenses:
            Radiobutton(frame, text=expense_type, variable=selection, value=expense_type).pack(side=TOP, fill=X, ipadx=1)
        Button(frame, text='Edit Expense', command=lambda: self.add_amount(frame, selection)).pack(anchor=SE)
        self.back_button(frame)

    # This needs work
    def delete_expense(self):
        frame = Toplevel()
        Label(frame, text="Which expense would you like to delete?", image=self.delete_expense_image).pack(side=TOP)
        for expense in self.yearly_expenses.keys():
            selection = StringVar()
            Radiobutton(frame, text=expense, variable=selection, value=expense).pack(anchor=NW)
        self.back_button(frame)

    def validate_delete(self, user_selections):
        for expense in user_selections:
            print(expense)

    def quit_button(self, frame):
        Button(frame, text='Quit', command=self.quit).pack(anchor=SE)

    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).pack(anchor=SE)

if __name__ == '__main__':
    root = Tk()
    root.title('Budget App')
    app = BudgetGui(root)
    app.mainloop()
