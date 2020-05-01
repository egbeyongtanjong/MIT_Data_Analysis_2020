# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:58:45 2020

@author: Egbeyong

Lecture 11

"""
"""
We are back to talking about abstract data types and the role
of classes in object oriented programming

The whole idea is that we can use oo concepts to extend our programming 
language by adding user defined types.

The goal is that these types can be used just as easily as any of the
built in types

classes are abstract data types because for each class we basically define an
interface. A program that explains what the methods do

The interface explains what the methods does at the level of the user, but does not explain how it
is implemented. Which is exactly the way built in types work. 

We use print statements, append ... but do not really worry about how
they were implemented

For example consider the example of dictionaries. We only recently saw the 
hashing mechaisisms that go into making them work the way they do


We have looked at how we could hashing to implement a set of integers

Syntax:
class class_name(super_class)

Since everything in Python is an object, the global superclass is object
For example you can have a class called

class inSet(object):

So every instance of inSet is an object

Anything of the form __methodName___() has a special status in Python

Whenever an instance of the class (object) is created the underbar
methods acts on the instance.Think of constructors in java. They can be 
parmetized or none parametized

Class interface should not include private methods/ but it is not 
enforced

Consider the method 
def setBirthday(self, birthdate):

Say p is an object of the class that has this method defined in.
In calling this method, you will write something like

p.setBirthday('3/1/1998')

Basically it will seem as if you used only one argument. However,
the p before the dot is actually the first argument to the method
setBirthday.

The idea of classes is that you want to program to the specification of
the data type instead of the implementation. Therefore making
changes to instance variable directly though not impossible is not ideal.

Imagine that in the implementation you want to use an instance variable 
as an int, so you cat it to int. However, a user changes the variable
to a string format. It might cause the program to break if the 
class implementation is altered.

Data hiding is a very important concept. It gives abstract data types
thesame status as built in types. The minute you choose to ignore this
you do it at your own peril.

Java uses the keyword private to enforce this, but python does not 
(Maybe it is a flaw in the language, maybe it is not)


Consider the following example
"""

#Example 1: 
    
#This program will store data of people

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


"""
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
 """   


"""
Example 1 continued

The idea of this example is to demonstrate how we use classes
and abstract data types to design programs

Imagine you want to write a program to keep track of all students,
faculty, and staff at LSU. You can write this program without using any classes

You can use dictionaries and store the name, address, years, grades...
per person. It will not be elegant, but it is doable

Alternatively, you can think about what abstractions could be useful.
This kind of thought process is the object oriented thought process

So basically you think at the level of abstraction, as opposed to thinking
at the level of lists, dicts and floats

Object Oriented Programming also enables inheritance. This is important 
because in our case for example, there are both similarities and differences
between students, faculty, and staff, so using inheritance will
help you reuse some of the similarities.

Basically all three types are persons, so starting with an abstraction person 
can be useful.

I already defined the class Person above, so right now I will go ahead to use it.
This illustrates the usefulness of hierachies


Every LSU person has an ID. So they are people, plus they have an ID

Also LSU Person is a subclass of Person(superclass). So it inherits all the attributes
of Person

"""

class LSUPerson(Person): #class LSUPerson extends class Person
    #nextIdNum is a class variable, it is not associated with an instance of an LSU person
    nextIdNum = 0 #global variable ID since all LSU people are expected to have one
    
    #The class itself is an object, so we can have class variables
    
    #Having this ability ensures that we can assign unique ID nums to LSUPersons
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = LSUPerson.nextIdNum    #assigns an ID to every LSU person
        LSUPerson.nextIdNum += 1            #increments ID so that the next person gets a different one
    
    def getIdNum(self):                     #Property that find ID number
        return self.idNum
    def __lt__(self,other):                 #compares two people on the basis of their ID numbers
        return self.idNum < other.idNum
    def isStudent(self):
        return type(self) == UG or type(self) == G
    
    
class UG(LSUPerson): #UG is an undergraduate LSU student
    def __init__(self, name):
        LSUPerson.__init__(self, name)
        self.year = None
    def setYear (self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year

class G(LSUPerson):
    pass                #A graduate student is an LSUPerson with no special property
    
p1 = UG('Barbara Beaver')  
p2 = UG('Sue Wong') 
p3 = G('Sue Wong') 
p4 = LSUPerson('Ebob Tanjong')

p1.setYear(4)

print(p1.getIdNum(),":",p1.name)
print(p2.getIdNum(),":",p2.name)
print(p3.getIdNum(),":",p3.name)
    
print(p1.__lt__(p4))
print(p4.isStudent()) 
print(p1)  
    
    
    





