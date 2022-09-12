import time
# I'm Reilly and this program is a showcase for a Hangman-Type game.
# Currently it is just the stages, but I want to make it a full-fledged game, hence some of the commented code.

# This is to get the name of the player
name = input("What is your name? ")
print("Hey there!", name)
print("The hangman game is under construction, maybe you'll get to play it in a few weeks…")
print("This is what various stages of the hangman game will look like…")
# ignore the line below this, it is part of a side project I am working on with this program
# word = input("What is your word? ")

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
#This is to display the stages in order
for a in stages:
    time.sleep(3.5)
    print(a)
# Ignore everything below this point, I am working on making it a functioning game for fun
# for z in word:
#    guess = input("What is your 1 letter guess? ")
#    for x in word:
#        if x == guess:
#            print("Correct!")
#            break
#    else:
#        y=y+1
#        if y=1:
#            print (stg1)
#        else:
#            if y = 2:
#                print (stg2)