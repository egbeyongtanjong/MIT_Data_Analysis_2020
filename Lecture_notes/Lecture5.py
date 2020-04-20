# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 08:36:06 2020

@author: Egbeyong
"""

"""
There are three data structures used in python to collect items:
Tuples, lists, and dictionaries

tuples and lists are ordered sequence of objects.
It makes sense to talk about the first object, the second object,
the last object, and so on

You can get slices of tuples

The major difference between list and tuples is that tuples are 
immutable. Once created, you cannot change its value, you can create
a new tuple, but you cannot change the value of the old one.

Lists are the first mutable objects we are dealing with.
Both lists and tuples need not be homogeneous. A list and a tuple
can contain 
different primitives, and even lists of lists, or tuple of tuples.

list.append(list1) actually mutates list, and it has side effects

we invoke append coz we are interested in the side effects



Dictionaries or dicts (as they are spelled in python) are not ordered
and two, the indices need not be integers and they are not called
integers, they are called keys



Watch out for aliasing (one object with two names) with mutabe objects
L1 = [2]
L2 = L1
L2[0] = 'a'
print(L1)

prints a (since both list point to the same object)

Now copying L1 to L2 produces a different side effect

L1 = [2]
L2 = L1[:]
L2[0] = 'a'
print(L1)

prints [2] (since both list point to different objects)
"""
#********************************************************************
"""
#example of tuple
x = (0,1,2,3,4)
print(x[0])
"""
#*********************************************************************
"""
#Useful example of tuple, find all divisors of 100 and save in a \
#tuple

divisors = ()
for x in range(1, 101):
    if 100%x == 0:
        divisors += (x,) #creates a new tuple in each run
print(divisors)
print(divisors [1:3]) #slicing tuples
divisors = (1,2,3,4) #creates another new tuple
print(divisors)

#*****************************************************************
# Illustrating the beauty and peril of mutation
#L2 updates when ever printed, eventhough L2 was never modified
#after L1 was modified.
L1 = [2,3]
L2 = ['a',L1,L1]
print(L2)
"""
#**************************************************************
"""
# Now we are moving on to talk about dictionaries
#A set of key value pairs
#acccessed by looking at the keys

D = {1: 'one', 'deux':'two','pi':3.14159}
D1 = D
print(D1['deux'])
D1[1] = 'uno'
print(D[1])
print(D.keys())
del D[1]
print(D)
"""
#*****************************************************************
#Example showing what we can do with dictionaries
#Obtaining translations with dictionary

EtoF = {'bread':'du pain', 'wine':'du vin','eats':'mange',\
        'drinks':'bois','likes':'aime',1:'un','6.00':'6.00'}
print(EtoF) 

if 'du pain' in EtoF: #evaluates to false, only keys will evaluate to true 
    print("True")
print()
print(EtoF.keys()) #built-in method to print all keys

#method to translate word 
def translateWord(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word
#method to translate sentence
def translate(sentence):
    translation = ''
    word = ''
    for c in sentence:
        if c != ' ':
            word = word + c
        else:
            translation = translation + ' ' + translateWord(word, EtoF)
            word = ''
    return translation[1:] + ' ' + translateWord(word, EtoF)
#test examples
print(translate('John eats bread'))
print(translate('Steve drinks wine'))
print(translate('John likes 6.00'))











