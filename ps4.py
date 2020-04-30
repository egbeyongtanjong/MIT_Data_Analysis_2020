# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
# Completed by Egbeyong Tanjong
#
import string
import random
import re

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.
    alphabet = {}
    
    #Fills alphabet dictionary with uppercase characters
    for i in range (65,91):
        alphabet[chr(i)] = chr(i)
    
    #Adds space character to alphabet dictionary
    alphabet[' ']=' '
    
    #Adds lowercase characters to alphabet dictionary
    for i in range (97,123):
        alphabet[chr(i)] = chr(i)

    
    if shift == 0:
        return alphabet
    
    elif shift > 0:
    #ASCII characters and numbers A=65, Z=90, a=97, z=122
    #use chr(int) to convert from 
        if shift < 0:
            shift = abs(shift)
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
                    temp[key] = alphabet[chr(val + 27)]
            else:
                temp[key] = alphabet[chr(122 - abs(shift) + 1)]
    
    return temp

    

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    
    temp = build_coder(shift)
    
    return temp
    
def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    shift = -int(shift)
    temp = build_coder(shift)
    return temp

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    ### TODO.
    newStr = ''
    ref = coder
    for c in text:
        if c in ref.keys():
            newStr += ref[c]
        else:
            newStr += c
    return newStr
    
  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ### TODO.
    return apply_coder(text, build_encoder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    ### TODO
    max_num = 0
    best_shift = 0
    count = 0
    res = []
    s = ''
    
    #Creates all 27 possible decoder alphabets 
    for i in range(0,27):
        s = apply_coder(text, build_decoder(i))
        
        #removes all non alphanumeric characters
        # \W == [^a-zA-Z0-9_]
        s = re.sub(r'\W+', ' ', s)
        #print(s)
        
        res = s.split( )
        #print(res)
        for word in res:
            if word in wordlist:
               # print(word)
                count += 1
        if count > max_num:
            max_num = count
            best_shift = i
           # print(max_num)
        count = 0   
        #print(max_num)
    return best_shift
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    for tup in shifts:
        if tup[0] == 0:
            text = apply_shift(text,tup[1])
        else:
            text = text[0:tup[0]]+apply_shift(text[tup[0]:],tup[1])
    return text
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    tup = []
    start = 0
    s = text
    
    #print(start_positions)
    while start < len(s):
            #s = text[start:]
            guess1 = find_best_shift(wordlist,s)
            print(guess1)
            guess = find_best_shifts_rec(wordlist,s,0)
            #guess1 = find_best_shift(wordlist,s)
            
            #print(guess1)
            #print(guess)
            
            s = apply_coder(s, build_decoder(guess[1]))
            tup.append((guess))
            m = ' '
            m = apply_coder(m, build_coder(guess[1]))
            
            for i in range(len(s)):
                if s[i] == m:
                    start = i+1
                    break
                else:
                    start = len(text)
            s = s[start:]
            
            
    return tup
    
    
    

def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    ### TODO.
    
    
    shift = find_best_shift(wordlist,text[start:])
    
    return (start, shift)


def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.



    
#What is the moral of the story?
#
#
#
#
#

"""
#TEST commands
text = "This is a test."

#print(apply_shift(text,8))
#s = apply_coder('Hello, world!', build_encoder(8))
s = apply_coder("Do Androids Dream of Electric Sheep?", build_encoder(6))
print(s)
guess = find_best_shift(wordlist, s)
print(guess)

print(apply_coder(s, build_decoder(guess)))
"""
"""
s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
print()
print(s)

"""

#Next test
s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
print(s)
shifts = find_best_shifts(wordlist, s) 
shifts = find_best_shift(wordlist, s) 
print(shifts)
print (apply_shifts(s, shifts))


"""
#Yet another test case
s = random_scrambled(wordlist, 3) 
print(s)
shifts = find_best_shifts(wordlist, s)
print(shifts)
print(apply_shifts(s, shifts))
"""




