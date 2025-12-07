# Halimatu_Sadia_Formative_Week_7
My Formative for Week 7 Submission(Budget Tracker)
# Budget Tracker – Week 7 Formative Project

This Budget Tracker is a simple Python program that runs in the terminal.  
It runs in the terminal and allows users to record their income and expenses, filter them, and see an overall summary of their spending.  
The goal of the project was to practise object-oriented programming, input validation, loops, functions, and basic menu navigation.

# Features:
- Add income
- Add expense
- View all transactions
- Filter transactions (either by type, category, or month)
- Budget summary (total income, total expenses, balance, and category totals)
- Set a budget warning threshold
- Undo last transaction
- Simple menu system

Now, during this program, everything we do is stored in a list.

# How to Run the Program
1. Open PyCharm.
2. Open the project folder
- (If you already created a GitHub repository and cloned/downloaded it,
go to File; Open and select that folder.)
- Make sure your .py file (your budget tracker code) is inside this folder.
3. In PyCharm’s Project sidebar, click on your Python file
(example: main.py or whatever you named your file).
4. At the top-right of PyCharm, click the green run button ️OR right-click the file; Run 'main'.
5. The program will start running in the black window at the bottom (the terminal).

# When you run the program, this menu is going to appear
Welcome to the Budget Tracker!
1) Add income
2) Add expense
3) Show all transactions
4) Filter transactions
5) Display summary
6) Set budget warning
7) Undo last transaction
0) Exit

# What each option does:
1) Add income
Allows you to enter date, amount, category, and description of income.

2) Add expense
Let's you record an expense.
If the amount is above your threshold, you will get a warning and can choose to cancel or continue.

3) Show all transactions
Lists every income and expense entered.

4) Filter transactions
You can filter by:
- Type (income/expense)
- Category
- Month (YYYY/MM)

5) Display summary
Shows:
- Total income
- Total expense
- Balance
- Category totals

6) Set budget warning
Allows you to set a spending limit.
Any expense higher than this will trigger a warning.

7) Undo last transaction
Removes the most recent transaction added.

0) Exit
Closes the program.

# Sample Interactions
- Adding Income:
  ` Adding income
  ` Enter date of income (DD/MM/YYYY): 02/12/2024
  ` Enter amount: 1200
  ` Enter category of income: salary
  ` Enter description of income: November salary
  ` Your income has been added!

- Adding Expense With Warning
Adding expense
Enter date of expense (DD/MM/YYYY): 03/12/2024
Enter amount: 900
Enter category of expense: shopping
Enter description of expense: clothes

WARNING: This expense is above your budget warning limit!
Do you still want to continue? (yes/no): no
Expense cancelled.

If the user chooses yes, then the output becomes:
Your expense has been added!

- Listing Transactions
Available transactions:
03/12/2024 | 1200.00 | salary | November salary | income

- Your Filter Options:
1) Type
2) Category
3) Month (YYYY/MM)
Enter your choice: 2
Enter category: salary

Transactions found:
03/12/2024 | 1200.00 | salary | November salary | income

- Summary Example
````Budget Summary````
Total Income: 1200.00
Total Expense: 300.00
Balance: 900.00

Category totals:
- salary: 1200.00
- food: 300.00

- Undo Last Transaction
Last transaction has been removed.




