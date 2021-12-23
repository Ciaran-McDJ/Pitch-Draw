import pygame
import math


#All other functions will be in 'variables' so can use things from both 'config' and 'variables' (can't import 'variables' here without loop)

def pixelsToUnitLength(pixels:int):
    return pixels/swidth*100
def UnitLengthToPixels(UnitLength):
    return swidth*UnitLength/100

def pytheorem(x:int, y:int):
    return math.sqrt(x**2 + y**2)
    

# inputs
swidth = 800 # only values in pixels
sheight = 800 # only values in pixels
infoScreenWidth = 0.5 # in percent of swidth



#Stylus Stuff
stylusImage = "/home/ciaran/Pictures/zombie.png" #TO DO - get image for cursor
stylusSize = 5 
"""diameter"""
stylusSpeed = 0.03 
"""percent per milisecond only in the x direction, y is non linear"""
defaultPaintColour = "Red"

#Audio Stuff
minDecibelToMove = -45 
"""Above this value the cursor starts moving (to avoid noise being an issue)"""
decibelsToCross = 25; 
"""The number of decibels to go from bottom to top"""
audioChunkSize = 2000; 
"""The amount of bytes it takes per frame, too low and can fall behind and jumpy. Higher smoother but lower frame rate (waits for audio)"""





