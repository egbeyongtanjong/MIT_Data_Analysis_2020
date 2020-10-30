# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:48:08 2020

@author: Egbeyong

Lecture 13

Basic probabilty and simulation


How do we think about the results of programs when the 
programs themselves are stochastic (random prob distribution)

We can analyze these statistically, but may not be able to 
predict precisely

Almost everything in the real world is stochastic

What is therefore the role of randomness in computation?

There is something comforting about newtonian mechanics

What is causal non-determinism? The belief that not every event
is caused by previous events.

A process is stochastic if its next state depends on both
the previous states and some random element
"""

# Rolling a die example

import random

def rollDie ():
    """ returns a random int between 1 and 6 """
    return random.choice([1,2,3,4,5,6])

def testRoll(n):
    result = ' '
    for i in range(n):
        result = result + ' ' + str(rollDie())
    return result

print(testRoll(10))

# Pylab is Pythons door into MATLAB, and enables plotting good visuals
# The plotting capabilities of Pylab are comparable to that of MATLAB

import pylab

#Plots first list as x-coordinates, and second list as y-coordinates
#size of both list must be the same


pylab.figure(1)

pylab.plot([1,2,3,4], [1,2,3,4])

pylab.figure(2)

pylab.plot([1,2,3,4], [1,4,9,16])

pylab.savefig('firstSaved')

pylab.figure(1) #Says you want to plot a second figure on figure 1

pylab.plot([5,6,7,10]) #assumes that the list is the y-axis and uses [0,1,2,3] as the corrresponding x-axis

pylab.savefig('secondSaved')

pylab.show() #not necessary in Python 3.6 to show the plot. 

print(1)

#Simple program calculating compound interest

principal = 10000  #initial investment
interestRate = 0.05
years = 20
values = []

for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values)   

pylab.title('5% Growth, Compounded Annually') 
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

pylab.savefig('third saved')
pylab.show()




