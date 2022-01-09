import typing
import pygame, pygame.font, pygame.draw, pygame.display
import config



# define a variable to control the main loop
gameIsRunning = True

# Create the main screen
mainScreen: pygame.Surface = pygame.display.set_mode((round(config.swidth*(1+config.infoScreenWidth)),config.swidth))

canvasScreen: pygame.Surface = pygame.Surface((config.swidth,config.swidth)) #This one isn't displayed to the user, just a buffer screen
canvasScreen.fill("white")

artDisplayedScreen: pygame.Surface = mainScreen.subsurface((0,0,config.swidth,config.swidth))
optionsScreen: pygame.Surface = mainScreen.subsurface((config.swidth,0,config.swidth*config.infoScreenWidth,config.swidth))

#The variables past this point should probably have been in config, will do that better for future projects
#Values for the stylus that other functions need access to
stylusSize:float = config.stylusSize
stylusColour:str = config.defaultPaintColour

#Variable to hold the active side screen
activeSideScreen = None 
"""Whenever switching screens run cleanup on the current one, replace it, and run init on the new one"""

# Variables for axes
xaxisSmoothness = 0.8 #Value between 0 and 1, 0 no effect, 1 is no movement at all (is slowing for constant time)
yaxisSmoothness = 0.8


xaxisInput:config.axisControls = config.axisControls.linearTime
yaxisInput:config.axisControls = config.axisControls.volume


# General Functions

def drawTextOnSurface(height:float, pos:pygame.Vector2, text:str, colour:str, backgroundColour:str=None, font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen):
    """draws text onto a surface, takes in unit length as arguments (100 is bottom, 50 is right edge. values are not centers, top and left edges)
    Note: It may not work with any screen other than the options screen"""
    fontObject = pygame.font.Font(font, round(config.UnitLengthToPixels(height)))
    textSurface = fontObject.render(text,False,colour,backgroundColour)
    surfaceToBlitOn.blit(textSurface,((config.UnitLengthToPixels(pos.x)),config.UnitLengthToPixels(pos.y)))
    # surfaceToBlitOn.blit(textSurface,(config.UnitLengthToPixels((pos.x)/2)-(textSurface.get_width()*0.5),config.UnitLengthToPixels(pos.y)-(textSurface.get_height()*0.5))) #Width is divided by 2 because info screen is half of regular screen #This version was to input the center of the text, not top left corner
    return textSurface

def drawTextInBox(height:float, width:float, leftTopPos:pygame.Vector2, text:str, textColour:str, borderColour:str, backgroundColour:str=None, spaceBetweenTextAndBorder:float=config.textBoxSpaceBetweenTextAndBorder, font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen):
    """draws text and box onto surface. Takes in unitlength as measurements, pos is top left corner of box, not centers. Warning: it might not work with any screen other than the options screen"""
    #Draw background
    if backgroundColour != None:
        pygame.draw.rect(
            surface=surfaceToBlitOn,
            color=backgroundColour,
            rect=pygame.Rect(
                config.UnitLengthToPixels(leftTopPos.x),
                config.UnitLengthToPixels(leftTopPos.y),
                config.UnitLengthToPixels(width),
                config.UnitLengthToPixels(height)
            )
        )    
    #Draw border
    pygame.draw.rect(
        surface=surfaceToBlitOn,
        color=borderColour,
        rect=pygame.Rect(
            config.UnitLengthToPixels(leftTopPos.x),
            config.UnitLengthToPixels(leftTopPos.y),
            config.UnitLengthToPixels(width),
            config.UnitLengthToPixels(height)
        ),
        width = round(config.UnitLengthToPixels(config.textBoxPaddingOnSide))
    )
    #Draw text TODO - why is it gross? Spacing of drawTextOnSurface seems weird (I think just blitting text with pygame) - make it look nice anyway
    drawTextOnSurface(
        height=height-2*spaceBetweenTextAndBorder,
        pos=pygame.Vector2(leftTopPos.x+spaceBetweenTextAndBorder,leftTopPos.y+spaceBetweenTextAndBorder),
        text=text,
        colour=textColour
    )
    # print("height=", self.height-2*config.textBoxSpaceBetweenTextAndBorder)
    # print("pos=",pygame.Vector2((self.leftTopPos.x+config.textBoxSpaceBetweenTextAndBorder)*2,self.leftTopPos.y+config.textBoxSpaceBetweenTextAndBorder))

