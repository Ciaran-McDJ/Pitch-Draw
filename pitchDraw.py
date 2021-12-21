import pygame, pygame.image, pygame.display, pygame.time, pygame.draw
import config
from stylus import Stylus
import variables



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

        # update the position of the stylus and draw onto the canvas
        stylus.update(timeSinceLastRender)
        
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
                if event.unicode == "w":
                    stylus.pos.y -= 2
                if event.unicode == "s":
                    stylus.pos.y += 2
                    

if __name__ == "__main__":
    main()