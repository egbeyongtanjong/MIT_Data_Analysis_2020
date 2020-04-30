# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 07:26:43 2020

@author: Egbeyong
"""
"""
#Replacing a word in a string
guess = 'e'
name = 'Egbeyong'
for char in name:
    if char == guess:
        name = name.replace(char,'')
        print(name)
"""
"""
word = 'dog'
curr = '---'
guess = 'o'
for char in word:
        if guess == char:
            for x in range(0, len(word)):
                if word[x] == char:
                    curr = curr[:x] + guess + curr[x+1:]
            print("Good guess:", curr)

#Recursion

def exp(b,n):
    if n==1:
        return b
    else:
        return(b * exp(b,(n-1)))

print(exp(2,4))

s = 'JJoey'
print(s[1:-1])
"""
"""
hand= {'d':2,'o':1,'g':3}
word = 'dog'
for c in word:
    hand[c] = hand.get(c,0)
    hand[c] -= 1
print(hand.values())
print(len(hand.keys()))

"""
"""
#finding the words that match a string in a wordlist
def findAll (wordList, lStr):
    result = []
    str = ''
    for word in wordList:
        if len(word) == len(lStr):
            for char in word:
                if char in lStr:
                    str += char
            result.append(str)
            str = ''
    return result

wordList = ("bat","tab","please")
lStr = ('atb')

print(findAll(wordList,lStr))
"""
"""
def addVectors(v1, v2):    
"""
    #assumes v1 and v2 are lists of ints.     
    #Returns a list containing the pointwise 
    #sum of        the elements in v1 and v2.  
    #For example,        addVectors([4,5], [1,2,3]) 
    #returns [5,7,3],and        addVectors([], []) 
    #returns []. Does not modify inputs.
"""   

    if len(v1) > len(v2):   
        result = v1.copy()        
        other = v2     
    else:        
        result = v2.copy()     
        other = v1    
    for i in range(len(other)):        
        result[i] += other[i]    
    return result 
v1 = [4,5]
v2 = [1,2,3]

print(addVectors(v1,v2))
print(v1)
print(v2)

"""
"""
def f(s, d):     
    for k in d.keys():        
        d[k] = 0     
    for c in s:       
        if c in d:           
            d[c] += 1       
        else: d[c] = 0    
    return d 
 
def addUp(d):    
    result = 0    
    for k in d:         
        result += d[k]     
    return result 
 
d1 = {} 
d2 = d1 
d1 = f('abbc', d1) 
print (addUp(d1)) 
d2 = f('bbcaa', d2) 
print (addUp(d2)) 
print (f('', {})) 
print (result) 
"""


"""
def logBase2(n): 
"""
"""

assumes that n is a positive int      
returns a float that approximates the log base 2 of n
    
"""
"""
    import math     
    return math.log(n, 2) 
 
def f(n):  
    """
"""assumes n is an int"""   
"""
    if n < 1:        
        return     
    curDigit = int(logBase2(n))   
    ans = 'n = '    
    while curDigit >= 0:      
        if n%(2**curDigit) < n:         
            ans = ans + '1'           
            n = n - 2**curDigit       
        else:            
            ans = ans + '0'        
        curDigit -= 1    
    return ans 
 
for i in range(3):     
    print (f(i))

"""
"""
#showing what happens to dictionaries with dupicated keys
hand= {'d':2,'o':1,'g':3,'d':2}
print(hand['d'])
"""

"""
alphabet = {}
shift = 3

for i in range (65,91):
    alphabet[chr(i)] = chr(i)

alphabet[' ']=' '

for i in range (97,123):
    alphabet[chr(i)] = chr(i)
print(alphabet)

if shift == 0:
    print(alphabet)

elif shift > 0:
    temp = alphabet.copy()
    for key in alphabet.keys():
        if key != ' ' and ord(key) <= 90 - shift:
            temp[key] = alphabet[chr(shift+ord(key))]
        elif key != ' ' and ord(key) <= 90:
            val = shift+ord(key)
            if val == 91:
                temp[key] = ' '
            else:
                temp[key] = alphabet[chr(val%90 + 63)]
        elif key != ' ' and ord(key) <= 122 - shift:
            temp[key] = alphabet[chr(shift+ord(key))]
        elif key != ' ' and ord(key) <= 122:
            val = shift+ord(key)
            if val == 123:
                temp[key] = ' '
            else:
                temp[key] = alphabet[chr(val%122 + 95)]
        else:
            temp[key] = alphabet[chr(97+shift-1)]

else:
    temp = alphabet.copy()
    for key in alphabet.keys():
        if key != ' ' and ord(key) - abs(shift) >= 97:
            temp[key] = alphabet[chr(ord(key)-abs(shift))]
        elif key != ' ' and ord(key) > 96 and ord(key) - abs(shift) > 70:
            val = ord(key) - abs(shift)
            if val == 96:
                temp[key] = ' '
            else:
                temp[key] = alphabet[chr(val + 27)]
        elif key != ' ' and ord(key) - abs(shift) >= 65:
            temp[key] = alphabet[chr(ord(key)-abs(shift))]
        elif key != ' ' and ord(key) - abs(shift) > 38:
            val = ord(key) - abs(shift)
            if val == 64:
                temp[key] = ' '
            else:
                print(val)
                temp[key] = alphabet[chr(val + 27)]
        else:
            temp[key] = alphabet[chr(90 - abs(shift) + 1)]
    
    
    
    
    
text = "The goal is to become good"
text = "QebXdlyiXfpXqlXzb ljbXdlla"   
print(temp)

newStr = ' '
ref = temp
for c in text:
    if c in ref.keys():
        newStr += ref[c]
    else:
        newStr += c
    #return newStr

print(newStr)
"""
"""
s = "Good morning"
s = s[0:2] + s[5]
print(s)


start_positions = [0]
s = "The boy is good"
for i in range(len(s)):
    if s[i] == ' ':
        start_positions.append(i+1)
print(start_positions)
"""

s = [1,2,3,1,5]

d = list(set(s))

print(s)
print(d)




