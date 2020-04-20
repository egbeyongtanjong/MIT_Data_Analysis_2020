# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:48:44 2020

@author: Egbeyong
Lecture 2, problem set#0

"""
#*********************************************************************
"""
#Printing name and date of birth

DOB = input("Enter your date of birth:")
print("**",DOB)
name = input("Enter your last name:")
print("**",name)
print(name, DOB)

"""
#*********************************************************************
"""
Notes:
    
    
A luddite is someone opposed to new technologies or stuck in the 
past
Usage: I am abit of a luddite

The Spyder IDE offers:
syntax highlighting, auto-completion, smart-indent, integrated debugger

Everything in python is an object
Each object has a type (python provides a built in function can be called to obtain)
and info about the type lets you know what you can with the object

There are two base types: scalar and non-scalar

scalar (primitive types) e.g. integers, float, boolean, none 
 (you can try to beak further,
but results will not be pleasant)

There is no char in python, char is considered a string of length 1

expressions: e.g. 3 + 2 

3/2 = 1.50 (integer division is not allowed)
3.0/2.0 = 1.5

The plus operator is overloaded, depending on the type of operands 
its function changes 

1 + 2 = 3      (addition)
'a' + 'b' = ab (concatenaiton)

Executed from a script (run from IDE), or executed directly in the 
interpreter (type in shell, and press enter)

In a striaght line program with no loops/repetition every command
gets executed exactly once

This concept can be used to measure levels of complexity, and identify
the types of functions that can be solved with such programs

Programs are intended to be read not just executed, because if they 
are not read, they cannot be debugged. So enforcing indentation 
to make code more readable is a very good design decision.

Visual structure matches the semantic structure in Python. In Java
and C you can fool the reader with a misrepresented visual structure

When thinking about program complexity, analyzing just the legnth of 
the program is not enough since the size of the data you want to use
to evaluate the program is also important.

Once loops are added, we have a turing complete language!

You have to type cast, since input reads values as string
"""
#*********************************************************************
"""
# This program computes the cuberoot of a perfect cube (Simple method)
# Example of a guess and check method
# Exhaustive enumeration

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
#*********************************************************************




