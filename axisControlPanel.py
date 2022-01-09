import pygame
import config
import mainControlPanel
import variables
from sideScreenSuperClass import SideScreenSuperClass

class AxisControlPanel(SideScreenSuperClass):
    """side screen for choosing the input method and smoothness of the  and y axis"""
    colourOfAxisSpecificText = "blue"
    colourOfInfoText = "white"
    colourOfGeneralBoxText = "white"
    
    widthOfBoxes = 20
    widthOfHalfScreenNonAxisSpecificBoxes = 22
    widthOfFullWidthBoxes = 46
    heightOfBoxes = 5
    heightOfText = 4
    
    xposOfxaxisBoxes = 3
    xposOfLeftSideNonSpecificBoxes = 2
    xposOfyaxisBoxes = 28
    xposOfRightSideNonSpecificBoxes = 27
    xposOfgeneralBoxes = 2
    
    
    yposOfAxisTitles = 2
    yposOfLinearTimeBoxes = 10
    yposOfSpeedBoxDescription = 16 #To control LinearTime movement
    yposOfSpeedBox = 20
    yposOfVolumeBoxes = 30
    yposOfVolumeControlBoxesDescription = 36 #min decibels to move and decibels to cross
    yposOfVolumeControlBoxes = 40
    yposOfPitchBoxes = 50
    yposOfPitchControlBoxesDescription = 56
    yposOfPitchControlBoxes = 60
    yposOfSmoothnessTextDescription = 75
    yposOfSmoothnessBoxes = 80
    

    
    
    

    
    def __init__(self) -> None:
        super().__init__()
        self.xaxisInputButtons = variables.mutuallyExclusiveButtons()
        self.groupsOfMutuallyExclusiveButtons.append(self.xaxisInputButtons)
        self.yaxisInputButtons = variables.mutuallyExclusiveButtons()
        self.groupsOfMutuallyExclusiveButtons.append(self.yaxisInputButtons)
        self.goBackButtons = variables.mutuallyExclusiveButtons()
        self.groupsOfMutuallyExclusiveButtons.append(self.goBackButtons)
    
    def initiateScreen(self):
        #These boxes have controls for specific input types
        def speedBoxSubmit(input:str):
            config.stylusSpeed = float(input)
        speedBox = variables.TextBox(
            submitFunc= speedBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfFullWidthBoxes,
            pos= pygame.Vector2(self.xposOfgeneralBoxes,self.yposOfSpeedBox),
            textColour= self.colourOfGeneralBoxText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.", #TODO - Currently can't be negative but could add that
            initialText= str(config.stylusSpeed) 
        )
        
        def minDecibelsToMoveBoxSubmit(input:str):
            config.minDecibelToMove = float(input)
        minDecibelToMoveBox = variables.TextBox(
            submitFunc= minDecibelsToMoveBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfHalfScreenNonAxisSpecificBoxes, 
            pos= pygame.Vector2(self.xposOfLeftSideNonSpecificBoxes,self.yposOfVolumeControlBoxes),
            textColour= self.colourOfGeneralBoxText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.-",
            initialText= str(config.minDecibelToMove) 
        )
        
        def decibelsToCrossBoxSubmit(input:str):
            config.decibelsToCross = float(input)
        decibelsToCrossBox = variables.TextBox(
            submitFunc= decibelsToCrossBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfHalfScreenNonAxisSpecificBoxes, 
            pos= pygame.Vector2(self.xposOfRightSideNonSpecificBoxes,self.yposOfVolumeControlBoxes),
            textColour= self.colourOfGeneralBoxText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.",
            initialText= str(config.decibelsToCross) 
        )
        
        def minDecibelToRegisterPitchBoxSubmit(input:str):
            config.minDecibelToRegisterPitch = float(input)
        minDecibelToRegisterPitchBox = variables.TextBox(
            submitFunc= minDecibelToRegisterPitchBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfHalfScreenNonAxisSpecificBoxes, 
            pos= pygame.Vector2(self.xposOfLeftSideNonSpecificBoxes,self.yposOfPitchControlBoxes),
            textColour= self.colourOfGeneralBoxText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.-",
            initialText= str(config.minDecibelToRegisterPitch) 
        )
        
        def pitchToCrossBoxSubmit(input:str):
            config.pitchToCross = float(input)
        pitchToCrossBox = variables.TextBox(
            submitFunc= pitchToCrossBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfHalfScreenNonAxisSpecificBoxes, 
            pos= pygame.Vector2(self.xposOfRightSideNonSpecificBoxes,self.yposOfPitchControlBoxes),
            textColour= self.colourOfGeneralBoxText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.",
            initialText= str(config.pitchToCross) 
        )
        
        #Then 2 text boxes for smoothness for each axis
        def xaxisSmoothnessBoxSubmit(input:str):
            variables.xaxisSmoothness = float(input)
            print("smoothness for x input should be updated")
        xaxisSmoothnessBox = variables.TextBox(
            submitFunc= xaxisSmoothnessBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfSmoothnessBoxes),
            textColour= self.colourOfAxisSpecificText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.",
            initialText= str(variables.xaxisSmoothness)
        )
        
        def yaxisSmoothnessBoxSubmit(input:str):
            variables.yaxisSmoothness = float(input)
        xaxisSmoothnessBox = variables.TextBox(
            submitFunc= yaxisSmoothnessBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfSmoothnessBoxes),
            textColour= self.colourOfAxisSpecificText,
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.",
            initialText= str(variables.yaxisSmoothness)
        )
        
        #Now the buttons
        
        #First 3 are the xaxis control buttons
        def onxaxisLinearTimeButttonPressed():
            xaxisLinearTimeButtton.makeActiveButton()
            variables.xaxisInput = config.axisControls.linearTime
        xaxisLinearTimeButtton = variables.Button(
            pressFunc= onxaxisLinearTimeButttonPressed,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfLinearTimeBoxes),
            textColour= self.colourOfAxisSpecificText,
            mutuallyExclusiveButtonsToAddSelfTo= self.xaxisInputButtons,
            text= "Linear Time"
        )
        if variables.xaxisInput == config.axisControls.linearTime: #patch job fix to the issue of stating with an active button. Rewriting the Button class like explained in ideas would be better
            xaxisLinearTimeButtton.makeActiveButton()
        
        def onxaxisPitchButttonPressed():
            xaxisPitchButtton.makeActiveButton()
            variables.xaxisInput = config.axisControls.pitch
        xaxisPitchButtton = variables.Button(
            pressFunc= onxaxisPitchButttonPressed,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfPitchBoxes),
            textColour= self.colourOfAxisSpecificText,
            mutuallyExclusiveButtonsToAddSelfTo= self.xaxisInputButtons,
            text= "Pitch"
        )
        if variables.xaxisInput == config.axisControls.pitch:
            xaxisPitchButtton.makeActiveButton()
        
        def onxaxisVolumeButttonPressed():
            xaxisVolumeButtton.makeActiveButton()
            variables.xaxisInput = config.axisControls.volume
        xaxisVolumeButtton = variables.Button(
            pressFunc= onxaxisVolumeButttonPressed,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfVolumeBoxes),
            textColour= self.colourOfAxisSpecificText,
            mutuallyExclusiveButtonsToAddSelfTo= self.xaxisInputButtons,
            text= "Volume"
        )
        if variables.xaxisInput == config.axisControls.volume:
            xaxisVolumeButtton.makeActiveButton()
        
        #Next 3 are the yaxis control buttons
        def onyaxisLinearTimeButttonPressed():
            yaxisLinearTimeButtton.makeActiveButton()
            variables.yaxisInput = config.axisControls.linearTime
        yaxisLinearTimeButtton = variables.Button(
            pressFunc= onyaxisLinearTimeButttonPressed,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfLinearTimeBoxes),
            textColour= self.colourOfAxisSpecificText,
            mutuallyExclusiveButtonsToAddSelfTo= self.yaxisInputButtons,
            text= "Linear Time"
        )
        if variables.yaxisInput == config.axisControls.linearTime: #patch job fix to the issue of stating with an active button. Rewriting the Button class like explained in ideas would be better
            yaxisLinearTimeButtton.makeActiveButton()
        
        def onyaxisPitchButttonPressed():
            yaxisPitchButtton.makeActiveButton()
            variables.yaxisInput = config.axisControls.pitch
        yaxisPitchButtton = variables.Button(
            pressFunc= onyaxisPitchButttonPressed,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfPitchBoxes),
            textColour= self.colourOfAxisSpecificText,
            mutuallyExclusiveButtonsToAddSelfTo= self.yaxisInputButtons,
            text= "Pitch"
        )
        if variables.yaxisInput == config.axisControls.pitch:
            yaxisPitchButtton.makeActiveButton()
        
        def onyaxisVolumeButttonPressed():
            yaxisVolumeButtton.makeActiveButton()
            variables.yaxisInput = config.axisControls.volume
        yaxisVolumeButtton = variables.Button(
            pressFunc= onyaxisVolumeButttonPressed,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfVolumeBoxes),
            textColour= self.colourOfAxisSpecificText,
            mutuallyExclusiveButtonsToAddSelfTo= self.yaxisInputButtons,
            text= "Volume"
        )
        if variables.yaxisInput == config.axisControls.volume:
            yaxisVolumeButtton.makeActiveButton()
        
        #And finally the button to go back to the main control panel
        def onGoToMainControlPanelButttonPressed():
            self.cleanupScreen()
            variables.activeSideScreen = mainControlPanel.MainControlPanel() 
            variables.activeSideScreen.initiateScreen()
        goToMainControlPanelButtton = variables.Button(
            pressFunc= onGoToMainControlPanelButttonPressed,
            height= 3,
            width= 40,
            pos= pygame.Vector2(5,90),
            textColour= "yellow",
            mutuallyExclusiveButtonsToAddSelfTo= self.goBackButtons,
            text= "press me to go back to the main control panel"
        )

    
    def update(self):
        """Redraws the info screen"""
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfAxisTitles),"x-axis",self.colourOfAxisSpecificText) #have to multiply the x by 2 because I did a bad with units, whoopsie
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfAxisTitles),"y-axis",self.colourOfAxisSpecificText)
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfgeneralBoxes, self.yposOfSpeedBoxDescription), "how fast should the brush move?", self.colourOfInfoText)
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfLeftSideNonSpecificBoxes, self.yposOfVolumeControlBoxesDescription), "min dBel", self.colourOfInfoText)
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfRightSideNonSpecificBoxes, self.yposOfVolumeControlBoxesDescription), "dBels to cross", self.colourOfInfoText)
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfLeftSideNonSpecificBoxes, self.yposOfPitchControlBoxesDescription), "min dBel to move", self.colourOfInfoText)
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfRightSideNonSpecificBoxes, self.yposOfPitchControlBoxesDescription), "pitch to cross", self.colourOfInfoText)
        variables.drawTextOnSurface(self.heightOfText,pygame.Vector2(self.xposOfgeneralBoxes, self.yposOfSmoothnessTextDescription), "axis smoothness (between 0 and 1)", self.colourOfAxisSpecificText)
        
        #TODO - would be good to write to user that smoothness should be more than or equal to 0 and lesss than 1   0<=smoothness<1
        
        for textBox in self.textBoxes:
            textBox.drawMe()
        for oneGroupOfMutuallyExclusiveButtons in self.groupsOfMutuallyExclusiveButtons:
            for button in oneGroupOfMutuallyExclusiveButtons.myButtons:
                button.drawMe()
    
    
    
    
    
    