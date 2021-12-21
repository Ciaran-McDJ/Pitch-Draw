import pygame
import math

def pixelsToUnitLength(pixels:int):
    return pixels/swidth*100
def UnitLengthToPixels(UnitLength):
    return swidth*UnitLength/100

def pytheorem(x:int, y:int):
    return math.sqrt(x**2 + y**2)

# inputs
swidth = 500 # only values in pixels
sheight = 500 # only values in pixels
infoScreenWidth = 0.5 # in percent of swidth




stylusImage = "/home/ciaran/Pictures/zombie.png" #TO DO - get image for cursor
stylusSize = 5 #diameter
stylusSpeed = 0.03 #percent per milisecond only in the x direction, y is non linear
defaultPaintColour = "red"



