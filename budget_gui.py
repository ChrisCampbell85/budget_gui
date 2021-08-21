from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from save_to_db import pickle_expenses, unpickle_expenses

# create export to csv function
# create income input and budgeting functionality i.e. desired savings, savings totals etc

"""
This class setups up an tkinter GUI for a simple budgeting app. Mappings for functions, media and name are created at initialization
"""
class BudgetGui(Frame):
    def __init__(self, master=None, app_title=None):
        super().__init__(master)
        self.button_dict = {
            'Enter Income': self.enter_income,
            'Show Budget': self.show_budget,
            'Create Expense': self.create_expense,
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
                        'title': ('Gill Sans MT', 18, 'bold'),
                        'regular': ('Myanmar MN', 15, 'bold')
        }
        self.app_title = app_title
        self.yearly_expenses = {}
        self.master = master
        self.menu_image = ImageTk.PhotoImage(file='money.jpg')
        self.show_amount_image = ImageTk.PhotoImage(file='money_bag.jpg')
        self.edit_amount_image = ImageTk.PhotoImage(file='money_roll.jpg')
        self.create_expense_image = ImageTk.PhotoImage(file='dollar_bill.jpg')
        self.delete_expense_image = ImageTk.PhotoImage(file='burning_money1.jpg')
        self.pack()
        self.create_menu()
        self.create_buttons()


    def create_menu(self):
        Label(self, text=self.app_title, font=self.fonts['title']).pack(side=TOP, fill=BOTH)
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


    def enter_income(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Enter your income:', font=self.fonts['title']).pack(side=TOP)
        income = StringVar()
        Entry(frame, textvariable=income).pack(side=TOP)
        Button(frame, text='Add Frequency', command=lambda: self.expense_frequency_calc(frame, 'Income', income)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.expense_frequency_calc(frame, 'Income', income))
 

    def create_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Please enter an expense to create:', font=self.fonts['title']).pack(side=TOP, fill=X)
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
            Radiobutton(frame, text=freq, variable=freq_value, value=value).pack(anchor=NW)
        Button(frame, text='Save', command=lambda: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value))        
        self.back_button(frame)
        self.quit_button(frame)


    def calculate_yearly_expense(self, frame, create_text, add_amount_text, freq_value):
        frame.destroy()
        if create_text != "Income":
            create_text = create_text.get()
        expense_amount = int(add_amount_text.get()) * freq_value.get()
        self.yearly_expenses[create_text.capitalize()] = expense_amount
        

    def show_budget(self):
        frame = Toplevel()
        frame.grab_set()
        Label(frame, text='Total Yearly Expenses', font=self.fonts['title']).pack(side=TOP)
        Label(frame, image=self.show_amount_image).pack(side=TOP)
        total, line = 0, 50 * '-'
        for key, value in self.yearly_expenses.items():
            if key != 'Income':
                Label(frame, text=f'* {key}: ${value}', font=self.fonts['regular']).pack(anchor=NW)
                total += value
        Label(frame, text=f'{line}\n').pack(anchor=NW)
        Label(frame, text=f'Total Expenses: ${total}', font=self.fonts['regular']).pack(anchor=NW)
        self.income_less_expenses(frame, total)
        self.back_button(frame)
        self.quit_button(frame)

    def income_less_expenses(self, frame, total):
        if 'Income' in self.yearly_expenses:
            net = self.yearly_expenses['Income'] - total
            Label(frame, text=f'Net Savings: ${net}', font=self.fonts['regular']).pack(anchor=NW)

    def edit_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Edit Expenses', font=self.fonts['title']).pack(side=TOP)
        Label(frame, image=self.edit_amount_image).pack(side=TOP)
        selection = StringVar()
        selection.set(None)
        for expense_type in self.yearly_expenses:
            if expense_type != 'Income':
                Radiobutton(frame, text=expense_type, variable=selection, value=expense_type, font=self.fonts['regular']).pack(anchor=NW)
        Button(frame, text='Edit Expense', command=lambda: self.add_amount(frame, selection)).pack(anchor=SE)
        self.back_button(frame)


    def delete_expense(self):
        frame = Toplevel()
        user_selection = []
        Label(frame, text="Which expense would you like to delete?", image=self.delete_expense_image, font=self.fonts['title']).pack(side=TOP)
        for expense in self.yearly_expenses.keys():
            selection = StringVar()
            selection.set(None)
            Radiobutton(frame, text=expense, variable=selection, value=expense, font=self.fonts['regular']).pack(anchor=NW)
            user_selection.append(selection)
        Button(frame, text='Delete', font=self.fonts['regular'], command=lambda: self.delete(frame, user_selection)).pack(anchor=SE)
        Button(frame, text='Reset', font=self.fonts['regular'], command=lambda: self.reset(user_selection)).pack(anchor=SE)
        self.back_button(frame)


    def delete(self, frame, user_selection):
        for item in user_selection:
            item = item.get()
            if item in self.yearly_expenses.keys():
                self.yearly_expenses.pop(item)
        frame.destroy()


    def reset(self, user_selection):
        for item in user_selection:
            item.set(None)

        
    def quit_button(self, frame):
        Button(frame, text='Quit', command=self.quit).pack(anchor=SE)


    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).pack(anchor=SE)
