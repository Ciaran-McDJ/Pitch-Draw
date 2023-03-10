import pygame
import math
from enum import Enum


#All other functions will be in 'variables' so can use things from both 'config' and 'variables' (can't import 'variables' here without loop)

def pixelsToUnitLength(pixels:int):
    return pixels/swidth*100
def UnitLengthToPixels(UnitLength):
    return swidth*UnitLength/100

def pytheorem(x:int, y:int):
    return math.sqrt(x**2 + y**2)
    

# inputs
swidth = 800 # only values in pixels
infoScreenWidth = 0.5 # in percent of swidth



#Stylus Stuff
stylusImage = "/home/ciaran/Pictures/zombie.png" #TO DO - get image for cursor
stylusSize = 5 
"""diameter"""
stylusSpeed = 0.03 
"""percent per milisecond only in the x direction, y is non linear"""
defaultPaintColour = "red"

#Audio Stuff
minDecibelToMove = -45 
"""Above this value the cursor starts moving (to avoid noise being an issue)"""
decibelsToCross = 25; 
"""The number of decibels to go from bottom to top"""

minDecibelToRegisterPitch = -35
"""above this volume will move based on pitch, if below volume position at 100 (to avoid background noise registering)"""
pitchToCross = 1000 #TODO - No clue what units are, add them
"""difference in pitch between position 100 and 0 (no clue what units are, should be added)"""
minPitch = 200
"""when input method is pitch this pitch will be the bottom"""

audioChunkSize = 1000; 
"""The amount of bytes it takes per frame, too low and can fall behind and jumpy. Higher smoother but lower frame rate (waits for audio)"""



#TextBox Stuff
textBoxPaddingOnSide = 0.3 #percent of screen padding on each side (the border thickness)
textBoxSpaceBetweenTextAndBorder = 0.3
notActiveTextBoxBackgroundColour = None
activeTextBoxBackgroundColour = "light gray"
textBoxBorderColour = "red"

buttonPaddingOnSide = 0.3 #percent of screen padding on each side (the border thickness)
buttonSpaceBetweenTextAndBorder = 0.3
notActiveButtonBackgroundColour = None
activeButtonBackgroundColour = "light green"
buttonBorderColour = "yellow"



# Possible Axis Controls
class axisControls(Enum):
    """enum with 3 values, each of which is a type of input for an axis, possibilities are linearTime, pitch, and volume"""
    
    linearTime = "linearTime"
    pitch = "pitch"
    volume = "volume"





    
    