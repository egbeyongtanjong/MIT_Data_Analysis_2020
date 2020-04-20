# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:15:28 2020

@author: Egbeyong Problem Set 1
Three simple programs
All answered correctly
"""

"""
ages = [12,34,56,78,90]     #homogenous tupple of integers
print(ages[0:len(ages)+1])  #slicing a tupple
Jack = [23, 'Stan', 1.66]
print(Jack[0])
print(ages+Jack)


name = 'Egbeyong'
print(name[0])

"""
"""
# Program to calculate credit card balance

balance = float(input('Enter the outstanding balance on your credit card: '))
interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))
payment_rate = float(input('Enter the minimum monthly payment rate as a decimal: '))
remaining_balance = balance
total_amount_paid = 0.0
for x in range (1, 13):
    print('Month: ',x)
    min_monthly_pay = float(format(payment_rate * balance,'.2f'))
    interest_paid = interest_rate/12*balance
    principal_paid = float(format(min_monthly_pay - interest_paid, '.2f'))
    remaining_balance = float(format(balance - principal_paid, '.2f'))
    print('Minimum monthly payment: $',min_monthly_pay)
    print('Principle paid: $',principal_paid)
    print('Remaining balance: $',remaining_balance)
    balance = remaining_balance
    total_amount_paid += min_monthly_pay
print('RESULT')
print('Total amount paid: $',total_amount_paid)
print('Remaining balance: $',remaining_balance)
"""
#****************************************************************************************
"""
#Problem 2
#Program to pay debt off in a year

balance = float(input('Enter the outstanding balance on your credit card: '))
interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))

monthly_pay = 10.0
temp = balance
while balance > 0:
    balance = temp
    #for x in range(1, 13):
    for x in range(1, 13):
        balance = float(round(balance*(1+(interest_rate/12.0))-monthly_pay, 2))
        if balance < 0:
            break
    monthly_pay += 10

print('RESULT')
print("Monthly payment to pay off debt in 1 year: ", int(monthly_pay-10))
print('Number of months needed: ', x)
print('Balance:',balance)
"""
#************************************************************************
"""
#Problem 3 Using 

#Program to pay debt off in a year

balance = float(input('Enter the outstanding balance on your credit card: '))
interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))

low = balance/12.0
high = (balance*(1+(interest_rate/12.0))**12.0)/12.0
monthly_pay = (low+high)/2
temp = balance
while abs(balance) > 0.01:
    balance = temp
    for x in range(1, 13):
        balance = float(round(balance*(1+(interest_rate/12.0))-monthly_pay,2))
    if balance < 0:
        high = monthly_pay
    else:
        low = monthly_pay
    monthly_pay = (low+high)/2
print('RESULT')
print("Monthly payment to pay off debt in 1 year: ", float(round(monthly_pay, 2)))
print('Number of months needed: ', x)
print('Balance:',balance)
"""





