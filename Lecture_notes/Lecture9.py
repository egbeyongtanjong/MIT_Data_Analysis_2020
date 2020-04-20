# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:43:00 2020

@author: Egbeyong

Lecture 9
Memory and search methods
"""
"""
So to simply search a list takes linear time. Since you can go through every
element worst case to find out the element you are searching for.

Alternatively, binary search takes log n time, since the list is 
halfed at every turn. The issue with binary search is that it 
depends on the list being sorted

Now the problem is can the list be sorted fast enough so that 
the sort algorithm, plus the binary search algorithm end up taking
sub-linear time?

The answer is no!

sorting is bounded by at least L, were L is the length of list
Infact, to sort, you need to visit every element

This therefore begs the question, why is sorting before binary search
still useful?

The answer is AMORTIZED COMPLEXITY
The cost for sorting a list once can be shared over the multpile 
times the list is searched using binary search

and that new cost per binary serach apres sorting is sublinear
















"""
