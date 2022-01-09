import math
import pygame, pygame.image, pygame.draw
from pygame import Vector2, transform
import config
import variables

class Stylus():
    """stylus class, AKA the pointer/paint brush. There should be one object of this class"""
    defaultScreen: pygame.Surface = variables.artDisplayedScreen #TO DO - this probably won't work, figure out how it works
    
    def __init__(self) -> None:
        self.amp_phase = 0
        self.pos:Vector2 = Vector2(0,100) #The centers of the stylus
        self.size = config.stylusSize #Only used in self.draw to see if it's different than variables.stylusSize (to heck when the size changes)   - TODO - would be better if somehow variables could make a changeStylusSize function that deals with it all in one, not sure how to do that without import issues though...
        self.image = transform.scale(pygame.image.load(config.stylusImage),(round(config.UnitLengthToPixels(variables.stylusSize)),round(config.UnitLengthToPixels(variables.stylusSize))))
        # self.paintColour = config.defaultPaintColour #Now held in variables to avoid import issues
        
    def draw(self, screen:pygame.Surface = None):
        """draws the sprite on specified screen or the default screen if screen is not passed"""
        if screen is None:
            screen = self.defaultScreen
        
        #optimization so I only change the image size if it changes
        if variables.stylusSize != self.size:
            self.size = variables.stylusSize
            self.image = transform.scale(pygame.image.load(config.stylusImage),(round(config.UnitLengthToPixels(variables.stylusSize)),round(config.UnitLengthToPixels(variables.stylusSize))))

        screen.blit(self.image, (config.UnitLengthToPixels(self.pos.x-variables.stylusSize/2), config.UnitLengthToPixels(self.pos.y-variables.stylusSize/2)))
        # pygame.draw.circle() maybe change to b a faded gray circle
    
    # def update(self, timeSinceLastRender:float):
    #     """update the stylus' position and draw on canvas"""
    #     self.pos.x += config.stylusSpeed * timeSinceLastRender
    #     if self.pos.x >= 100:
    #         self.pos.x = 0
    #     pygame.draw.circle(variables.canvasScreen, self.paintColour, config.UnitLengthToPixels(self.pos), config.UnitLengthToPixels(self.size/2))
    
    def draw_freq_data(self, timeSinceLastRender: float, pitch_data):
        # variables.canvasScreen.fill("black")
        SCALE = 1e-4
        WIDTH = 3
        HUE_SPEED = 1e-3
        self.amp_phase += timeSinceLastRender*HUE_SPEED
        self.amp_phase %= 2*math.pi
        r = math.cos(self.amp_phase) + 1
        g = math.cos(self.amp_phase+2*math.pi/3) + 1
        b = math.cos(self.amp_phase-2*math.pi/3) + 1
        c = pygame.Color(int(r*127),int(g*127),int(b*127))
        for idx,val in enumerate(pitch_data):
            variables.canvasScreen.fill(c, pygame.Rect(idx*WIDTH, 0, WIDTH, val*SCALE))
            
    # TODO to make this work need to pass it decibelValue and pitch from main loop, create xaxisControl & yaxisControl and have them set to the correct things. Probably a named tyuple that can only be "linearTime", "volume", or "pitch"
    def update(self, timeSinceLastRender:float, decibelVolume:float, pitch:float): #Not sure what pitch will be
        """update the stylus' position and draw on canvas"""
        #Update x-pos
        if variables.xaxisInput == config.axisControls.linearTime:  
            self.pos.x = self.moveLinearTime(self.pos.x, config.stylusSpeed, timeSinceLastRender)
        elif variables.xaxisInput == config.axisControls.volume:
            self.pos.x = self.moveVolume(self.pos.x, variables.xaxisSmoothness, decibelVolume)
        elif variables.xaxisInput == config.axisControls.pitch:
            self.pos.x = self.movePitch(self.pos.x, variables.xaxisSmoothness, decibelVolume, pitch)
        else:
            print("uh, nothing is set to control the x-axis")
        
        #Update y-pos
        if variables.yaxisInput == config.axisControls.linearTime:  
            self.pos.y = self.moveLinearTime(self.pos.y, config.stylusSpeed, timeSinceLastRender)
        elif variables.yaxisInput == config.axisControls.volume:
            self.pos.y = self.moveVolume(self.pos.y, variables.yaxisSmoothness, decibelVolume)
        elif variables.yaxisInput == config.axisControls.pitch:
            self.pos.y = self.movePitch(self.pos.y, variables.yaxisSmoothness, decibelVolume, pitch)
        else:
            print("uh, nothing is set to control the y-axis")
        
        pygame.draw.circle(variables.canvasScreen, variables.stylusColour, config.UnitLengthToPixels(self.pos), config.UnitLengthToPixels(variables.stylusSize/2))

    #TODO Also add smoothness factor into all 3 of these movement types (maybe not linear motion, then mention that somewhere)
    def moveLinearTime(self, valueToMove:float, speed:float, timeSinceLastRender:float):
        valueToMove += speed * timeSinceLastRender
        if valueToMove >= 100:
            valueToMove = 0
        return valueToMove #need to return it and reassign at calling since valueToMove loses it's connextion to the original variable passed

    
    def moveVolume(self, valueToMove:float, valueSmoothness:float, decibelVolume:float):
        # if decibelVolume >= config.minDecibelToMove: #TODO - currently crashes if mic is off - fix that
        #     valueToMove = 100 - (((decibelVolume-config.minDecibelToMove)/config.decibelsToCross)*100) #At minDecibelToMove value=100, at minDecibelToMove+decibelsToCross, value=0
        # else:
        #     valueToMove = 100 #100 is bottom of screen
        # return valueToMove
    
        if decibelVolume >= config.minDecibelToMove: #TODO - currently crashes if mic is off - fix that
            expectedValueToMoveIfNoSmooth = 100 - (((decibelVolume-config.minDecibelToMove)/config.decibelsToCross)*100) #At minDecibelToMove value=100, at minDecibelToMove+decibelsToCross, value=0
        else:
            expectedValueToMoveIfNoSmooth = 100 #100 is bottom of screen
        valueToMove = expectedValueToMoveIfNoSmooth*(1-valueSmoothness) + valueToMove*valueSmoothness 
        
        return self.calcNewPosWithSmoothness(expectedValueToMoveIfNoSmooth, valueToMove, valueSmoothness)
    
    def movePitch(self, valueToMove:float, valueSmoothness:float, decibelVolume:float, pitch):
        if decibelVolume >= config.minDecibelToRegisterPitch: #So it doesn't move from background noise (could make a different value in config)    #TODO - currently crashes if mic is off - fix that
            expectedValueToMoveIfNoSmooth = 100-(pitch/config.pitchToCross)*100 #TODO make min pitch? make any other changes so it's actually good
        else:
            expectedValueToMoveIfNoSmooth = 100 #100 is bottom of screen
        
        return self.calcNewPosWithSmoothness(expectedValueToMoveIfNoSmooth, valueToMove, valueSmoothness)
    
    
    def calcNewPosWithSmoothness(self, expectedDestinationWithoutSmoothness:float, currentPosition:float, smoothness:float):
        return expectedDestinationWithoutSmoothness*(1-smoothness) + currentPosition*smoothness #If smoothness not 0 this will make a difference weighting it towards where it already is to avoid jumpyness
        
