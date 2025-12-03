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
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "Income")

# Child Class for Expense
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
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

        inc = Income(date, amount, category, description)
        self.transactions.append(inc)
        print("Your income has been added!")

    # Add Your Expense
    def add_expense(self):
        print("Adding expense")
        date = input("Enter date of expense(DD/MM/YYYY): ")
        amount = input("Enter amount of expense: ")
        category = input("Enter category of expense: ")
        description = input("Enter description of expense: ")

        exp = Expense(date, amount, category, description)
        self.transactions.append(exp)
        print("Your expense has been added!")

    # Here, we will list our various transactions inputted
    # List All Transactions
    def list_transactions(self):
        print("Available transactions:")
        if len(self.transactions) == 0:
            print("No transactions available")
        else:
            for t in self.transactions:
                print(t.date, t.amount, t.category, t.description, t.type)

    # Let's validate our amount to make sure it is an actual number and not less than 0
    def show_valid_amount(self):
        while True:
            amount = input("Enter amount: ")
            try:
                number = float(amount)
                if number > 0:
                    return number
                else:
                    print("Amount must be positive and greater than 0.")
            except:
                print("Invalid Number. Please try again.")

# Let's create our menu which is going to display the various options provided
# Main Menu

def main():
    tracker = Budget_Tracker()

    while True:
        print("Welcome to the Budget Tracker!")
        print("1) Add income")
        print("2) Add expense")
        print("3) Show all transactions")
        print("0) Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tracker.add_income()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.show_valid_amount()
        elif choice == "0":
            print("Okay, goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()





