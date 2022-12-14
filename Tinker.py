myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

oldfile = open("test.txt", "r")
a = oldfile.readlines()
oldfile.close()

a.reverse()
newfile = open("test.txt", "w")
for v in a:
    newfile.write(v)
newfile.close()

newfile = open("test.txt", "r")
while True:                            # Keep reading forever
    theline = newfile.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    print(theline, end="")

newfile.close()