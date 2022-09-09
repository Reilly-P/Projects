import turtle
wn = turtle.Screen()
wn.title = ("Hello Ricky!")
Ricky = turtle.Turtle()
Ricky.forward(250)
for i in range(5):
    Ricky.right(144)
    Ricky.forward(500)

wn.mainloop()
