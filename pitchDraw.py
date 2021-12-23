import pygame, pygame.image, pygame.display, pygame.time, pygame.draw
import config
from stylus import Stylus
import variables
import pyaudio
import math
import struct
import myPyAudioStuff #In importing it starts the stream TO DO - is this bad practise and should move the starting to this file?
import optionsScreen



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
    
    
    
    print("main is running")
    
    
    # main loop
    while variables.gameIsRunning:
        timeSinceLastRender = GameClock.tick()

        #Doing pyaudio stuff every frame and updating y of the stylus
        pyaudioData = myPyAudioStuff.stream.read(config.audioChunkSize) #TODO - make it take a variable amount so it can't fall behind
        currentrmsValue = myPyAudioStuff.rms(pyaudioData)
        currentDecibelValue = 20 * math.log10(currentrmsValue)
        if currentDecibelValue >= config.minDecibelToMove:
            stylus.pos.y = 100 - (((currentDecibelValue-config.minDecibelToMove)/config.decibelsToCross)*100) #At minDecibelToMove y=100, at minDecibelToMove+decibelsToCross, y=0
            # print("\n this is the current stylus.y.pos")
            # print(stylus.pos.y)
        else:
            stylus.pos.y = 100 #100 is bottom of screen
        
        
        # update the position of the stylus
        stylus.update(timeSinceLastRender)
        
        #update the info screen (might not need to do this every frame... maybe only when restarting? Oh no when data is being put in?)
        variables.optionsScreen.fill("black")
        optionsScreen.updateOptionsScreen()
        
        # put images on screen
        
        
        variables.artDisplayedScreen.blit(variables.canvasScreen,(0,0))
        stylus.draw(variables.artDisplayedScreen) #draws the stylus on the screen
        
        
        
        pygame.display.update()
        
        
        
        
        
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            print(event)
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                variables.gameIsRunning = False
            if event.type == pygame.KEYDOWN:
                #Currently use input to control colour, plan on changing this in the future
                newColour = optionsScreen.keepTrackOfColour(event.unicode)
                if newColour != None:
                    #So if 'return' was pressed
                    stylus.paintColour = newColour
                
                    

if __name__ == "__main__":
    main()
    myPyAudioStuff.stream.stop_stream()
    myPyAudioStuff.stream.close()