"""
Name: Hansen Chen
Section: EXB3
netID: hc1941
Description: Program that draws a triangle using Turtle
"""

import turtle
import math

a=float(input("Please enter the length of the first leg: "))
b=float(input("Please enter the length of the second leg: "))
ang=float(input("Please enter the size of the angle: "))
turtle.forward(a)
turtle.left(180-ang)
turtle.forward(b)
ang=math.radians(ang)
c=a**2+b**2-2*a*b*math.cos(ang)
c=c**0.5
ang_a=math.acos((a**2-b**2-c**2)/(-2*b*c))
ang_a=math.degrees(ang_a)
turtle.right(180)
turtle.right(ang_a)
turtle.forward(c)

turtle.done()