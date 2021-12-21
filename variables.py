import pygame
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


