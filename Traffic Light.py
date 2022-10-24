import turtle           # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

tess.penup()
tess.forward(-40)
tess.pendown()

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


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
tess.end_fill()

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0

green_light = turtle.Turtle()
yellow_light = turtle.Turtle()
red_light = turtle.Turtle()

green_light.shape("circle")
yellow_light.shape("circle")
red_light.shape("circle")

green_light.shapesize(3)
yellow_light.shapesize(3)
red_light.shapesize(3)
green_light.penup()
yellow_light.penup()
red_light.penup()

green_light.fillcolor("Dark Olive Green")
yellow_light.fillcolor("Brown")
red_light.fillcolor("Sienna")


# Turn them all to face upward.
green_light.left(90)
yellow_light.left(90)
red_light.left(90)

# Walk them to their places
green_light.forward(50)
yellow_light.forward(190)
red_light.forward(120)

def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()                      # Listen for events
wn.mainloop()