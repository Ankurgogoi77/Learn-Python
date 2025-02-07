amount = input("Enter the amount: ")
tax = input("Enter the tax percentage: ")
try:
    amount = float(amount)
    tax = float(tax)
    if amount < 0 or tax < 0:
        print("Amount and tax percentage should be positive.")
    else:
        total = amount + amount * tax / 100
        print(f"The total amount is {total}")
except ValueError:
    print("Please enter a valid number.") 