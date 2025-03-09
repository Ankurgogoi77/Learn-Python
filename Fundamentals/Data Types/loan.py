money_owed = float(input("Enter the amount of money owed: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_payment = float(input("Enter the monthly payment: "))
months = int(input("Enter the number of months: "))

for i in range(months): 
    interest = money_owed * annual_interest_rate / 12 / 100
    money_owed = money_owed + interest - monthly_payment
    if money_owed < 0:
        money_owed = 0
        break
#round off to two decimal places
money_owed = round(money_owed, 2)

#show the remaining balance
print("Remaining balance: $" + str(money_owed))

#show in how many months the loan will be paid off
if money_owed == 0:
    print("The loan will be paid off in " + str(i + 1) + " months.")
else:
    print("The loan will not be paid off in " + str(months) + " months.")
    
#option to calculate the total amount paid
total_paid = monthly_payment * months
print("Total amount paid: $" + str(total_paid))

#option to calculate the total interest paid    
total_interest = money_owed - total_paid
print("Total interest paid: $" + str(total_interest))
