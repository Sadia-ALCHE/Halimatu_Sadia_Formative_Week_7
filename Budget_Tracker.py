# Transaction Classes

# So first we create the parent class
class Transaction:
    def __init__(self, date, amount, category, description, transactionType):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.type = transactionType

# Now, let's create our child classes
# Child Class for Income
class Income(Transaction):
    def __init__(self, date, amount, category, description, transactionType):
        super().__init__(date, amount, category, description, "Income")

# Child Class for Expense
class Expense(Transaction):
    def __init__(self, date, amount, category, description, transactionType):
        super().__init__(date, amount, category,description,"Expense")


# After making sure we've created classes for our transactions, we create a class for our Budget Tracker which is going to house our code

# Budget Tracker
class Budget_Tracker:
    def __init__(self):
        self.transactions = [] # We've created a list which is going to incorporate alll our transactions

    # Add Your Income
    def add_income(self):
        print("Adding income")
        date = input("Enter date of income(DD/MM/YYYY): ")
        amount = input("Enter amount of income: ")
        category = input("Enter category of income: ")
        description = input("Enter description of income: ")

        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print("Your income has been added!")

    # Add Your Expense
    def add_expense(self):
        print("Adding expense")
        date = input("Enter date of expense(DD/MM/YYYY): ")
        amount = input("Enter amount of expense: ")
        category = input("Enter category of expense: ")
        description = input("Enter description of expense: ")

        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print("Your expense has been added!")



