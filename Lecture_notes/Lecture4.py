# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:15:28 2020

@author: Egbeyong 

Lecture 4
"""
#*****************************************************
"""
In general having more code than necessary is a bad thing

The reason for this is becomes the difficulty in getting code 
to work increases (maybe quadratically) as the size of the code increases

So is lines of code necessarily a good measure of complexity?

Functions, classes... provide for decomposition and abstraction

decomposition creates structure, it allows us to break programs down
into modules. 

And advantage of a module is that it should be self contained 
and reusable

abstraction supresses details. It allows us to use a piece of code
as if it were a black box. 

Functions let's us in a way extend a language by adding new primitives

If you see none popping up in your output, you probably forgot to 
return a value 

Stack frames

asserts ensure parameters are bound. If it evaluates to true
nothing happens. If it evaluates to false, it stops the program
dead in the tracks. 

Ex. assert type(variable) == float

garbage collection happens automatically. So you can call something 1000
times, it does not use up all your memory. Everytime it is finished, it gets 
rid of what it no longer needs. 

Use the "\" to jump lines without error

formals are the function parameters, actuals, is what is actually
passed

Using assertions, is defensive programming

In executing script, a new scope/frame is created when ever a 
function is called. Once completed, the frame is popped

In execution, the interpreter therefore makes use of stack frames

debugg stack viewer lets you visualize all the different stack
frames through out the course of execution

Whcich stacks exist in the stack viewer depend on the functions that are 
still active. Completed functions are popped.


x = 2.0
assert type(x) == float
print(x\
      )
"""

#program to illustrate the use of listing in for loop
for x in (-1,1,5):
    print (x)

sum_digits = 0

#program to find the sum of digits in a number
for c in str(123456789):
    sum_digits += int(c)
print(sum_digits)

#use of the string.find() builtin function
name = 'Egbeyong'
print(name.find('g'))


