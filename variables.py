import pygame, pygame.font
import config

# define a variable to control the main loop
gameIsRunning = True


# Create the main screen
mainScreen: pygame.Surface = pygame.display.set_mode((round(config.swidth*(1+config.infoScreenWidth)),config.sheight))

canvasScreen: pygame.Surface = pygame.Surface((config.swidth,config.sheight)) #This one isn't displayed to the user, just a buffer screen
canvasScreen.fill("white")
# mainScreen.subsurface((0,0,config.swidth,config.sheight)) # To delete

artDisplayedScreen: pygame.Surface = mainScreen.subsurface((0,0,config.swidth,config.sheight))
optionsScreen: pygame.Surface = mainScreen.subsurface((config.swidth,0,config.swidth*config.infoScreenWidth,config.sheight))



# Functions

def drawTextOnSurface(height:float, pos:pygame.Vector2, text:str, colour:str, backgroundColour:str=None, font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen):
    """draws text onto a surface, takes in percent of optionsScreen as arguments (100 is bottom, 100 is right edge. values are not centers, top and left edges)
    Note: It may not work with any screen other than the options screen"""
    fontObject = pygame.font.Font(font, round(config.UnitLengthToPixels(height)))
    textSurface = fontObject.render(text,False,colour,backgroundColour)
    surfaceToBlitOn.blit(textSurface,((config.UnitLengthToPixels(pos.x)/2),config.UnitLengthToPixels(pos.y))) #Width is divided by 2 because info screen is half of regular screen
    # surfaceToBlitOn.blit(textSurface,(config.UnitLengthToPixels((pos.x)/2)-(textSurface.get_width()*0.5),config.UnitLengthToPixels(pos.y)-(textSurface.get_height()*0.5))) #Width is divided by 2 because info screen is half of regular screen #This version was to input the center of the text, not top left corner
    return textSurface

class TextBox():
    """Class where each object is a textbox that can be drawn and get input"""
    
    activeTextBox = None
    textBoxes = []
    
    def __init__(self, submitFunc:"function", height:float, width:float, pos:pygame.Vector2, text:str, colour:str, font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen, validInputs:str="*"):
        #Note that there will be some padding between the border and the text, the height represents the height of the box, not the height of the text
        #(this probably doesn't belong in __init__)Note that the box has a max width, if type more than that then the user won't be able to see it, TODO - implement side scrolling maybe? Not sure how that would work
        self.submitFunc = submitFunc
        self.height = height
        self.width = width
        self.leftTopPos = pos
        self.bottomRightPos = pygame.Vector2(pos.x+width,pos.y+height)
        self.text = text
        self.colour = colour
        self.font = font
        self.surfaceToBlitOn = surfaceToBlitOn
        self.validInputs = validInputs
        
        self.isactiveBox = False
        TextBox.textBoxes += self
    
    def makeActiveTextBox(self): #TODO - Note has not been tested, should check
        #Makes the old active box no loonger active and makes
        if TextBox.activeTextBox !=None:
            TextBox.activeTextBox.isactiveBox = False
        TextBox.activeTextBox = self
        self.isactiveBox = True
    
    # def drawMe(self):
    #     if self.isactiveBox == True:
    #         drawTextOnSurface()
        
    
    
        