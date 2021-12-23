import pygame
import variables
import config

#This module will be for drwing onto the config screen and controlling data on it

currentColourInput = ""

def updateOptionsScreen():
    """Redraws the info screen"""
    variables.drawTextOnSurface(4,pygame.Vector2(5,2),"Type a colour (backspace clears it)","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,6),"and press enter to change the colour,","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,10),"make sure it's a valid colour or else","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,20),"this is the colour input:","blue")
    variables.drawTextOnSurface(4,pygame.Vector2(5,25),currentColourInput,"blue")
    
    
def keepTrackOfColour(unicodeCharacter):
    """Keeps track of colour, if 'return' is pressed returns the input colour"""
    global currentColourInput #TODO ask Tadhg about this... is this available in other files now? That's bad if it is so how do i change?
    if unicodeCharacter == "\r":
        colour_to_use = currentColourInput
        currentColourInput = ""
        return colour_to_use
    elif unicodeCharacter == "\x08":
        currentColourInput = ""
        print("it should be wiped?")
    else:
        currentColourInput += unicodeCharacter
