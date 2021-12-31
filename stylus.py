import pygame, pygame.image, pygame.draw
from pygame import Vector2, transform
import config
import variables

class Stylus():
    """stylus class, AKA the pointer/paint brush. There should be one object of this class"""
    defaultScreen: pygame.Surface = variables.artDisplayedScreen #TO DO - this probably won't work, figure out how it works
    
    def __init__(self) -> None:
        self.pos:Vector2 = Vector2(0,100) #The centers of the stylus
        self.size = config.stylusSize
        self.image = transform.scale(pygame.image.load(config.stylusImage),(round(config.UnitLengthToPixels(self.size)),round(config.UnitLengthToPixels(self.size))))
        self.paintColour = config.defaultPaintColour
        
    def draw(self, screen:pygame.Surface = None):
        """draws the sprite on specified screen or the default screen if screen is not passed"""
        if screen is None:
            screen = self.defaultScreen
        screen.blit(self.image, (config.UnitLengthToPixels(self.pos.x-self.size/2), config.UnitLengthToPixels(self.pos.y-self.size/2)))
        # pygame.draw.circle() maybe change to b a faded gray circle
    
    # def update(self, timeSinceLastRender:float):
    #     """update the stylus' position and draw on canvas"""
    #     self.pos.x += config.stylusSpeed * timeSinceLastRender
    #     if self.pos.x >= 100:
    #         self.pos.x = 0
    #     pygame.draw.circle(variables.canvasScreen, self.paintColour, config.UnitLengthToPixels(self.pos), config.UnitLengthToPixels(self.size/2))
    
    
    # TODO to make this work need to pass it decibelValue and pitch from main loop, create xaxisControl & yaxisControl and have them set to the correct things. Probably a named tyuple that can only be "linearTime", "volume", or "pitch"
    def update(self, timeSinceLastRender:float, decibelVolume:float, pitch:float): #Not sure what pitch will be
        """update the stylus' position and draw on canvas"""
        #Update x-pos
        if config.xaxisInput == config.axisControls.linearTime:  
            self.pos.x = self.moveLinearTime(self.pos.x, config.stylusSpeed, timeSinceLastRender)
        elif config.xaxisInput == config.axisControls.volume:
            self.pos.x = self.moveVolume(self.pos.x, decibelVolume)
        elif config.xaxisInput == config.axisControls.pitch:
            self.pos.x = self.movePitch(self.pos.x, pitch)
        else:
            print("uh, nothing is set to control the x-axis")
        
        #Update y-pos
        if config.yaxisInput == config.axisControls.linearTime:  
            self.pos.y = self.moveLinearTime(self.pos.y, config.stylusSpeed, timeSinceLastRender)
        elif config.yaxisInput == config.axisControls.volume:
            self.pos.y = self.moveVolume(self.pos.y, decibelVolume)
        elif config.yaxisInput == config.axisControls.pitch:
            self.pos.y = self.movePitch(self.pos.y, pitch)
        else:
            print("uh, nothing is set to control the y-axis")
        
        pygame.draw.circle(variables.canvasScreen, self.paintColour, config.UnitLengthToPixels(self.pos), config.UnitLengthToPixels(self.size/2))

    #TODO Also add smoothness factor into all 3 of these movement types (maybe not linear motion, then mention that somewhere)
    def moveLinearTime(self, valueToMove:float, speed:float, timeSinceLastRender:float):
        valueToMove += speed * timeSinceLastRender
        if valueToMove >= 100:
            valueToMove = 0
        return valueToMove #need to return it and reassign at calling since valueToMove loses it's connextion to the original variable passed

    
    def moveVolume(self, valueToMove:float, decibelVolume:float):
        if decibelVolume >= config.minDecibelToMove: #TODO - currently crashes if mic is off - fix that
            valueToMove = 100 - (((decibelVolume-config.minDecibelToMove)/config.decibelsToCross)*100) #At minDecibelToMove value=100, at minDecibelToMove+decibelsToCross, value=0
        else:
            valueToMove = 100 #100 is bottom of screen
        return valueToMove
    
    def movePitch(self, valueToMove:float, pitch):
        print("This isn't implemented yet, sorryyyyyyy")
        return valueToMove
        
