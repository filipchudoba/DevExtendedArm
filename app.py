import re
from string import whitespace

definedColour = input("Enter colour: ")

class colour:
    def __init__(self, nazev, r, g, b):
        self.nazev = nazev
        self.r = r
        self.g = g
        self.b = b

    def lightColour(self):
        chosenOneName = self.nazev
        chosenOneR = self.r
        chosenOneG = self.g
        chosenOneB = self.b
        str(chosenOneR)
        str(chosenOneB)
        str(chosenOneR)
        print("LIGHT_PARAM full_custom_halo_night  0 8.1 -1.9  ",chosenOneR," ",chosenOneG," ",chosenOneB,"1  40 0 -1 0 0")


white = colour("white",1,1,1)
black = colour("black",0,0,0)
yellow = colour("yellow",1,1,0)
orange = colour("orange",1,0.5,0)
red = colour("red",1,0,0)
purple = colour("purple",1,0,1)
blue = colour("blue",0,0,1)
cyan = colour ("cyan",0,1,1)
green = colour ("green",0,1,0)

#Na zaklade inputu vybere prislusnou funkci
if definedColour == "white": 
    white.lightColour()
if definedColour == "black": 
    black.lightColour()
if definedColour == "yellow": 
    yellow.lightColour()
if definedColour == "orange": 
    orange.lightColour()
if definedColour == "red": 
    red.lightColour()
if definedColour == "purple": 
    purple.lightColour()
if definedColour == "blue": 
    blue.lightColour()
if definedColour == "cyan": 
    cyan.lightColour()
if definedColour == "green": 
    green.lightColour()
