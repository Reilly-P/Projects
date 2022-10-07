import random
import math
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
print("start")
iterations = 1000000
height = 600
width = 1000

window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width//2, height//2), image=img, state="normal")

def mid_point(point1, point2):
    midx = (point1[0]+point2[0])/2
    midy = (point1[1]+point2[1])/2
    mid_point = [midx, midy]

    return mid_point


        


three_point = [[width//2,0],[0,height-1],[width-1,height-1]]
xy = [0,0]
for i in range(iterations):
    c = random.choice(three_point)
    p = mid_point(xy, c)
    xy = p
    x = int(p[0])
    y = int(p[1])
    red = (255*(y+1)//height)
    green = (255*(x+1)//width)
    blue = (int(255*math.sqrt(x**2+y**2)//(math.sqrt((height-1)**2)+(width-1)**2)))
    color = "#{:02x}{:02x}{:02x}".format(red,green,blue)
    img.put(color,(x,y))
print("end")

mainloop()