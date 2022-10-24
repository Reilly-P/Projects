import turtle

def draw_housing():
    """Draw a nice housing to hold the traffic lights."""
    tess.pensize(3)
    tess.color("black", "Dim Grey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

def advance_state_machine():
    """Move stoplight on to the next state.

    States 0, 1, 2 correspond to green, yellow, red
    in a standard traffic light.
    """
    global state_num
    if state_num == 0:       # Transition from 'green' to 'yellow'
        green_light.color("Dark Olive Green")
        yellow_light.color("Orange")
        state_num = 1
    elif state_num == 1:     # Transition from 'yellow' to 'red'
        yellow_light.color("Sienna")
        red_light.color("red")
        state_num = 2
    elif state_num == 2:       # Transition from 'red' to 'green'
        red_light.color("Brown")
        state_num = 0
        green_light.color("Lime Green")
    else:
        print("Uh oh. Problem in the state machine.")

    wn.ontimer(advance_state_machine, 1000)

# Set up turtles and screen to work with.
# Tess will draw the housing, and
# turtles with obvious names will serve as lights.

# Set up tess.
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

# Draw the housing and move tess into position.
tess.penup()
tess.forward(-40)
tess.pendown()

draw_housing()
tess.penup()
tess.hideturtle()

# Set up tess's three counterparts.
green_light = turtle.Turtle()
yellow_light = turtle.Turtle()
red_light = turtle.Turtle()

# Make them the appropriate colors and such
green_light.shape("circle")
yellow_light.shape("circle")
red_light.shape("circle")

green_light.shapesize(3)
yellow_light.shapesize(3)
red_light.shapesize(3)

# The three lights shouldn't draw anything, so
# let's preemptively stop them.
green_light.penup()
yellow_light.penup()
red_light.penup()

green_light.fillcolor("Dark Olive Green")
yellow_light.fillcolor("Sienna")
red_light.fillcolor("Brown")


# Turn them all to face upward.
green_light.left(90)
yellow_light.left(90)
red_light.left(90)

# Walk them to their places
green_light.forward(50)
yellow_light.forward(120)
red_light.forward(190)

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine.
state_num = 0

wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()