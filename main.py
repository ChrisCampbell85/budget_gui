from budget_gui import *
from budget_config import BudgetConfig as config
from budget_config import BudgetMedia as media

"""
App creation file
"""
if __name__ == '__main__':
    root = Tk()
    root.title('Budget App')
    app = BudgetGui(config=config(), media=media(), master=root, app_title='Budget App')
    app.mainloop()