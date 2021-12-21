import pygame, pygame.image, pygame.draw
from pygame import Vector2, transform
import config
import variables

class Stylus():
    """stylus class, AKA the pointer/paint brush. There should be one object of this class"""
    defaultScreen: pygame.Surface = variables.artDisplayedScreen #TO DO - this probably won't work, figure out how it works
    
    def __init__(self) -> None:
        self.pos:Vector2 = Vector2(0,50) #The centers of the stylus
        self.size = config.stylusSize
        self.image = transform.scale(pygame.image.load(config.stylusImage),(round(config.UnitLengthToPixels(self.size)),round(config.UnitLengthToPixels(self.size))))
        self.paintColour = config.defaultPaintColour
        
    def draw(self, screen:pygame.Surface = None):
        """draws the sprite on specified screen or the default screen if screen is not passed"""
        if screen is None:
            screen = self.defaultScreen
        screen.blit(self.image, (config.UnitLengthToPixels(self.pos.x-self.size/2), config.UnitLengthToPixels(self.pos.y-self.size/2)))
    
    def update(self, timeSinceLastRender:float):
        """update the stylus' position and draw on canvas"""
        self.pos.x += config.stylusSpeed * timeSinceLastRender
        if self.pos.x >= 100:
            self.pos.x = 0
        pygame.draw.circle(variables.canvasScreen, self.paintColour, config.UnitLengthToPixels(self.pos), config.UnitLengthToPixels(self.size/2))
        
    

#Make a class that the main loop will make an object of that has position and a sprite (maybe copy sprite stuff from dungeonCrawler)