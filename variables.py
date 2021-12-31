import pygame, pygame.font, pygame.draw
import config

# define a variable to control the main loop
gameIsRunning = True


# Create the main screen
mainScreen: pygame.Surface = pygame.display.set_mode((round(config.swidth*(1+config.infoScreenWidth)),config.swidth))

canvasScreen: pygame.Surface = pygame.Surface((config.swidth,config.swidth)) #This one isn't displayed to the user, just a buffer screen
canvasScreen.fill("white")
# mainScreen.subsurface((0,0,config.swidth,config.sheight)) # To delete

artDisplayedScreen: pygame.Surface = mainScreen.subsurface((0,0,config.swidth,config.swidth))
optionsScreen: pygame.Surface = mainScreen.subsurface((config.swidth,0,config.swidth*config.infoScreenWidth,config.swidth))



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
    
    def __init__(self, submitFunc:"function", height:float, width:float, pos:pygame.Vector2, textColour:str, font:str=None, surfaceToBlitOn:pygame.Surface=optionsScreen, validInputs:str="*", initialText:str=""):
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
        TextBox.textBoxes.append(self)
    
    def makeActiveTextBox(self): #TODO - Note has not been tested, should check
        #Makes the old active box no loonger active and makes
        if TextBox.activeTextBox !=None:
            TextBox.activeTextBox.isactiveBox = False
        TextBox.activeTextBox = self
        self.isactiveBox = True
    
    def giveInput(self, newInput:str):
        if newInput == "\r":
            self.submitFunc(self.currentText)
        elif newInput == "\x08":
            self.currentText = self.currentText[:-1] #splices it so it removes the last character
        else:
            self.currentText += newInput
    
    def drawMe(self):
        if self.isactiveBox == True:
            #Draw active background
            pygame.draw.rect(
                surface=self.surfaceToBlitOn,
                color=config.activeTextBoxBackgroundColour,
                rect=pygame.Rect(
                    config.UnitLengthToPixels(self.leftTopPos.x),
                    config.UnitLengthToPixels(self.leftTopPos.y),
                    config.UnitLengthToPixels(self.width),
                    config.UnitLengthToPixels(self.height)
                )
            )
        else:
            #Draw nonactive background (currently None)
            if config.notActiveTextBoxBackgroundColour != None:
                pygame.draw.rect(
                    surface=self.surfaceToBlitOn,
                    color=config.notActiveTextBoxBackgroundColour,
                    rect=pygame.Rect(
                        config.UnitLengthToPixels(self.leftTopPos.x),
                        config.UnitLengthToPixels(self.leftTopPos.y),
                        config.UnitLengthToPixels(self.width),
                        config.UnitLengthToPixels(self.height)
                    )
                )
        #Draw border
        pygame.draw.rect(
            surface=self.surfaceToBlitOn,
            color=config.textBoxBorderColour,
            rect=pygame.Rect(
                config.UnitLengthToPixels(self.leftTopPos.x),
                config.UnitLengthToPixels(self.leftTopPos.y),
                config.UnitLengthToPixels(self.width),
                config.UnitLengthToPixels(self.height)
            ),
            width = round(config.UnitLengthToPixels(config.textBoxPaddingOnSide))
        )
        #Draw text TODO - why is it gross? Spacing of drawTextOnSurface seems weird (I think just blitting text with pygame) - make it look nice anyway
        drawTextOnSurface(
            height=self.height-2*config.textBoxSpaceBetweenTextAndBorder,
            pos=pygame.Vector2((self.leftTopPos.x+config.textBoxSpaceBetweenTextAndBorder)*2,self.leftTopPos.y+config.textBoxSpaceBetweenTextAndBorder), #Note I have to multiply by 2 cause I'm not consistent with my values :(
            text=self.currentText,
            colour=self.textColour
        )
        # print("height=", self.height-2*config.textBoxSpaceBetweenTextAndBorder)
        # print("pos=",pygame.Vector2((self.leftTopPos.x+config.textBoxSpaceBetweenTextAndBorder)*2,self.leftTopPos.y+config.textBoxSpaceBetweenTextAndBorder))
        
    
    
        