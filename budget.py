class Expenses:
    def __init__(self):
        self.expenses = {}
        self.yearly_expenses = {}
        self.total_expense_amount = 0

    def add_expense(self):
        user_expense = input('Please enter type of expense: ').capitalize()
        if user_expense.isdigit():
            print('Please enter a valid expense type.')
            self.add_expense()
        else:
            try:
                self.expenses[user_expense] = int(input('Please enter expense amount: $'))
                amount = self.expenses[user_expense]
                frequency = self.calculate_expense_cycle()
                self.calculate_yearly_expenses_by_catergory(amount, frequency, user_expense)
            except ValueError:
                print('Error')
                self.add_expense()

        
    def edit_expense(self):
        numbered_expenses = self.list_dict(self.expenses)
        try:
            user_selection = int(input('Please enter the expense number to edit: '))
            for item in numbered_expenses:
                if user_selection == item[0]:
                    print(f'You have selected: {item[1]}')
                    self.expenses[item[1]] = int(input('Please enter new amount for this expense: $'))
                    amount = self.expenses[item[1]]
                    frequency = self.calculate_expense_cycle()
                    self.calculate_yearly_expenses_by_catergory(amount, frequency, item[1])
        except ValueError:
            print('Error')
            self.edit_expense()

    def delete_expense(self):
        numbered_expenses = self.list_dict(self.expenses)
        try:
            user_selection = int(input('Enter the number of the expense you would like to delete?\n> ' ))
            for item in numbered_expenses:
                    if user_selection == item[0]:
                        print(f'You have selected: {item[1]}')
                        yes_or_no = str(input('Is this correct? (y/n)\n> ').lower())
                        if yes_or_no == 'n':
                            return
                        elif yes_or_no == 'y':
                            self.total_expense_amount - self.expenses[item[1]]
                            del self.expenses[item[1]]
                            del self.yearly_expenses[item[1]]
                        else:
                            self.delete_expense()
        except ValueError:
            print('Woops')
            self.delete_expense()

    def list_dict(self, dict):
        listed_dict = list(enumerate(dict,1))
        for key, value in listed_dict:
            print(f'{key}: {value}')
        return listed_dict


    def calculate_expense_cycle(self):
        frequency = {'weekly': 52,
                    'monthly': 12,
                    'yearly': 1}
        print('What is your expense frequency?')
        listed_frequency = self.list_dict(frequency)
        user_selection = int(input('> '))
        for cycle in listed_frequency:    
            if user_selection == cycle[0]:
                print(f'You have selected: {cycle[1].capitalize()}.')
                result = cycle[1]
        return int(frequency[result])


    def calculate_yearly_expenses_by_catergory(self, amount, frequency, item):
        self.yearly_expenses[item] = amount * frequency


    def calculate_total_expenses(self):
        for amount in self.yearly_expenses.values():
            self.total_expense_amount += amount
        return f'${self.total_expense_amount}'


class Income:
    def __init__(self, income=0):
        self.income = income
    
    def set_income(self):
        try:
            self.income = int(input('Please enter your yearly salary: $'))
        except ValueError:
            print('Please enter a valid number')
            self.set_income()

    def __str__(self):
        return f'Income: ${str(self.income)}'

class Budget:
    def __init__(self):
        
        self.income = Income()
        self.expenses = Expenses()
        return print('Budget Created!')

    def show_weekly_expenses(self):
        print('Weekly expenses:')
        for expense, amount in self.expenses.expenses.items():
            print(f'{expense}: ${amount}')

    def show_yearly_expenses_list(self):
        print('Yearly expenses:')
        for expense, amount in self.expenses.yearly_expenses.items():
            print(f'{expense}: ${amount}')

    def show_yearly_totals(self):
        print(f'Yearly total:\n{self.expenses.calculate_total_expenses()}')

    def show_income(self):
        print(f'Yearly Income:\n${self.income.income}')

    def show_income_less_expenses(self):
        net = self.income.income - self.expenses.total_expense_amount
        print(f'Net funds:\n${net}')


if __name__ == '__main__':
    Budget().expenses.add_expense()




    
        


