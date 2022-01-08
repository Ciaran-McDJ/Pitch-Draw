import pygame, pygame.image, pygame.display, pygame.time, pygame.draw
import config
from stylus import Stylus
import variables
import pyaudio
import math
import struct
import myPyAudioStuff #In importing it starts the stream TO DO - is this bad practise and should move the starting to this file?
import mainControlPanel
import configScreen
import axisControlPanel



# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()

    # load and set the logo TODO - make a proper logo (currently a place holder from google images) (also where is this logo used???)
    logo: pygame.Surface = pygame.image.load("/home/ciaran/Downloads/token_5.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Pitch Draw!")
    
    # Don't know if I'll ever need this but just in case will keep all clocks in this set
    myClocks = set()
    
    # Making some variables
    GameClock = pygame.time.Clock()
    myClocks.add(GameClock)
    stylus = Stylus()
    
    variables.activeSideScreen = mainControlPanel.MainControlPanel()
    variables.activeSideScreen.initiateScreen()
    
    
    print("main is running")
    
    
    # main loop
    while variables.gameIsRunning:
        timeSinceLastRender = GameClock.tick()

        #Doing pyaudio stuff every frame and updating y of the stylus
        pyaudioData = myPyAudioStuff.stream.read(config.audioChunkSize) #TODO - make it take a variable amount so it can't fall behind
        currentrmsValue = myPyAudioStuff.rms(pyaudioData)
        currentDecibelValue = 20 * math.log10(currentrmsValue)
        currentpitch = myPyAudioStuff.convertDataToPitch(pyaudioData)
        print(currentpitch)
        # Now doing this in stylus' update function, can delete this section
        # if currentDecibelValue >= config.minDecibelToMove: #TODO - currently crashes if mic is off - fix that
        #     stylus.pos.y = 100 - (((currentDecibelValue-config.minDecibelToMove)/config.decibelsToCross)*100) #At minDecibelToMove y=100, at minDecibelToMove+decibelsToCross, y=0
        #     # print("\n this is the current stylus.y.pos")
        #     # print(stylus.pos.y)
        # else:
        #     stylus.pos.y = 100 #100 is bottom of screen
        
        
        # update the position of the stylus
        stylus.update(timeSinceLastRender,currentDecibelValue,currentpitch)
        
        #update the info screen (might not need to do this every frame... maybe only when restarting? Oh no when data is being put in?)
        variables.optionsScreen.fill("black")
        variables.activeSideScreen.update()
        
        
        variables.artDisplayedScreen.blit(variables.canvasScreen,(0,0))
        stylus.draw(variables.artDisplayedScreen) #draws the stylus on the screen
        
        
        
        pygame.display.update()
        
        
        
        
        
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            # print(event)
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                variables.gameIsRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #The left mouse button
                    #If pressed on position of any box, activate that box                    
                    for individualBox in variables.activeSideScreen.textBoxes:
                        # first part of if statement checking if x values allign, second part checking y values
                        if (config.UnitLengthToPixels(individualBox.leftTopPos.x)+config.swidth < event.pos[0] < config.UnitLengthToPixels(individualBox.bottomRightPos.x)+config.swidth) and (config.UnitLengthToPixels(individualBox.leftTopPos.y) < event.pos[1] < config.UnitLengthToPixels(individualBox.bottomRightPos.y)):  #Note, not alowed to reconfigure screen, this dependant on options screen to the right and only textboxes in options screen
                            individualBox.makeActiveTextBox()
                    for oneGroupOfMutuallyExclusiveButtons in variables.activeSideScreen.groupsOfMutuallyExclusiveButtons: #Ideally I'd make a function to check if clicked in box but for now copy paste works :)
                        for button in oneGroupOfMutuallyExclusiveButtons.myButtons:
                            if (config.UnitLengthToPixels(button.leftTopPos.x)+config.swidth < event.pos[0] < config.UnitLengthToPixels(button.bottomRightPos.x)+config.swidth) and (config.UnitLengthToPixels(button.leftTopPos.y) < event.pos[1] < config.UnitLengthToPixels(button.bottomRightPos.y)):  #Note, not alowed to reconfigure screen, this dependant on options screen to the right and only textboxes in options screen
                                button.makeActiveButton()
                                button.pressFunc()
            #If key pressed pass it to active box
            if event.type == pygame.KEYDOWN:
                if variables.TextBox.activeTextBox != None: #Only check if there is an active text box to avoid errors
                    if event.unicode in variables.TextBox.activeTextBox.validInputs or event.unicode == "\r" or event.unicode == "\x08":
                        variables.TextBox.activeTextBox.giveInput(event.unicode)

                
                    

if __name__ == "__main__":
    main()
    myPyAudioStuff.stream.stop_stream()
    myPyAudioStuff.stream.close()