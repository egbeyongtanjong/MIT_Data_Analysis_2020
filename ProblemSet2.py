# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 06:21:46 2020

@author: Egbeyong

Solutions to problem Set 2
Successive Approximation and a Wordgame!
"""
#********************************************************************
"""
Problem #1

This function evaluates a polynomial function for the given x value
Computes the polynomial function for a given value x. Returns that 
value. Example: 
>>> poly = (0.0, 0.0, 5.0, 9.3, 7.0) # f(x) = 7.0x4 + 9.3x3 + 5.0x2 
>>> x = -13 
>>> print evaluate_poly(poly, x) # f(-13) = 7.0(-13)4 + 9.3(-13)3 + 5.0(-13)2 
180339.9 
poly: tuple of numbers, length > 0 
x: number 
returns: float    
"""

def evaluate_poly(poly,x):
    result = 0.0
    for num in range(0,len(poly)):
        result += x**num * poly[num]
    return result

poly = (0.0, 0.0, 5.0, 9.3, 7.0)
x = -13
print(evaluate_poly(poly, x))

#*******************************************************************
"""
Problem #2

This function computes the derivative of a polynomial function
Computes and returns the derivative of a polynomial function. If the
derivative is 0, returns (0.0,).
>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0) # x4 + 3.0x3 + 17.5x2 - 13.39 
>>> print compute_deriv(poly) # 4.0x3 + 9.0x2 + 35.0x 
(0.0, 35.0, 9.0, 4.0)
poly: tuple of numbers, length > 0
returns: tuple of numbers

"""
def compute_deriv(poly):
    derivative = ()
    for num in range(0, len(poly)):
        if num == 0:
            continue
        elif num == 1:
            derivative += (poly[num],)
        else:
            derivative += (poly[num]*(num),)
    return derivative
poly = (-13.39, 0.0,17.5,3.0,1.0)
print(compute_deriv(poly))

#*****************************************************************
"""
Problem #3 

This method applies Newton's method of successive approx to find the 
root of a polynomial
Uses Newton's method to find and return a root of a polynomial function.
Returns a tuple containing the root and the number of iterations required to
get to the root.
Example:
>>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0) #x4 + 3.0x3 + 17.5x2 - 13.39 
>>> x_0 = 0.1 
>>> epsilon = .0001
>>> print compute_root(poly, x_0, epsilon)
(0.80679075379635201, 8)
poly: tuple of numbers, length > 1.
Represents a polynomial function containing at least one real root.
The derivative of this polynomial function at x_0 is not 0.
x_0: float 
epsilon: float > 0
returns: tuple (float, int)

"""
#****************************************************************
def compute_root(poly,x_0,epsilon):
    count = 0
    sum1 = 0+1
    sum2 = 0
    while abs(sum1)>epsilon:
        sum1 = evaluate_poly(poly,x_0)
        if abs(sum1)<epsilon:
            count += 1
            break
        else:
            count += 1
            sum2 = evaluate_poly(compute_deriv(poly),x_0)
        x_0 = x_0 - sum1/sum2
    return (x_0, count)
poly=(-13.39,0.0,17.5,3.0,1.0)
x_0=0.1
epsilon=.0001
print(compute_root(poly,x_0,epsilon))
#****************************************************************
"""
Problem#4

Implement a function, hangman(), that will start up 
and carry out an interactive Hangman game between a player and the computer. 

"""
# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def available_letters(availableLetters,guess,word):
    """

    Returns the letters of the alphabet minus a correct guessed letter
    """
    
    for char in word:
        if guess == char:
            availableLetters = availableLetters.replace(char,'')
    return availableLetters

def word_check(guess,word,curr):
    count1 = 1
    count2 = count1
    if guess not in word:
        print("Oops! That letter is not in my word:", curr)
    else:
        for char in word:
            if guess == char:
                for x in range(0, len(word)):
                    if word[x] == char and curr[x]=='-' and count1 == count2:
                        curr = curr[:x] + guess + curr[x+1:]
                        print("Good guess:", curr)
                        count2 += 1
                        break
        
        if curr == word:
            print("Congratulations, you won")
        
    return curr
# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
    
wordlist = load_words()
word = choose_word(wordlist)

#word = 'good'
curr = ''
for x in range(0,len(word)):
    curr += '-'
num_guesses = len(word)+4
availableLetters = "abcdefghijklmnopqrstuvwxyz"
# your code begins here!
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is ", len(word)," letters long.")
print("-------------")
guess = ''

while num_guesses > 0 and curr!=word:
    print("You have ", num_guesses," guesses left.")
    availableLetters = available_letters(availableLetters,guess, word)
    print("Available letters: ",availableLetters)
    guess = input("Please guess a letter: ")
    curr = word_check(guess,word,curr)
    print("-------------")
    num_guesses -= 1
print("The word was: ", word)    









