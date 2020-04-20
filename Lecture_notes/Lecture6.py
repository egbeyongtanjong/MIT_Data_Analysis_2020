# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:23:44 2020

@author: Egbeyong
Lecture 6, Recurssion

"""
"""
Keys could be associated with numbers, strings, dictionaries
tuple...

If you are going to use code in multiple places, creating a 
function saves you typing/rewriting time of code and time to debug code

But more importantly, it gives you modular abstraction. Secluding
a particular functionality to one place, so that if you are going
to change how you perform a function, you need not comb
through all the code

Infact modular abstraction is an example of a general problem
solving principle called DIVIDE and CONQUER

Recursion is a sweet divide and conquer technique

1. Recursion is both a way of describing and defining problems
2. and a way of designing solutions.

The base part typically gives us a direct answer
The recursive or inductive case, reduces the problem to a simpler 
version in every run plus some smaller operations 

Sometimes when you get a problem, think about how you can break it down 
recursively

Towers of Hanoi

Doing a simple check for pallindromes
"""
def toChar(s):
    #import string
    ans =''
    s = str.lower(s)
    for c in s:
        if c != ' ' or '.': 
           ans = ans + c
    return ans
    
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

print(isPal(toChar('Guttag')))    
print(isPal(toChar('Guttug')))  
print(isPal(toChar('Able was I ere I saw Elba')))

#the following test functions checks the pallindrome 
#implementation for example

def isPalTest(): 
    L = [1, 2] 
    result = isPal(L) 
    print ('Should print False:', result )
    L = [1, 2, 1] 
    result = isPal(L) 
    print ('Should print True:', result )

#fibonacci series

def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)
    
print(fibonacci(4))

#Anything on a binary computer has this inherent limitation
print(1/100 + 9/100)
print(10/100)
    
    
    
    
    
    
    
    