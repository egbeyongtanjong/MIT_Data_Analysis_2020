# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:32:35 2019

@author: Egbeyong
"""
'''
#Using variables
x = 3
x = x * x 
print(x)
print()

#Conferting a number to a floating point number
y = float(input("Enter a number: "))
print(y)
print(y*y)
'''
'''
#Checking whether a number is even or odd
x = int(input("Enter a number: "))
if(x%2 == 0):
    print("The number you entered is even")
else:
    print("The number you entered is odd")
    if(x%3 != 0):
        print("The number you entered is a prime")
 '''
'''
#Comparing three numbers
x = int(input("Enter a number: "))  
y = int(input("Enter a second number: ")) 
z = int(input("Enter a third number: ")) 

least_number = x
if y<x:
    least_number = y
    print("The smallest number is ", least_number)
elif z<x:
    least_number = z
    print("The smallest number is ", least_number)
else:
    print("The smallest number is ", least_number)
'''

'''
#Find the cube root of a perfect cube
x = int(input("Enter a number: "))

cube_root = 0

while cube_root**3 < x:
    cube_root += 1
if cube_root**3 == -x:
    print("The number you entered is a perfect cube with cube root ", -1*cube_root)
elif cube_root**3 == x:
    print("The number you entered is a perfect cube with cube root ", cube_root)
else:
    print("The number you entered is not a perfect cube")
'''
'''
#Using the for loop - the for loop hovers over a tuple built by the range function
count = 0
for count in range(4):
    count += 1
print(count)
'''
'''
#Checking for squareroot using epsilon and a step function
x = 0.5 
epsilon = 0.01 
numGuesses = 0 
ans = 0.0 
while abs(ans**2 - x) >= epsilon and ans <= x: 
    ans += 0.00001
    #ans += 1
    numGuesses += 1 
print ('numGuesses =', numGuesses) 
if abs(ans**2 - x) >= epsilon: 
    print ('Failed on square root of', x) 
else: 
    print (ans, 'is close to square root of', x) 

def say_name(name):
    print()
    print(name)

assert True
say_name('Egbeyong')
'''
'''
#Exercise to calculate roots 

"""x, y, epsilon ints or floats. epsilon > 0.0 returns true if x is within epsilon of y""" 
def withinEpsilon(x, y, epsilon):
    return abs(x - y) <= epsilon 

"""assumes i a positive int returns True if i is even, otherwise False"""
def isEven(i): 
    return i%2 == 0 

"""assumes pwr an int; val, epsilon floats
pwr and epsilon > 0
if it exists,
returns a value within epsilon of val**pwr otherwise returns None""" 
def findRoot(pwr, val, epsilon): 
    assert type(pwr) == int and type(val) == float and type(epsilon) == float
    assert pwr > 0 and epsilon > 0
    if isEven(pwr) and val < 0: 

        return None 
    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low)/2.0
    while not withinEpsilon(ans**pwr, val, epsilon):
        #print 'ans =', ans, 'low =', low, 'high =', high if ans**pwr < val: low = ans else: high = ans ans = (high + low)/2.0 return ans 
        if ans**pwr < val: 
            low = ans 
        else: 
            high = ans 
        ans = (high + low)/2.0 
        return ans
"""x float, epsilon float, pwr positive int""" 
def testFindRoot():
    for x in (-1.0, 1.0, 3456.0): 
        for pwr in (1, 2, 3):
            ans = findRoot(pwr, x, 0.001)
            if ans == None: 
                print ('The answer is imaginary') 
            else: 
                print (ans, 'to the power', pwr,'is close to', x) 

root = findRoot(2,3.0,0.1)
print(root)
'''
'''
#Finding the sum of digits in a string of numbers

#print ('Enter a number whose sum of digits you want')
x = input('Enter a number whose sum of digits you want: ' )
sum_of_digits = 0
for digit in x:
    sum_of_digits += int(digit)
print('The sum of the digits in the number is ', sum_of_digits)
'''

'''
# Finding the number of divisors of a number
x = int(input('Enter a number: '))
divisors = ()
for i in range(1, x+1):
        if x%i == 0:
            divisors += (i, )
print('The factors of ', x ,' are ', divisors)
'''


#Problem Set 1: Paying off credit card debt

outstanding_balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest_rate = float(input('Enter the annual credit card interest rate as a decimal: '))
min_monthly_payment_rate = float(input('Enter the minimum monthly payment rate as a decimal: '))



for i in range(1,13):
    minimum_monthly_payment = min_monthly_payment_rate * outstanding_balance
    interest_paid = (annual_interest_rate/12)*outstanding_balance
    principal_paid = minimum_monthly_payment - interest_paid
    remaining_balance = outstanding_balance - principal_paid
    print('Month: ', i)
    print('Minimum monthly payment: ', minimum_monthly_payment)
    print('Principle paid: ', principal_paid)
    print('Remaining balance: ', remaining_balance)
    outstanding_balance = remaining_balance
