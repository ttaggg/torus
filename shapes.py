import numpy as np
from numpy import pi, sin, cos, sqrt
from math import ceil
import Tkinter as tk

#######################
### HYPERPARAMETERS ###
#######################
R = 3
r = 2

a = 1
b = 0
s = 1

n = 1000
t = np.linspace(0, 1, n)
tt = np.linspace(0, 1, 10*n)
theta, phi = np.meshgrid(2.*pi*t, 2.*pi*t)

eps = 0.001
#######################


##############
### SHAPES ###
##############
def torus(theta=theta, phi=phi):
        return [(R + r*cos(theta))*cos(phi),
                (R + r*cos(theta))*sin(phi),
                r*sin(theta)]

# # this one refuse to work for some reason
# def torusConformal(a=a, b=b):
#         # by "Conformal Tiling on a Torus", Sullivan
#         denom = (sqrt(a**2. + b**2.) - b*cos(theta/b))
#         x = (a*cos(phi/a))/denom
#         y = (a*sin(phi/a))/denom
#         z = (b*sin(theta/b))/denom
#         return [x,y,z]

def curve(p, q, R=R, r=r):
    return [(R + r*cos(p*2.*pi*tt))*cos(q*2.*pi*tt),
            (R + r*cos(p*2.*pi*tt))*sin(q*2.*pi*tt),
            r*sin(p*2.*pi*tt)]

def curveArbitrary(u,v, R=R, r=r):
    return [(R + r*cos(2.*pi*u))*cos(2.*pi*v),
            (R + r*cos(2.*pi*u))*sin(2.*pi*v),
            r*sin(2.*pi*u)]

def getLine():
    coordinates = []
    lastx, lasty = 0, 0

    def xy(event):
        global lastx, lasty
        lastx, lasty = event.x, event.y

    def addLine(event):
        global lastx, lasty
        canvas.create_line((lastx, lasty, event.x, event.y))
        coordinates.append([lastx/100.0, (1000-lasty)/100.0])
        lastx, lasty = event.x, event.y

    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    canvas = tk.Canvas(root, width=1000, height=1000, background='white')
    canvas.grid(column=0, row=0, sticky=("N", "W", "E", "S"))

    cellwidth = 100
    cellheight = 100
    rect = {}
    for column in range(10):
        for row in range(10):
            x1 = column*cellwidth
            y1 = row * cellheight
            x2 = x1 + cellwidth
            y2 = y1 + cellheight
            rect[row,column] = canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")

    canvas.itemconfig("rect", fill="white")
    canvas.bind("<Button-1>", xy)
    canvas.bind("<B1-Motion>", addLine)

    root.mainloop()
    return (coordinates)
##############


#################
