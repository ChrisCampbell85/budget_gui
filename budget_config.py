from PIL import ImageTk

class BudgetConfig:
    def __init__(self):
        self.expense_frequency = {
            'Daily': 365,
            'Weekly': 52,
            'Monthly': 12,
            'Yearly': 1
        }
        self.fonts = {'button': ('Devanagari MT', 15, 'normal'),
                        'title': ('Gill Sans MT', 18, 'italic'),
                        'regular': ('Myanmar MN', 15, 'normal')
        }

class BudgetMedia:
    def __init__(self):
        self.images = {'income': ImageTk.PhotoImage(file='.//pics//money_sack.jpg'),
                        'menu': ImageTk.PhotoImage(file='.//pics//money.jpg'),
                        'show_amount': ImageTk.PhotoImage(file='.//pics//money_bag.jpg'),
                        'edit_amount': ImageTk.PhotoImage(file='.//pics//money_roll.jpg'),
                        'create_expense': ImageTk.PhotoImage(file='.//pics//dollar_bill.jpg'),
                        'delete_expense': ImageTk.PhotoImage(file='.//pics//burning_money1.jpg')
        }