class TextBox():
    """Class where each object is a textbox that can be drawn and get input"""
    
    activeTextBox = None
    
    def __init__(self, submitFunc:"function", height:float, width:float, pos:pygame.Vector2, textColour:str, listOfTextBoxesToAddSelfTo:list, font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen, validInputs:str="*", initialText:str=""):
        #Note that there will be some padding between the border and the text, the height represents the height of the box, not the height of the text
        #(this probably doesn't belong in __init__)Note that the box has a max width, if type more than that then the user won't be able to see it, TODO - implement side scrolling maybe? Not sure how that would work
        self.submitFunc = submitFunc #Only argument is the self.currentText
        self.height = height
        self.width = width #Note that the width is size relative to swidth, so on config screen 50 is max
        #Note that pos is percent swidth from top left of whatever screen blitting onto
        self.leftTopPos = pos #Will go slightly outside these positions due to the thickness of the border
        self.bottomRightPos = pygame.Vector2(pos.x+width,pos.y+height)
        self.textColour = textColour
        self.font = font
        self.surfaceToBlitOn = surfaceToBlitOn
        self.validInputs = validInputs #Will do stuff if either one of these, delete or return
        self.currentText = initialText
        
        self.isactiveBox = False
        listOfTextBoxesToAddSelfTo.append(self)
        self.referenceToListOfTextBoxesInThisScreen = listOfTextBoxesToAddSelfTo
    
    def makeActiveTextBox(self): #TODO - Note has not been tested, should check
        #Makes the old active box no loonger active and makes
        if TextBox.activeTextBox !=None:
            TextBox.activeTextBox.isactiveBox = False
        TextBox.activeTextBox = self
        self.isactiveBox = True
    
    def onSubmit(self):
        if self.currentText == None or self.currentText == "": #Don't have to worry about the case it gets None (unless there's some case None is acceptable in which case whoops)
            print("some button is getting None, please don't do that...")
        else:
            self.submitFunc(self.currentText)
    
    def giveInput(self, newInput:str):
        if newInput == "\r":
            self.onSubmit()
        elif newInput == "\x08":
            self.currentText = self.currentText[:-1] #splices it so it removes the last character
        else:
            self.currentText += newInput
    
    def drawMe(self):
        if self.isactiveBox == True:
            #Draw textBox with active colour background
            drawTextInBox(
                height = self.height,
                width = self.width,
                leftTopPos = self.leftTopPos,
                text = self.currentText,
                textColour = self.textColour,
                borderColour = config.textBoxBorderColour,
                backgroundColour = config.activeTextBoxBackgroundColour,
                spaceBetweenTextAndBorder = config.textBoxSpaceBetweenTextAndBorder
            )
        else:
            #Draw textBox with active colour background (currently None, but still draws border and text)
            drawTextInBox(
                height = self.height,
                width = self.width,
                leftTopPos = self.leftTopPos,
                text = self.currentText,
                textColour = self.textColour,
                borderColour = config.textBoxBorderColour,
                backgroundColour = config.notActiveTextBoxBackgroundColour,
                spaceBetweenTextAndBorder = config.textBoxSpaceBetweenTextAndBorder
            )
        
class Button(): #Note if I were to rewrite this program this and textbox would be more modular and share more code, but since I'm almost done I just copy pasted a bunch
    """class where each object is one button that can draw itself and does something when pressed. Note after creation each button must be added to a mutuallyExclusiveButtons object to be rendered and checked. pressFunc needs to take no args, and call makeActiveButton on it's mutuallyExclusiveButtons object"""
    def __init__(self, pressFunc:"function", height:float, width:float, pos:pygame.Vector2, textColour:str, mutuallyExclusiveButtonsToAddSelfTo:"mutuallyExclusiveButtons", font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen, text:str=""):
        #Note that there will be some padding between the border and the text, the height represents the height of the box, not the height of the text
        #(this probably doesn't belong in __init__)Note that the box has a max width, if type more than that then the user won't be able to see it, TODO - implement side scrolling maybe? Not sure how that would work
        self.pressFunc = pressFunc #func needs to have no arguments and call makeActiveButton on it's mutuallyExclusiveButtons object 
        self.height = height
        self.width = width #Note that the width is size relative to swidth, so on config screen 50 is max
        #Note that pos is percent swidth from top left of whatever screen blitting onto
        self.leftTopPos = pos #Will go slightly outside these positions due to the thickness of the border
        self.bottomRightPos = pygame.Vector2(pos.x+width,pos.y+height)
        self.textColour = textColour
        self.font = font
        self.surfaceToBlitOn = surfaceToBlitOn
        self.text = text
        
        self.isactiveBox = False
        mutuallyExclusiveButtonsToAddSelfTo.myButtons.append(self)
        self.referenceToMutuallyExclusiveButtons = mutuallyExclusiveButtonsToAddSelfTo
    
    def drawMe(self):
        if self.isactiveBox == True:
            #Draw textBox with active colour background
            drawTextInBox(
                height = self.height,
                width = self.width,
                leftTopPos = self.leftTopPos,
                text = self.text,
                textColour = self.textColour,
                borderColour = config.buttonBorderColour,
                backgroundColour = config.activeButtonBackgroundColour,
                spaceBetweenTextAndBorder = config.buttonSpaceBetweenTextAndBorder
            )
        else:
            #Draw textBox with active colour background (currently None, but still draws border and text)
            drawTextInBox(
                height = self.height,
                width = self.width,
                leftTopPos = self.leftTopPos,
                text = self.text,
                textColour = self.textColour,
                borderColour = config.buttonBorderColour,
                backgroundColour = config.notActiveButtonBackgroundColour,
                spaceBetweenTextAndBorder = config.buttonSpaceBetweenTextAndBorder
            )
    
    def makeActiveButton(self):
        if self.referenceToMutuallyExclusiveButtons.activeButton != None:
            self.referenceToMutuallyExclusiveButtons.activeButton.isactiveBox = False
        self.isactiveBox = True
        self.referenceToMutuallyExclusiveButtons.activeButton = self
    

class mutuallyExclusiveButtons():
    """class where each object holds a group of buttons where only one can be active at a time"""
    def __init__(self, currentActiveButton:Button = None):
        self.myButtons:typing.List[Button] = [] #TODO add type annotation to specify it's a list of Buttons
        self.activeButton = currentActiveButton
    
    # def makeActiveButton(self, newActiveButton:Button):
    #     if self.activeButton != None:
    #         self.activeButton = False
    #     newActiveButton.isactiveBox = True
    #     self.activeButton = newActiveButton
        
    
        