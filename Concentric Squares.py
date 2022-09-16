import turtle
 
def draw_square(a,size):
     for i in range(4):
         a.forward(size)
         a.left(90)
wn = turtle.Screen()        
wn.bgcolor("lightgreen")
wn.title("Russian Nesting Squares")

alex = turtle.Turtle()      # Create alex      
alex.pensize(3)
alex.pencolor("hotpink")

size=20             # Size of the smallest square
for i in range(5):
    draw_square(alex, size)
    size = size + 20        # Increase the size for next time
    # Scooch it over so the Squares encapsualte the others
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()
    

wn.mainloop()