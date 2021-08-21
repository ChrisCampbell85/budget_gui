from budget_gui import *

"""
App creation file
"""
if __name__ == '__main__':
    root = Tk()
    root.title('Budget App')
    app = BudgetGui(root, 'Budget App')
    app.mainloop()