from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    max_word_score = 0
    max_word = ''
    words = []
    words_in_wordsList = []
    for num in range (1,len(hand.keys())+1):
        words.append(get_perms(hand,num))
    #print(words)
    
    for values in words:
        for val in values:
            if val in word_list:
                words_in_wordsList.append(val)
    #print(words_in_wordsList)
    
    for word in words_in_wordsList:
        word_score = get_word_score(word, HAND_SIZE)
        if word_score > max_word_score:
            max_word = word
            max_word_score = word_score
    #print(max_word)
    return max_word
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    total_score = 0
    word_score = 0
    
    while calculate_handlen(hand) > 0:
        print("Current Hand: ", end = " ")
        display_hand(hand)
        print()
        #word = input("Enter word, or a \".\" to indicate that you are finished: " )
        word = comp_choose_word(hand, word_list)
        if word != None and is_valid_word(word, hand, word_list):
            word_score = get_word_score(word, HAND_SIZE)
            total_score += word_score
            print("\"",word,"\" earned ", word_score, "points. Total:",total_score)
            print()
            word_score = 0
        else:
            print("Out of words.")
            print()
            break

    
#
# Problem #6C: Playing a game
#
#
  

"""   
def play_game(word_list):
    
"""   
"""Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
"""
    
"""
    # TO DO...
    temp ={}
    count = 0
    game_test = True
    
    while game_test:
        first_value = input("Enter 'a' or 'u' or 'c': ") 
        
        #Gives the opportunity for the user to play
        if first_value == 'u':
            while game_test:
                value = input("Enter 'n' or 'r' or 'e': ")
        
                if value == 'n':
                    hand = deal_hand(HAND_SIZE)
                    temp = hand.copy()
                    play_hand(hand,word_list)
                    print()
                    print("New Game")
                    count += 1
   
                elif value == 'r':
                    if count != 0:
                        play_hand(temp,word_list)
                        print()
                        print("New Game")
                    else:
                        print("There has been no previous hand dealt")
            
                elif value == 'e':
                    print("Exiting game...Goodbye")
                    game_test = False
                else:
                    game_test = True
        #Gives the opportunity for the computer to play
        elif first_value == 'c':
            comp_play_hand(hand, word_list)
            print()
        else:
            game_test = True
    
    
    
"""
 
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    #hand = deal_hand(HAND_SIZE)
    word_list = load_words()
    #play_game(word_list)
    #comp_choose_word(hand, word_list)
    #comp_play_hand(hand, word_list)
    play_game(word_list)

    
