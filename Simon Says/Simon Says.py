#I'm Reilly Prescott and this is my Simon Says program
lines = input()     #How many lines of instructions do you want
text = ''
def Simon():
              
        global text
        if text.find("Simon says ") == 0:   #Does Simon say?
            text = text.replace("Simon says ",'')   #If Simon says, then print and return a command
            print(text)
            return(text)
        else:
            if text.find("Simon says ") != 0:   #If Simon doesn't say, then return an empty line
                print("")
                return("") 
for i in range(int(lines)):
    text = input()     #Input your instructions
    Simon()

#Prepare and execute assert statements
lines = 1
text = "Simon says jump"
print("assert 1")
assert(Simon() == "jump")

text = "Simon says spin"
print("assert 2")
assert(Simon() == "spin")

text = "Simon don't says"
print("assert 3")
assert(Simon() == "")