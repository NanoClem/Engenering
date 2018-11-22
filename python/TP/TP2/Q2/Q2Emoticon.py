# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math

class Emoticon:
    
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    
    def setEmoticoneParameters(self,size):
        self.eyeWidth = 0.1*size
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size, 0.1*size]
        self.eyeRightPosition = [0.15*size, 0.1*size]
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size
        self.mouthMaxWidth = 0.55*size
        self.mouthAngle = math.pi/10
    # Draws the emoticon    
    def draw(self):   
       self. head(1)
# retourne les coordonnées dans le repère (o,x,y) du parametre position
    def headToArea(self,position):
        return [int(self.generalConfiguration.screen.get_width()/2+position[0]), int((self.generalConfiguration.emoticonSize/2)+(self.generalConfiguration.emoticonBorder)+(self.generalConfiguration.buttonHeight)-position[1])]
    
    def color(self,x):
      
        if x>=-1 and x<=0 :
            R=255
            V=255*x+255
            
        elif x>=0 and x<=1 :
            R=-255*x+255
            V=255

        else :
            print("format de x non accepté")
        
        return [R,V,0]
    
    def head(self,x):
        screen= pygame.display.get_surface()
         # Draws a circle in red with a center in 100, 100 and a radius equal to 80
        pygame.draw.circle(screen,self.color(x), [100, 100], 80)
        
   def eye(self,position):
        # Draws a black ellipse contained in a rectangle whose left upper corner is 50,60, 
        # width=15 and height=20
        screen= pygame.display.get_surface()
        pygame.draw.ellipse(screen, [0,0,0], [70, 80, 17, 25])
       
   
    