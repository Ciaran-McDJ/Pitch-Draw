import pygame
import variables
import config

#This module will be for drawing onto the control panel and controlling data on it

currentColourInput = ""
isActive = True

def updateControlPanel():
    """Redraws the info screen"""
    variables.drawTextOnSurface(4,pygame.Vector2(5,2),"Type a colour (backspace clears it)","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,6),"and press enter to change the colour,","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,10),"make sure it's a valid colour or else","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,20),"this is the colour input:","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,25),currentColourInput,"blue")
    
    
def keepTrackOfColour(unicodeCharacter):
    """Keeps track of colour, if 'return' is pressed returns the input colour"""
    global currentColourInput
    if unicodeCharacter == "\r":
        colour_to_use = currentColourInput
        currentColourInput = ""
        return colour_to_use
    elif unicodeCharacter == "\x08":
        currentColourInput = currentColourInput[:-1] #splices it so it removes the last character
    else:
        currentColourInput += unicodeCharacter
