#My name is Reilly Prescott and this is my Number Guess program
import random
number = random.randrange(1,20)
name = input("What's your name? ", )
print("Hello", name,",","welcome to my number guess game!")
w = 0
l = 0
t = 0
def again():
    again = input("Shall we go again? (Y/N) ", )
    if again == "Y":
        numgame()
    elif again == "N":
        print("You played a total of", t,"games, won", w,"of them, and lost", l,"of them")

def numguess():
    global guess
    guess = int(input("Guess a number between 1 and 20: ",))
    if guess < 1 or guess > 20:
        print("Guess again!")
        guess = int(input("Guess a number between 1 and 20: ",))
    if guess == number:
        print("Correct!")
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
def numgame():
    i = 7
    while i > (0):
        numguess()
        if guess == number:
            print("You win! The secret number was:", number)
            global w
            global t
            w += 1
            t += 1
            again()
            return
        else:
            i -= 1
            print("You have", i, "guesses remaining!")
            if i == 0:
                print("You lose!")
                global l
                l += 1
                t += 1
                again()
                return

numgame()
