# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:42:24 2020

@author: Egbeyong

Lecture 3
"""
#***********************************************************************

"""
The guess and check example of finding the root of a perfect cube is an
exhaustive enumeration method.

Exhaustive enumeration is typically refered to as brute force
Try every possible solution in a solution/search space, and if no answer
is found, then there is no solution.

Brute force works because the computer is really fast. 
A good processor can compute 100 million instructions per second!



"""
#***********************************************************************
"""
# WHILE loop method to finding cube roots of a perfect cube
x = int(input("Enter an integer: "))
ans = 0
while ans * ans * ans < abs(x):
    ans = ans + 1
if ans*ans*ans != abs(x):
    print( x, " is not a perfect cube ")
else:
    if x < 0:
        ans = -ans
    print("The cuberoot of ",x," is ",ans)
"""
#***********************************************************************
"""
# FOR loop equivalent of the cube root locator solution
x = int(input("Enter an integer: "))
for ans in range(0, abs(x) + 1):
    if ans**3 == abs(x):
        break                #optimization
if ans**3 != abs(x):
    print(x,"is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("The cuberoot of ",x," is ",ans)
"""
#***********************************************************************
"""
Since finding the exact value for certain computations is tedious
The concept of approximation serves as a saving grace

Basically, we always want to start a good enough approximation we are
willing to accept

"""
"""
#Consider this solution to find the approx square root of a number
# The running time of the algorithm depends on both 
# The distance from the start point to the actual squareroot
# the value of the precision, epsilon and the increment
x = 25
epsilon = 0.01
ans = 0.0
num_guesses = 0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += 0.00001      #stepsize = 0.00001
    # ans += 0.3 #Fails Hence needs a bissection search
    num_guesses += 1
print('numGuesses = ', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on squareroot of ', x)
else:
    print(ans,' is close to the squarre root of ',x)
"""
#********************************************************************* 

#A bisection section search fixes the above limitation  
#The limitation arises when the step size causes the algorithm to fail
#With a bisssection the search space reduces by half everytime

x = 0.5
epsilon = 0.01
guess_num = 0
low = 0.0
high = max(x, 1)
ans = (low + high)/2
while abs(ans**2 - x) >= epsilon and ans <= x:
    guess_num += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2
print("The number of guesses is ",guess_num)
print(ans, ' is close to square toot of ', x)

#*************************************************
"""
#This introduces functions 
#this function returns true if x is within epsilon of y
def withinEpsilon(x,y,epsilon):
    return abs(x-y) <= epsilon
print(withinEpsilon(26,25,1))
"""




  