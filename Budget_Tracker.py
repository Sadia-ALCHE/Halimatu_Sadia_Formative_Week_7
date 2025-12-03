transactions = []

def input_transaction():
    print("\nAdding your transaction")
    date = input("Enter your transaction date (DD-MM-YYYY): ")
    amount = input("Enter your transaction amount: ")

    #For this part, we have to check if the number inputted is an actual number in numeric form and not in words
    #We use try and if that does not work, we use except which gives a message to the user without my code crashing
    try:
        amount = float(amount)
    except:
        print("Not a valid amount. Please enter a numeric value.\n")
        return

    category = input("Enter your transaction category: ")
    description = input("Enter your transaction description: ")
    transactionType = input("Enter your transaction type: ")

    # The category basically helps me to know under what category the money coming in or going out falls under. Is it salary? For food? Gift? Transport? Etc.
    # For description, it's basically giving me extra detail about what exactly the transaction was for.
    # For transaction type, this is where we input what the transaction type is, is it an income or an expense?

    #We now store it as a dictionary
    t = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
        "transactionType": transactionType
        }

    transactions.append(t)
    print("Transaction added!\n")

input_transaction()