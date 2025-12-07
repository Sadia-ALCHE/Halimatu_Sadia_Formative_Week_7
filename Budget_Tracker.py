# Transaction Classes

# So first we create the parent class
class Transaction:
    def __init__(self, date, amount, category, description, transactionType):
        self.date = date
        self.amount = float(amount)
        self.category = category.lower().strip()
        self.description = description
        self.type = transactionType.lower().strip()

    def __str__(self):
        return f"{self.date} | {self.amount:.2f} | {self.category} | {self.description} | {self.type}"

# Now, let's create our child classes
# Child Class for Income
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")

# Child Class for Expense
class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category,description,"expense")


# After making sure we've created classes for our transactions, we create a class for our Budget Tracker which is going to house our code.
# Budget Tracker
class BudgetTracker:
    def __init__(self):
        self.transactions = [] # We've created a list which is going to incorporate all our transactions
        self.budget_limit = None  # Here, we have created a budget limit variable

    # Add Your Income
    def add_income(self):
        print("\nAdding income")
        date = input("Enter date of income(DD/MM/YYYY): ")
        amount = self.validate_amount()
        category = input("Enter category of income: ")
        description = input("Enter description of income: ")

        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print("Your income has been added!")

    # Add Your Expense
    def add_expense(self):
        print("\nAdding expense")
        date = input("Enter date of expense(DD/MM/YYYY): ")
        amount = self.validate_amount()
        category = input("Enter category of expense: ")
        description = input("Enter description of expense: ")

        # Here, we create a warning check
        if self.budget_limit is not None and amount > self.budget_limit:
            print("\nWARNING: Your expense is way above your budget limit!")
            choice = input("Do you still want to continue? (yes/no): ").lower().strip()

            if choice == "no":
                print("Expense has been cancelled.")
                return      # This stops our function here

        # But if the user agrees, then we proceed to:
        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print("Your expense has been added!")

    # Here, we will list our various transactions inputted
    # List All Transactions
    def list_transactions(self):
        print("\nAvailable transactions:")
        if len(self.transactions) == 0:
            print("No transactions available")
        else:
            for t in self.transactions:
                print(t)

    # Let's now create our filter menu
    # Filter Menu
    def filter_transactions(self):
        print("\nYour Filter Options:" )
        print("1) Type")
        print("2) Category")
        print("3) Month(YYYY/MM)")
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

    # Show summary of transactions
    def display_summary(self):
        total_income = 0
        total_expense = 0
        category_totals = {}

        for t in self.transactions:
            if t.type == "income":
                total_income += t.amount
            elif t.type == "expense":
                total_expense += t.amount

            #This updates our category totals
            if t.category not in category_totals:
                category_totals[t.category] = 0
            # expense adds, income subtracts
            if t.type == "expense":
                category_totals[t.category] += t.amount
            else:
                category_totals[t.category] -= t.amount

        balance = total_income - total_expense        # This is the money we have left after we take out our expense from the income we have

        print("\nBudget Summary:")
        print(f"Total Income: {total_income:.2f}")
        print(f"Total Expense: {total_expense:.2f}")
        print(f"Balance: {balance:.2f}")
        print("\nCategory totals:")
        for category, total in category_totals.items():
            print(f"- {category}: {abs(total):.2f}")

    # Let's create a feature for undoing our last transaction
    # Undo last transaction
    def undo_last_transaction(self):
        if len(self.transactions) == 0:
            print("No transactions available")
        else:
            remove_transaction = self.transactions.pop()
            print("\nRemoving transaction:")
            print(remove_transaction)

    # Here, we add a feature which allows the user to set their budget threshold
    def set_threshold(self):
        print("\nSet your budget limit:")
        self.budget_limit = self.validate_amount()
        print(f"Your budget limit has been set to {self.budget_limit:.2f}")

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
    tracker = BudgetTracker()

    while True:
        print("\nWelcome to the Budget Tracker!")
        print("1) Add income")
        print("2) Add expense")
        print("3) Show all transactions")
        print("4) Filter transactions")
        print("5) Display summary")
        print("6) Undo the last transaction")
        print("7) Set your budget limit")
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
        elif choice == "5":
            tracker.display_summary()
        elif choice == "6":
            tracker.undo_last_transaction()
        elif choice == "7":
            tracker.set_threshold()
        elif choice == "0":
            print("Okay, goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()





