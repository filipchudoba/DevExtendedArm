import re
from string import whitespace
from tracemalloc import stop
from turtle import end_fill

definedColour = input("Enter colour: ")

class colour:
    def __init__(self, nazev, r, g, b):
        self.nazev = nazev
        self.r = r
        self.g = g
        self.b = b
        self.finalOperation = "LIGHT_PARAM full_custom_halo_night  0 8.1 -1.9  "

    def lightColour(self):
        chosenOneName = self.nazev
        chosenOneR = self.r
        chosenOneG = self.g
        chosenOneB = self.b
        str(chosenOneR)
        str(chosenOneB)
        str(chosenOneR)
        self.finalOperation = "LIGHT_PARAM full_custom_halo_night  0 8.1 -1.9  "+str(chosenOneR)+" "+str(chosenOneG)+" "+str(chosenOneB)+" 1  40 0 -1 0 0\n"
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

#Na zaklade inputu vybere prislusnou funkci
if definedColour == "white": 
    white.lightColour()
    finalOperation = white.finalOperation
if definedColour == "black": 
    black.lightColour()
    finalOperation = black.finalOperation
if definedColour == "yellow": 
    yellow.lightColour()
    finalOperation = yellow.finalOperation
if definedColour == "orange": 
    orange.lightColour()
    finalOperation = orange.finalOperation
if definedColour == "red": 
    red.lightColour()
    finalOperation = red.finalOperation
if definedColour == "purple": 
    purple.lightColour()
    finalOperation = purple.finalOperation
if definedColour == "blue": 
    blue.lightColour()
    finalOperation = blue.finalOperation
if definedColour == "cyan": 
    cyan.lightColour()
    finalOperation = cyan.finalOperation
if definedColour == "green": 
    green.lightColour()
    finalOperation = green.finalOperation



string1 = 'LIGHT_PARAM'
  
# opening a text file
file1 = open("a09_lamp_street2.obj", "r")
  
# setting flag and index to 0
flag = 0
index = 0
  
# Loop through the file line by line
for line in file1:  
    index += 1 
      
    # checking string is present in line or not
    if string1 in line:
        
      flag = 1
      break 
          
# checking condition for string found or not
if flag == 0: 
   print('String', string1 , 'Not Found') 
else: 
   print('String', string1, 'Found In Line', index)
  
# closing text file    
file1.close() 
print (index)
index -= 1

# with is like your try .. finally block in this case
with open('a09_lamp_street2.obj', 'r') as file:
    data = file.readlines()

print ("Changing this line: ", data[index])
print ("Will be changed with this: " + finalOperation)

data[index] = finalOperation

str(finalOperation)

# and write everything back
with open('a09_lamp_street2.obj', 'w') as file:
    file.writelines(data)