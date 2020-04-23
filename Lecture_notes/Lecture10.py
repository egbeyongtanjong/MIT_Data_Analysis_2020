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
"""
