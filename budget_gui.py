from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk
from save_to_db import pickle_expenses, unpickle_expenses


# create export to csv function
# create income input and budgeting functionality i.e. desired savings, savings totals etc

# create mappings of funcs and config in separate classes to be embedding into __init__?
"""
This class setups up an tkinter GUI for a simple budgeting app. Mappings for functions, media and name are created at initialization
"""
class BudgetGui(Frame):
    def __init__(self, config=None, media=None, master=None, app_title=None):
        super().__init__(master)
        self.button_dict = {
            'Enter Income': self.enter_income,
            'Show Budget': self.show_budget,
            'Create Expense': self.create_expense,
            'Edit Expenses': self.edit_expense,
            'Delete Expenses': self.delete_expense
        }
        self.config = config
        self.media = media
        self.app_title = app_title
        self.yearly_expenses = {}
        self.master = master
        # self.income_image = ImageTk.PhotoImage(file='.//pics//money_sack.jpg')
        # self.menu_image = ImageTk.PhotoImage(file='.//pics//money.jpg')
        # self.show_amount_image = ImageTk.PhotoImage(file='.//pics//money_bag.jpg')
        # self.edit_amount_image = ImageTk.PhotoImage(file='.//pics//money_roll.jpg')
        # self.create_expense_image = ImageTk.PhotoImage(file='.//pics//dollar_bill.jpg')
        # self.delete_expense_image = ImageTk.PhotoImage(file='.//pics//burning_money1.jpg')
        self.pack()
        self.create_or_open()
        

    # option to open new or existing budget
    def create_or_open(self):
        answer = messagebox.askquestion('Welcome!', 'Click \'Yes\' to OPEN existing budget\n Or \'No\' to CREATE new budget')
        if answer == 'yes':
            self.open_budget()
        else:
            self.save_budget(init=True)
        
    # open existing budget, passes filename to menu title
    def open_budget(self):
        filename = filedialog.askopenfilename()
        if filename:
            file_load = unpickle_expenses(filename)
            self.yearly_expenses = file_load
            new_title = filename.split('/')[-1].rstrip('.pkl').capitalize()
            self.create_menu(name=new_title)

    # save budget of existing if init=False, otherwise creates new file
    def save_budget(self, init=False):
        frame = Toplevel()
        Label(frame, text='Type in filename of your budget').pack(side=TOP)
        ent_var = StringVar()
        Entry(frame, textvariable=ent_var).pack(side=TOP)
        if init:
            Button(frame, text='Create', command=lambda: self.create_menu(ent_var.get().capitalize(), frame, init=True)).pack(anchor=SE)
        else:
            Button(frame, text='Save', command=lambda: pickle_expenses(self.yearly_expenses, ent_var.get(), frame)).pack(anchor=SE)

    # if init=True, saves new filename and creates menu with filename as title
    def create_menu(self, name, frame=None, init=False):
        if init:
            pickle_expenses(self.yearly_expenses, name.lower(), frame)
        Label(self, text=name, font=self.config.fonts['title']).pack(side=TOP, fill=BOTH)
        Label(self, image=self.media.images['menu']).pack()
        Button(self, text='Open File', command=self.open_budget).pack(anchor=NE)
        Button(self, text='Save File', command=self.save_budget).pack(anchor=NE)
        self.create_buttons()
        

