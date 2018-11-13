# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
import math

class GeneralConfiguration:
    # Constructor
    def __init__(self) :
        self.initPygame()
        
        # Parameters for the buttons
        self._buttonWidht  = 150
        self._buttonHeight = 80
        
        # Parameter for the emoticones
        self._emoticoneSize   = 400
        self._emoticoneBorder = 20 
        
    # Getters / Setters
    #Screen
    def getButtonWidth(self) :  return self._buttonWidth
    def getButtonHeight(self) : return self._buttonHeight
    def setButtonWidth(self, value) : self._buttonWidht   = value
    def setButtonHeight(self, value) : self._buttonHeight = value
    # Emoticone
    def getEmoticoneSize(self) : return self._emoticoneSize
    def getEmoticoneBorder(self): return self._emoticoneBorder
    def setEmoticoneSize(self, value) :   self._emoticoneSize = value 
    def setEmoticoneBorder(self, value) : self._emoticoneBorder = value
        
    # Initializes pygame
    def initPygame(self): 
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((800, 600))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)
        # Gets pygame screen
        self.screen = pygame.display.get_surface()
        
    # Draws on pygame screen    
    def draw(self):
        # Draws a circle in red with a center in 100, 100 and a radius equal to 80
        head = pygame.draw.circle(self.screen, [255, 0, 0], [100, 100], 80) 
        # Draws a black ellipse contained in a rectangle whose left upper corner is 50,60, 
        # width=15 and height=20
        leftEye = pygame.draw.ellipse(self.screen, [0,0,0], [70, 80, 17, 25])
        # Draws a black ellipse contained in a rectangle whose left upper corner is 50,60, 
        # width=15 and height=20
        rightEye = pygame.draw.ellipse(self.screen, [0,0,0], [110, 80, 17, 25])
        # Draws a black arc contained in a rectangle whose left upper corner is 60,120, 
        # width=80, height=30, starting angle=5*pi/4, ending angle=7*pi/4
        pygame.draw.arc(self.screen, [0,0,0], [50, 120, 100, 50], math.pi/4, 3*math.pi/4)
       
        # Draws a black line starting in position 50,100 and ending in position 150,100
        #pygame.draw.line(self.screen, [0,0,0], [50,100], [150,100]) 
        
        # Head's outline
        outline = pygame.draw.rect(self.screen, [255, 255, 255], [20, 20, 160, 160], 1)
            
    # Displays pygame screen
    def display(self):
        # Draws on the screen surface
        self.draw()        
        # Updates the displat and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
