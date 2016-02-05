# 6.00 Problem Set 3
# 
# Hangman
#
# Problem Set 2 
# Name: AC 
# Collaborators (Discussion): -
# Collaborators (Identical Solution): -
# Time: 1:30 
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
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def is_letter_remaining(letter, abc):
    pass

def find_occurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def main():
    print "Welcome to the game, Hangman!"
    the_word = choose_word(wordlist)
    wlen = len(the_word)

    # initialise list to undescores
    hidden_word = []
    for i in range(0, wlen):
        hidden_word.append('_')

    print "I am thinking of a word that is %d letters long. (%s)" % (wlen, "")

    won = False
    guesses_remain = wlen * 2
    letters_remain = "abcdefghijklmnopqrstuvwxyz"

    while guesses_remain > 0 and won != True:
        print "-------------"
        print "You have %d guesses left." % guesses_remain
        print "Available letters: %s" % letters_remain

        invalid_in = True
        while invalid_in:
            letter_in = raw_input("Please guess a letter: ").lower()
            if len(letter_in) == 1:
                break

        # input is a remaining letter
        if letters_remain.find(letter_in) != -1:
            # remove letter from remaining letters
            letters_remain = letters_remain.replace(letter_in, '')
            guesses_remain -= 1

            # and in the word
            if the_word.find(letter_in) != -1:
                # reveal found letters
                for i in find_occurences(the_word, letter_in):
                    hidden_word[i] = letter_in
                print "Good guess: ",
            else:
                print "Oops! That letter is not in my word: ",
      
            str_hidden_word = "".join(hidden_word)
            print str_hidden_word

            if str_hidden_word == the_word:
                won = True
        else:
            print "Already used '%s'." % letter_in

    if won == True:
        print "Congratulations!"
    else:
        print "Better luck next time. The word was %s" % the_word

main()
