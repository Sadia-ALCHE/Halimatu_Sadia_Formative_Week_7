# Transaction Classes

# So first we create the parent class
class Transaction:
    def __init__(self, date, amount, category, description, transactionType):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.type = transactionType

    def __str__(self):
        return f"{self.date} | {self.amount:.2f} | {self.category} | {self.description} | {self.type}"

# Now, let's create our child classes
# Child Class for Income
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "Income")

# Child Class for Expense
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category,description,"Expense")


# After making sure we've created classes for our transactions, we create a class for our Budget Tracker which is going to house our code.
# Budget Tracker
class Budget_Tracker:
    def __init__(self):
        self.transactions = [] # We've created a list which is going to incorporate all our transactions

    # Add Your Income
    def add_income(self):
        print("Adding income")
        date = input("Enter date of income(DD/MM/YYYY): ")
        amount = self.validate_amount()
        category = input("Enter category of income: ")
        description = input("Enter description of income: ")

        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print("Your income has been added!")

    # Add Your Expense
    def add_expense(self):
        print("Adding expense")
        date = input("Enter date of expense(DD/MM/YYYY): ")
        amount = self.validate_amount()
        category = input("Enter category of expense: ")
        description = input("Enter description of expense: ")

        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print("Your expense has been added!")

    # Here, we will list our various transactions inputted
    # List All Transactions
    def list_transactions(self):
        print("Available transactions:")
        if len(self.transactions) == 0:
            print("No transactions available")
        else:
            for t in self.transactions:
                print(t)

    # Let's now create our filter menu
    # Filter Menu
    def filter_transactions(self):
        print("Your Filter Options:" )
        print("1) Type")
        print("2) Category")
        print("3) Month(YYYY/MM")
        choice = input("Enter your choice: ")

        results = []
        if choice == "1":
            filter_type = input("Enter type (income/expense): ")
            for t in self.transactions:
                if t.type == filter_type:
                    results.append(t)

        elif choice == "2":
            filter_category = input("Enter category : ")
            for t in self.transactions:
                if t.category == filter_category:
                    results.append(t)

        elif choice == "3":
            filter_month = input("Enter month(YYYY/MM): ")
            for t in self.transactions:
                if t.date.startswith(filter_month):
                    results.append(t)

        else:
            print("Invalid Choice. Please try again.")
            return
        if len(results) == 0:
            print("Unable to find any matching transactions.")
        else:
            print("Transactions found:")
            for r in results:
                print(r)

    # Let's validate our amount to make sure it is an actual number and not less than 0
    def validate_amount(self):
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
            tracker.list_transactions()
        elif choice == "4":
            tracker.filter_transactions()
        elif choice == "0":
            print("Okay, goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()





