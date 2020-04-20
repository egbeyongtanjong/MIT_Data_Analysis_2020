# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:26:14 2020

@author: Egbeyong
Problem Set 3

6.00 wordgame
"""
"""
The rules of the game are as follows: 
Dealing 
•	A player is dealt a hand of n letters chosen at random (assume n=7 for now).
•	The player arranges the hand into as many words as they want out of the letters, but using each letter at most once. •	Some letters may remain unused (these won’t be scored). 
Scoring 
•	The score for the hand is the sum of the score for the words times the length of the word. •	The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first go. •	Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary  
SCRABBLE_LETTER_VALUES 
that maps each lowercase letter to its Scrabble letter value. 
•	For example, ‘weed’ would be worth 32 points ((4+1+1+2)*4=32), as long as the hand actually has 1 ‘w’, 2 ‘e’s, and 1 ‘d’. 
•	As another example, if n=7 and you get ‘waybill’ on the first go, it would be worth 155 points ((4+1+4+3+1+1+1)*7=105, +50) for the bonus of using all seven letters). 

We design test to test the individual modules(functions), this is called unit
testing

We will make modifications to ps3a.py to complete this project
"""



