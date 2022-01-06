import pygame
import config
import mainControlPanel
import variables
from sideScreenSuperClass import SideScreenSuperClass

class AxisControlPanel(SideScreenSuperClass):
    """side screen for choosing the input method and smoothness of the  and y axis"""
    
    widthOfBoxes = 20
    heightOfBoxes = 5
    
    xposOfxaxisBoxes = 3
    xposOfyaxisBoxes = 28
    
    yposOfAxisTitles = 5
    yposOfLinearTimeBoxes = 15
    yposOfVolumeBoxes = 25
    yposOfPitchBoxes = 35
    yposOfSmoothnessBoxes = 50
    
    
    

    
    def __init__(self) -> None:
        super().__init__()
        self.xaxisInputButtons = variables.mutuallyExclusiveButtons()
        self.groupsOfMutuallyExclusiveButtons.append(self.xaxisInputButtons)
        self.yaxisInputButtons = variables.mutuallyExclusiveButtons()
        self.groupsOfMutuallyExclusiveButtons.append(self.yaxisInputButtons)
        self.goBackButtons = variables.mutuallyExclusiveButtons()
        self.groupsOfMutuallyExclusiveButtons.append(self.goBackButtons)
    
    def initiateScreen(self):
        #First 2 text boxes for smoothness
        def xaxisSmoothnessBoxSubmit(input:str):
            if input==None or input=="":
                print("Oh no! xaxis smoothness box got None!")
            else:
                variables.xaxisSmoothness = float(input)
                print("smoothness for x input should be updated")
        xaxisSmoothnessBox = variables.TextBox(
            submitFunc= xaxisSmoothnessBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfSmoothnessBoxes),
            textColour= "blue",
            listOfTextBoxesToAddSelfTo= self.textBoxes,
            validInputs= "1234567890.",
            initialText= str(variables.xaxisSmoothness)
        )
        
        def yaxisSmoothnessBoxSubmit(input:str):
            if input==None or input=="":
                print("Oh no! xaxis smoothness box got None!")
            else:
                variables.yaxisSmoothness = float(input)
        xaxisSmoothnessBox = variables.TextBox(
            submitFunc= yaxisSmoothnessBoxSubmit,
            height= self.heightOfBoxes,
            width= self.widthOfBoxes,
            pos= pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfSmoothnessBoxes),
            textColour= "blue",
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
            textColour= "blue",
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
            textColour= "blue",
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
            textColour= "blue",
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
            textColour= "blue",
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
            textColour= "blue",
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
            textColour= "blue",
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
        variables.drawTextOnSurface(4,pygame.Vector2(self.xposOfxaxisBoxes,self.yposOfAxisTitles),"x-axis","blue") #have to multiply the x by 2 because I did a bad with units, whoopsie
        variables.drawTextOnSurface(4,pygame.Vector2(self.xposOfyaxisBoxes,self.yposOfAxisTitles),"y-axis","blue")
        
        for textBox in self.textBoxes:
            textBox.drawMe()
        for oneGroupOfMutuallyExclusiveButtons in self.groupsOfMutuallyExclusiveButtons:
            for button in oneGroupOfMutuallyExclusiveButtons.myButtons:
                button.drawMe()
    
    
    
    
    
    