# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:06:24 2020

@author: Egbeyong
Lecture 10

"""
"""
Hashing is how dictionaries are implemented in python. They lead to efficient 
search, but at the cost of space

Hashing uses a hash function to convert data and store in a bucket, or a list 
in a list of lists.

Now since we can find the ith element of a list in constant time, it makes
hashing efficient. Whenever we want to find out if an element is in 
a set, we can hash it and go directly to the bucket where this element is
and search it.

collisions occur when different elements hash to thesame bucket. We can 
handle collisions using linear rehashing 

If you have a million buckets, there will be alot fewer collisions than
if you have two buckets

A good hash function has the property that it will widely disperse the 
values you have. For example modulo of 100, will be a good hash function
for numbers in the range 1 - 100

Anykind of immutable objects can be hashed. In Python for example
keys in dicts have to be immutable coz, imagne that a key was a list
then if it is is mutated, the value in the dict is lost forever.

Unhandled exceptions cause programs to crash.

We use exceptions by means of try-except blocks

A module is a collection of related functions
For example the math module, that provided 
us with functions like math.log

A class is like a module, but it is not just a collection of functions

It is a collection of data and functions, functions that operate on 
the data

The data and functions associated with an object are called the object's 
attributes

In python everything is an object, including the class itself. 

We can use to introduce new types into the programming environment







"""
"""
# Hashing broken down

numBuckets = 47 

#Function to create a bucket oR lists of lists
def create():
    numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    return hSet
"""
"""
#Hash fuction, takes element and returns an int between 0 and numBuckets minus 1
def hashElem(e):
    numBuckets
    return e%numBuckets
"""
"""
#Inserts an element 
def insert(hSet, i):
    hSet[hashElem(i)].append(i)

# Remove and element
def remove (hSet, i):
    newBucket = []
    for j in hSet[hashElem(i)]:
        if j != i:
            newBucket.append(j)
    hSet[hashElem(i)] = newBucket

# Checks for membership
def member(hSet, i):
    return i in hSet[hashElem(i)]    


def test1():
    s = create()
    for i in range(40):
        insert(s, i)
    print(s)
    insert(s, 325)
    insert(s, 325)
    insert(s, 987654321)
    print(s)
    print(member(s, 325))
    remove(s, 325)
    print(member(s, 325))
    print(member(s, 987654321))
    
#test1()

#More sophisticated hash function
def hashElem(e):    
    numBuckets    
    if type(e) == int:        
        val = e     
    if type(e) == str:       
    #Convert e to an int       
        val = 0        
        shift = 0         
        for c in e:         
            val = val + shift*ord(c)
            shift += 1    
    return val%numBuckets 
 
def test2():    
    d = create()    
    strs = ['ab', 'ba', '32a',\
            'big dog', 'small bird'] 
    for s in strs:        
        insert(d, s)     
    for i in range(40):        
        insert(d, i)     
    print(d)     
    print(member(d, 'small bird'))   
    print(member(d, 'big bird'))   
    remove(d, 'small bird')  
    print(d) 

test2()

"""

#Exploring the use of exceptions
def readVal(valType, requestMsg, errorMsg):
    numTries = 0
    while numTries < 4:
        value = input(requestMsg)
        try:
            value = valType(value)
            return value
        except ValueError:
            print(errorMsg)
            numTries += 1
    raise TypeError('Num tries exceeded')
#print(readVal(int, 'Enter int: ','Not an int.'))
try:
    readVal(int, 'Enter int: ', 'Not an int.')
except TypeError:
    print('Not an int')














