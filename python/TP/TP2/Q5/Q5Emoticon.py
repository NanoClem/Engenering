# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math
  
class Emoticon:
    # Constructor
    def __init__(self, sensor) :
        self.sensor = sensor

    # Sets the emoticon parameters
    def setEmoticonParameters(self, size) :        
        self.eyeWidth = 0.1*size
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size, 0.1*size]
        self.eyeRightPosition = [0.15*size, 0.1*size]    
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size
        self.mouthMaxWidth = 0.55*size
        self.mouthAngle = math.pi/10    

    # Computes the position in the screen 
    def headToArea(self, position):
        pass
        
    # Computes the color    
    def color(self,x):
        pass
 
    # Draws head            
    def head(self, x):
        pass
    
    # Draws one eye    
    def eye(self, position):
        pass

    # Draws the mouth          
    def mouth(self, position, x):
        pass
        
    # Draws the emoticon    
    def draw(self):   
        pass        
        
