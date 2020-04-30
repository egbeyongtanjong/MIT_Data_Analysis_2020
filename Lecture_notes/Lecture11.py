# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:58:45 2020

@author: Egbeyong

Lecture 11

"""
"""
We are back to talking about abstract data types and object oriented
programming

The whole idea is that we can use oo concepts to extend our programming 
language.

classes are abstract because for each class we basically define an
interface. A program that explains the method

The interface explains what the function does, but does not explain how it
is implemented

We have looked at how we could hashing to implement a set of integers

Syntax:
class class_name(super_class)

Since everything in Python is an object, the global superclass is object

Consider the following example
"""

#This program will store data of people from Cameroon

import datetime #We import this module to help us calculate ages of persons

class Person(object):   #class person is a subclass of object
    def __init__ (self, name):  #special function that initialiazes instance variables
        #create a person with name name
        self.name = name
               
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getLastName(self):
        #returns self last name
        return self.lastName
    
    def setBirthday(self, birthDate):
        #assumes birthdate is of type datetime.date
        # (year,month,day)
        assert type(birthDate) == datetime.date
        self.birthday = birthDate
    def getAge(self):
        #Assumes self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    def __lt__(self,other):
        #returns true if self's name is lexicograpically greater
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #returns self's name
        return self.name











#Class test cases
def personTest(nom):
    s= Person(nom)

    print(s.__str__())
#print(s.lastName) #lastName is hiding and not meant to be accessed directly

    print('Your last name is: ', s.getLastName())
    year = int(input('Enter the year you were born: '))
    month = int(input('Enter the numerical value of your birth month: '))
    day = int(input('What day of the month were ou born on: '))
    s.setBirthday(datetime.date(year,month,day))
    print()
    print('Your age in days is: ',s.getAge())
    
    p= Person("Ebob Tanjong")
    
    print("It is ",p.__lt__(s)," that ",p.__str__(),"comes before " \
          , s.__str__ ()," on the class list.")

personTest('Egbeyong Tanjong')
    

