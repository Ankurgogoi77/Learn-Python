total = 0
expenses = []

while True:
    try:
        expense = input("Enter an expense: ")
        if expense == "done": # Exit the loop if the user enters "done"
            break
        expense = float(expense)
        if expense < 0:   # Check if the expense is negative
            print("Expense should be positive.")
        else:
            expenses.append(expense)
    except ValueError:
        print("Please enter a valid number.")

for expense in expenses:
    total = total + expense

print("You spent $" + str(total) + " this month.")

#option to view all expenses
view = input("Do you want to view all expenses? (yes/no)")
if view == "yes":
    for expense in expenses:
        print(expense)
else:
    print("Thanks for using the expense tracker!")
    
#option to delete an expense
delete = input("Do you want to delete an expense? (yes/no)")
if delete == "yes":
    try:
        expense = float(input("Enter the expense to delete: "))
        if expense in expenses:
            expenses.remove(expense)
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")
    except ValueError:
        print("Please enter a valid number.")    