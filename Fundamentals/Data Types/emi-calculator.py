princial_amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

emi = (princial_amount * rate * (1 + rate) * time) / ((1 + rate) * time - 1)
print("The EMI is: $" + str(emi))   

