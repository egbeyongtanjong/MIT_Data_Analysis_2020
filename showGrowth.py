# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:41:35 2020

@author: Egbeyong
Lecture 8
"""
"""
Efficiency is important coz some computational problems are enormous, not 
only large. 

Efficiency matters as we see the scale of problems increasing

Efficiency is about algorithms, not coding details

Clever algorithms are hard to invent, so our focus is not on being
able to develop them. Our focus is being able to reduce problems
to previously solved problems. We try to fit our problems
into some clever model that already has a solution.

We think about efficiency in terms of space and time. And we can often
trade one for the other. 

We can make a program run faster by using more memory, or use less memory 
at the cost of making it run more slowly

Let us focus on time for now.

So to be able to talk about measuring the time it takes to for
an algorithm to run more abstractly, we use count the number
of basic steps.

we do this because the running time of algorithms depends on the 
speed of machines, size of input...all variables which make using
run time as a measure for speed unstable.

Steps are operations that take constant time. They are not variable
they are constants. 

the random access model uses the assumption that:
1. instructons are executed one after another (though there may be 
prallelism) [sequentially]
2.  Constant time is required to access memory (in the days of tapes,
it will take longer to access objects located at the end of the tape)
Also, with today's hierachies (cache...) it is still faster
to access some memory than others

complexity analysis almost always focuses on the worst case
Since figuring out the epected (average) case is usually not feasible

The worse case provides an upper bound. Which represents how bad things
 can get
 
The worst case is really the right one to wory about. Coz we believe
in Murphy's law. if something can go wrong, it will

When we analyze algorithms (look at complexity) we are concerned with the growth
of the algorithm with respect to the input size, so the additive constants
can be ignored, since they really stay thesame regarless of the input
size


   
    








"""
