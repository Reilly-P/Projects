import turtle
tess= turtle.Turtle()
xs = [48, 117, 200, 240, 160, 260, 220]
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.right(90)
    t.forward(40)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.forward(10)         # Leave small gap after each bar

...
for v in xs:              # Assume xs and tess are ready
    draw_bar(tess, v)

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    if height >= 200:
        tess.color("blue", "red",)
    elif height > 100 and height < 200:
        tess.color("blue", "yellow",)
    elif height < 100:
        tess.color("blue", "green",)

    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()