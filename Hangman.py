#https://ascii.co.uk/art/hangman original source for hangman ascii inspiration
import time
# I'm Reilly and this program is a showcase for a Hangman-Type game.
# Currently it is just the stages, but I want to make it a full-fledged game, hence some of the commented code.

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

file_name = "EDMTDictionary.json"
if os.path.isfile(file_name) != True:
    retrieve_page('https://github.com/eddydn/DictionaryDatabase/raw/master/EDMTDictionary.json', file_name)
#else:
    #print("Already have the dictionary")

with open("EDMTDictionary.json") as json_dict:
    words_dict = json.load(json_dict)
    #print(type(words_dict))
    #print('There are {0} words in the file'.format(len(words_dict)))
    #print(words_dict[2584])
    #print(type(words_dict[2584]))  
    length = input("What is the length of the word? (Max of 23 letters) ")  
    desc = random.choice(words_dict)
    choice = desc['word']
    while len(desc['word']) != int(length):
        desc = random.choice(words_dict)
        choice = desc['word']
    #print('{}\n{}\n{}'.format(desc['word'], \
    #    desc['type'], desc['description']))

choice = choice.lower()
letters = [*choice]
letters2 = letters.copy()



#word = input("What is your word? ")

#These are the stages as Variables
stg0 = '''
     _________
     |/      |
     |      
     |      
     |       
     |      
     |
 jgs_|___'''
stg1 = '''
     _________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___'''
stg2 = '''
     _________
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 jgs_|___'''
stg3 = '''
     _________
     |/      |
     |      (_)
     |      /|
     |       |
     |      
     |
 jgs_|___'''
stg4 = '''
     _________
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      
     |
 jgs_|___'''
stg5 = '''
     _________
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      / 
     |
 jgs_|___'''
stg6 = '''
     _________
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      / \\
     |
 jgs_|___'''
stages = [stg0, stg1, stg2, stg3, stg4, stg5, stg6]

def death():
    print('{}\n{}\n{}'.format(desc['word'], \
        desc['type'], desc['description']))
    print("You Lose!")
    exit()

def hangman():
    hungmen = 0
    wrong = []
    guesses = []
    for i in range(len(letters)):
        guesses.append(" ")
    while True:
        if hungmen == 6:
            death()
        guess = input("What is your 1 letter guess? ")
        guess = guess.lower()
        for x in letters:
            if x == guess:
                index = letters.index(x)
                letters[index] = ""
                print(stages[hungmen])
                guesses[index] = x
                print(guesses)
                print("Wrong:", wrong)
                print("Correct!")
                
        if guess not in letters2:
            hungmen += 1
            print(stages[hungmen])
            print(guesses)
            wrong.append(guess)
            print("Wrong:", wrong)
        if guesses == letters2:
            print("You win!")
            print('{}\n{}\n{}'.format(desc['word'], \
        desc['type'], desc['description']))
            break
                
hangman()
    #else:
     #   y = y+1
      #  if y==1:
       #     print (stg1)
        #else:
         #   if y == 2:
          #      print (stg2)
