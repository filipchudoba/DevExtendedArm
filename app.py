import re
import os
import sys
import versioncheck
import colourcheck
import inputWindow
from colourcheck import colourList
from inputWindow import sceneryPath
from string import whitespace
from tracemalloc import stop
from turtle import end_fill

print("The colours will change in this order: ", colourList)

#colourList = ("blue","blue","blue","yellow","yellow","yellow")

class colour:
    def __init__(self, nazev, r, g, b):
        self.nazev = nazev
        self.r = r
        self.g = g
        self.b = b
        self.finalOperation = ""

    def lightColour(self):
        chosenOneName = self.nazev
        chosenOneR = self.r
        chosenOneG = self.g
        chosenOneB = self.b
        str(chosenOneR)
        str(chosenOneB)
        str(chosenOneR)
        self.finalOperation = str(chosenOneR)+" "+str(chosenOneG)+" "+str(chosenOneB)
        #self.finalOperation = "LIGHT_PARAM full_custom_halo_night 0 8.1 -1.9 "+str(chosenOneR)+" "+str(chosenOneG)+" "+str(chosenOneB)+" 1 40 0 -1 0 0\n"
        str(self.finalOperation)

white = colour("white",1,1,1)
black = colour("black",0,0,0)
yellow = colour("yellow",1,1,0)
orange = colour("orange",1,0.5,0)
red = colour("red",1,0,0)
purple = colour("purple",1,0,1)
blue = colour("blue",0,0,1)
cyan = colour ("cyan",0,1,1)
green = colour ("green",0,1,0)

string1 = 'LIGHT_PARAM'
  
# opening a text file
filepath = sceneryPath +'\\a09_lamp_street2.obj'
file1 = open(filepath, "r")
  
# setting flag and index to 0
flag = 0
index = 0
c = 0
  
# Loop through the file line by line
for line in file1:  
    index += 1
      
    # checking string is present in line or not
    if string1 in line:
        
        index -= 1
        definedColour = colourList[c]
        print ("The next colour will be:",colourList[c])
        print(c)
        c += 1

        #Na zaklade inputu vybere prislusnou funkci
        if definedColour == 'white': 
            white.lightColour()
            finalOperation = white.finalOperation
        elif definedColour == 'black': 
            black.lightColour()
            finalOperation = black.finalOperation
        elif definedColour == 'yellow': 
            yellow.lightColour()
            finalOperation = yellow.finalOperation
        elif definedColour == 'orange': 
            orange.lightColour()
            finalOperation = orange.finalOperation
        elif definedColour == 'red': 
            red.lightColour()
            finalOperation = red.finalOperation
        elif definedColour == 'purple': 
            purple.lightColour()
            finalOperation = purple.finalOperation
        elif definedColour == 'blue': 
            blue.lightColour()
            finalOperation = blue.finalOperation
        elif definedColour == 'cyan': 
            cyan.lightColour()
            finalOperation = cyan.finalOperation
        elif definedColour == 'green': 
            green.lightColour()
            finalOperation = green.finalOperation
        else:
            print("no colour available, will be used black instead")
            black.lightColour()
            finalOperation = black.finalOperation

        # with is like your try .. finally block in this case
        with open('a09_lamp_street2.obj', 'r') as file:
            data = file.readlines()

        print ("Changing this line: ", data[index])

        linka = data[index]
        x = linka.split(" ")
        #print(x)

        i = 0
        stringBeforeAttachement = x[i]
        i =+ 1
        while i < 5:
            stringBeforeAttachement = stringBeforeAttachement + " " + x[i]
            #debug purpose
            #print(stringBeforeAttachement)
            i += 1

        stringBeforeAttachement = stringBeforeAttachement + " " + finalOperation

        i = i + 3

        while i < 14:
            stringBeforeAttachement = stringBeforeAttachement + " " + x[i]
            #debug purpose
            #print(stringBeforeAttachement)
            i += 1

        print ("Will be changed with this: " + stringBeforeAttachement)
        #print ("The colour will be:" + finalOperation)

        data[index] = stringBeforeAttachement

        str(stringBeforeAttachement)

        # and write everything back
        with open('a09_lamp_street2.obj', 'w') as file:
            file.writelines(data)
        file.close()

        index += 1