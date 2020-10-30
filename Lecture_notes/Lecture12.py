# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:06:32 2020

@author: Egbeyong
Lecture 12

Intro to simulation

Picks up from the Person, and LSUpersons classes in Lecture 11

Remember that yield is a genrator that keeps track of a state of 
computation, so that it can go back and pick it up whenever it needs it.

How do we go about building computational models to 
solve real problems?

Analytical Models are things that let you predict what a system is going 
to do. However, they do not always work, so simulations are a fix to them

Three reasons for simulation of prediction:

1.    
Prediction models do not always work well, so simulation models could help
address this. For example, trying to build physical models that exactly predicts
 weather forcast

2. 
Sometimes things get complex, and pinning down all details for a 
predictive model is not as ideal as successively refining a series of simulations.

3.
Extracting useful intermediate results of a simulation is more useful sometimes than
trying to build a detailed analytical model

The advent of computers made simulation useful and possible!



Simulation gives an estimate rather than trying to predict exactly
what is going to happen!


Simulation models are descriptive not prescriptive

Random Walks as it relates to the displacement of things

Brownian motion models

Mov't of the stock market is a random walk, except for the day the 
markets are crashing









from Lecture11 import *


# Defines a new class to create a courselist

class CourseList(object):
    def __init__(self,number):
        self.number = number
        self.students = []
        
    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError ('Not a student')
        elif who in self.students:
            raise ValueError ('Duplicate student')
        else:
            self.students.append(who)
            
    def remStudent(self, who):
        try:
            self.students.remove(who)
        except:
            print(str(who) + 'not in ' + self.number)
    
    def allStudents(self):
        for s in self.students:
            yield s         #can only be used inside a function
         #yield is also a form called a generator, you can return a list, but what if you want to return only certain elements of the list?   
    #return causes any info we had to get popped off the stack frame once found
    #A generator remembres the points in the function body where it last returned
    
    def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
            indx += 1
 
    
m1 = LSUPerson('Barbara Beaver')  
ug1 = UG('Jane Doe') 
ug2 = UG('John Doe') 
g1 = G('Mitch Peabody') 
g2 = G('Ryan Jackson') 
g3 = G('Sarina Canelake') 
SixHundred = CourseList('6.00') 
SixHundred.addStudent(ug1) 
SixHundred.addStudent(g1) 
SixHundred.addStudent(ug2) 
try:     
    SixHundred.addStudent(m1) 
except:     
    print('Whoops') 
    print (SixHundred) #Perhaps not what one expected 
SixHundred.remStudent(g3) 
print ('Students') 
for s in SixHundred.allStudents():     
    print(s)
print('Students Squared') 
for s in SixHundred.allStudents():    
    for s1 in SixHundred.allStudents():         
        print(s, s1) 
print('Undergraduates') 
for u in SixHundred.ugs():    
    print(u)     
        
"""

import random   
   
class Location(object):     
    def __init__(self, x, y):         
        """x and y are floats"""        
        self.x = x        
        self.y = y   
        
    def move(self, deltaX, deltaY):     
        """deltaX and deltaY are floats"""      
        return Location(self.x + deltaX, self.y + deltaY)   
    
    def getX(self):      
        return self.x   
    
    def getY(self):       
        return self.y    
    
    def distFrom(self, other):       
        ox = other.x         
        oy = other.y        
        xDist = self.x - ox       
        yDist = self.y - oy        
        return (xDist**2 + yDist**2)**0.5   
    def __str__(self):        
        return '<' + str(self.x) + ', ' + str(self.y) + '>'    
    
class Field(object):  
    
    def __init__(self):        
        self.drunks = {}   
        
    def addDrunk(self, drunk, loc):    
        if drunk in self.drunks:          
            raise ValueError('Duplicate drunk')   
        else:            
            self.drunks[drunk] = loc    
            
    def moveDrunk(self, drunk):    
        if not drunk in self.drunks:     
            raise ValueError('Drunk not in field')      
        xDist, yDist = drunk.takeStep()        
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)   
        
    def getLoc(self, drunk):       
        if not drunk in self.drunks:           
            raise ValueError('Drunk not in field')     
        return self.drunks[drunk] 
 
class Drunk(object): 
    
    def __init__(self, name):      
        self.name = name  
        
    def takeStep(self):         
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]    
        return random.choice(stepChoices)    

    def __str__(self):        
         return 'This drunk is named ' + self.name 
 
def walk(f, d, numSteps):    
    start = f.getLoc(d)    
    for s in range(numSteps):        
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d))) 
 
def simWalks(numSteps, numTrials):    
    homer = Drunk('Homer')     
    origin = Location(0, 0)     
    distances = []    
    for t in range(numSteps):       
        f = Field()        
        f.addDrunk(homer, origin)        
        distances.append(walk(f, homer, numTrials))     
    return distances 
 
def drunkTest(numTrials):     
    for numSteps in [10, 100, 1000, 10000, 100000]:      
        distances = simWalks(numSteps, numTrials)      
        print ('Random walk of ' + str(numSteps) + ' steps' )   
        print ('  Mean =', sum(distances)/len(distances)   )   
        print ('  Max =', max(distances), 'Min =', min(distances) )

 
m = Drunk("EGBEYONG TANJONG")    
print(drunkTest(10))









































       
        
        




