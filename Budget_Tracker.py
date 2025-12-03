# Transaction Classes

# So first we create the parent class
class Transaction:
    def __init__(self, date, time, amount, category, description, transactionType):
        self.date = date
        self.time = time
        self.amount = amount
        self.category = category
        self.description = description
        self.transactionType = transactionType

# Now, let's create our child classes
# Child Class for Income
class Income(Transaction):
    def __init__(self, date, time, amount, category, description, transactionType):
        super().__init__(date, amount, category, description, "Income")

# Child Class for Expense
class Expense(Transaction):
    def __init__(self, date, time, amount, category, description, transactionType):
        super().__init__(date, amount, category,description,"expense")


