#https://ascii.co.uk/art/hangman original source for hangman ascii inspiration
import time
# I'm Reilly and this program is a showcase for a Hangman-Type game.

# This is to get the name of the player
name = input("What is your name? ")
print("Hey there!", name)


import json
import os
import random
from urllib import request

def retrieve_page(url, file_name):
    """Download the contents of a web page.
    """
    response = request.urlretrieve(url, file_name)

# This retrieves the dictionary
file_name = "EDMTDictionary.json"
if os.path.isfile(file_name) != True:
    retrieve_page('https://github.com/eddydn/DictionaryDatabase/raw/master/EDMTDictionary.json', file_name)
#else:
    #print("Already have the dictionary")


   
#These are the stages as Variables
stg0 = '''
     _________
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___'''
stg1 = '''
     _________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|___'''
stg2 = '''
     _________
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 ____|___'''
stg3 = '''
     _________
     |/      |
     |      (_)
     |      /|
     |       |
     |      
     |
 ____|___'''
stg4 = '''
     _________
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      
     |
 ____|___'''
stg5 = '''
     _________
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      / 
     |
 ____|___'''
stg6 = '''
     _________
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      / \\
     |
 ____|___'''
stg7 = '''
     _________
     |/      |
     |     (x_x)
     |      /|\\
     |       |
     |      / \\
     |
 ____|___'''
stages = [stg0, stg1, stg2, stg3, stg4, stg5, stg6, stg7]

def again():
    YN = input("Play again? (Y/N) ",)
    YN = YN.upper()
    if YN == "Y":
        hangman()
    elif YN == "N":
        exit()
    elif YN != "Y" or "N":
        again()







# This is our main function
def hangman():

    def death():
        # This defines the state of losing the game
        print('{}\n{}\n{}'.format(desc['word'], \
        desc['type'], desc['description']))
        print("You Lose!")
        again()
    # This chooses the word
    with open("EDMTDictionary.json") as json_dict:
        words_dict = json.load(json_dict)
        #print(type(words_dict))
        #print('There are {0} words in the file'.format(len(words_dict)))
        #print(words_dict[2584])
        #print(type(words_dict[2584]))  
        length = input("What is the length of the word? (Max of 21 letters) ")  
        desc = random.choice(words_dict)
        choice = desc['word']
        while len(desc['word']) != int(length):
            desc = random.choice(words_dict)
            choice = desc['word']
        #print('{}\n{}\n{}'.format(desc['word'], \
        #    desc['type'], desc['description']))

    # This makes sure the choice is lowercase and creates a second list to work with
    # The first list is used as a reference
    choice = choice.lower()

    letters = [*choice]
    letters2 = letters.copy()


    #This sets up the failed attempts, wrong guesses, and list of letters
    hungmen = 0
    wrong = []
    guesses = []
    # This makes the length of open spaces in the word equal to the amount of guesses
    # I did it this way to show the place of the letter in the word
    for i in range(len(letters)):
        guesses.append(" ")
    while True:
        # This ends the game
        if hungmen == 7:
            death()
        # Here is where you guess (the guess is also converted to lowercase)
        guess = input("What is your 1 letter guess? ")
        guess = guess.lower()
        # This checks the guess against the word, removes them from our copied list, and adds them to our guesses in the correct spot.
        # It also displays the current state of our man, our word, and our incorrect guesses
        for x in letters:
            if x == guess:
                index = letters.index(x)
                letters[index] = ""
                print(stages[hungmen])
                guesses[index] = x
                print(guesses)
                print("Wrong:", wrong)
                print("Correct!")
                
        # This catches the incorrect guesses and appends the wrong list, it also helps hang our man and shows the state of the game
        if guess not in letters2:
            hungmen += 1
            print(stages[hungmen])
            print(guesses)
            wrong.append(guess)
            print("Wrong:", wrong)
        # This checks if we should win. If so, it stops the loop, tells us what the word was, and its meaning, then ends the game.
        if guesses == letters2:
            print("You win!")
            print('{}\n{}\n{}'.format(desc['word'], \
        desc['type'], desc['description']))
            again()
            break
                
hangman()