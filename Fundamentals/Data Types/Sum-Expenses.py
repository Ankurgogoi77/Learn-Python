expense = [400, 400, 550, 600, 500]
total = sum(expense)
print(total)

sum = 0
for x in expense:
    sum = sum + x
print(sum)
print('You spent $' + str(sum) + ' this month.')
print('You spent $', sum, sep='')

