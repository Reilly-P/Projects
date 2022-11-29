#https://ascii.co.uk/art/hangman original source for hangman ascii inspiration
import time
# I'm Reilly and this program is a showcase for a Hangman-Type game.
# Currently it is just the stages, but I want to make it a full-fledged game, hence some of the commented code.

# This is to get the name of the player
name = input("What is your name? ")
print("Hey there!", name)
print("The hangman game is under construction, maybe you'll get to play it in a few weeks…")
print("This is what various stages of the hangman game will look like…")

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
    desc = random.choice(words_dict)
    choice = desc['word']
    while len(desc['word']) > 5:
        desc = random.choice(words_dict)
        choice = desc['word']
    print('{}\n{}\n{}'.format(desc['word'], \
        desc['type'], desc['description']))

letters = [*choice]
print(letters)



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
stages = [stg1, stg2, stg3, stg4, stg5, stg6]


def hangman():
    previndex = -1
    guesses = []
    for z in letters:
        guess = input("What is your 1 letter guess? ")
        for x in letters:
            if x == guess:
                index = letters.index(x)
                if index < previndex:
                    guesses.insert(0,x)
                elif previndex < index:
                    guesses.append(x)
                print("Correct!")
                
    print(guesses)
hangman()
    #else:
     #   y = y+1
      #  if y==1:
       #     print (stg1)
        #else:
         #   if y == 2:
          #      print (stg2)