# create buttons for root window from __init__ parameters
    def create_buttons(self):
        for button_name, func in self.button_dict.items():
            Button(self, text=button_name, font=self.config.fonts['button'], command=func).pack(side=TOP, fill=X)
        self.quit_button(frame=self)


    def enter_income(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Enter your income:', font=self.config.fonts['title']).pack(side=TOP)
        Label(frame, image=self.media.images['income']).pack(side=TOP)
        income = StringVar()
        Entry(frame, textvariable=income).pack(side=TOP)
        Button(frame, text='Add Frequency', command=lambda: self.expense_frequency_calc(frame, 'Income', income)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.expense_frequency_calc(frame, 'Income', income))
 

    def create_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Please enter an expense to create:', font=self.config.fonts['title']).pack(side=TOP, fill=X)
        Label(frame, image=self.media.images['create_expense']).pack(side=TOP)
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


    # options for expense frequency, mapped in __init__
    def expense_frequency_calc(self, frame, create_text, add_amount_text):
        Label(frame, text='Please select expense frequency').pack(side=TOP)
        freq_value = IntVar()
        for freq, value in self.config.expense_frequency.items():
            Radiobutton(frame, text=freq, variable=freq_value, value=value).pack(anchor=NW)
        Button(frame, text='Save', command=lambda: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value)).pack(anchor=SE)
        frame.bind('<Return>', lambda event: self.calculate_yearly_expense(frame, create_text, add_amount_text, freq_value))        
        self.back_button(frame)
        self.quit_button(frame)


    # calculate expenses, excluding income value
    def calculate_yearly_expense(self, frame, create_text, add_amount_text, freq_value):
        frame.destroy()
        if create_text != "Income":
            create_text = create_text.get()
        expense_amount = int(add_amount_text.get()) * freq_value.get()
        self.yearly_expenses[create_text.capitalize()] = expense_amount
        

    # shows all expenses, totals, and net result
    def show_budget(self):
        frame = Toplevel()
        frame.grab_set()
        Label(frame, text='Total Yearly Expenses', font=self.config.fonts['title']).pack(side=TOP)
        Label(frame, image=self.media.images['show_amount']).pack(side=TOP)
        total, line = 0, 50 * '-'
        for key, value in self.yearly_expenses.items():
            if key != 'Income':
                Label(frame, text=f'* {key}: ${value}', font=self.config.fonts['regular']).pack(anchor=NW)
                total += value
        Label(frame, text=f'{line}\n').pack(anchor=NW)
        Label(frame, text=f'Total Expenses: ${total}', font=self.config.fonts['regular']).pack(anchor=NW)
        self.income_less_expenses(frame, total)
        self.back_button(frame)
        self.quit_button(frame)


    def income_less_expenses(self, frame, total):
        if 'Income' in self.yearly_expenses:
            net = self.yearly_expenses['Income'] - total
            Label(frame, text=f'Net Savings: ${net}', font=self.config.fonts['regular']).pack(anchor=NW)


    def edit_expense(self):
        frame = Toplevel()
        frame.grab_set()
        frame.focus_set()
        Label(frame, text='Edit Expenses', font=self.config.fonts['title']).pack(side=TOP)
        Label(frame, image=self.media.images['edit_amount']).pack(side=TOP)
        selection = StringVar()
        selection.set(None)
        for expense_type in self.yearly_expenses:
            if expense_type != 'Income':
                Radiobutton(frame, text=expense_type, variable=selection, value=expense_type, font=self.config.fonts['regular']).pack(anchor=NW)
        Button(frame, text='Edit Expense', command=lambda: self.add_amount(frame, selection)).pack(anchor=SE)
        self.back_button(frame)


    def delete_expense(self):
        frame = Toplevel()
        user_selection = []
        Label(frame, text="Which expense would you like to delete?", image=self.media.images['delete_expense'], font=self.config.fonts['title']).pack(side=TOP)
        for expense in self.yearly_expenses.keys():
            selection = StringVar()
            selection.set(None)
            if expense != 'Income':
                Radiobutton(frame, text=expense, variable=selection, value=expense, font=self.config.fonts['regular']).pack(anchor=NW)
            user_selection.append(selection)
        Button(frame, text='Delete', font=self.config.fonts['regular'], command=lambda: self.delete(frame, user_selection)).pack(anchor=SE)
        Button(frame, text='Reset', font=self.config.fonts['regular'], command=lambda: self.reset(user_selection)).pack(anchor=SE)
        self.back_button(frame)

    # delete button function
    def delete(self, frame, user_selection):
        for item in user_selection:
            item = item.get()
            if item in self.yearly_expenses.keys():
                self.yearly_expenses.pop(item)
        frame.destroy()

    # reset delete frame user selections
    def reset(self, user_selection):
        for item in user_selection:
            item.set(None)

    # quit program
    def quit_button(self, frame):
        Button(frame, text='Quit', command=self.quit).pack(anchor=SE)


    def back_button(self, frame):
        Button(frame, text='Go Back', command=frame.destroy).pack(anchor=SE)
