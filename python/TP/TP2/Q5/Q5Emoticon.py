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

    def setEmoticoneParameters(self,size):
        self.eyeWidth = 0.1*size
        self.eyeHeight = 0.15*size
        self.eyeLeftPosition = [-0.15*size, 0.1*size]
        self.eyeRightPosition = [0.15*size, 0.1*size]
        self.mouthPosition = [0, -0.25*size]
        self.mouthMaxHeight = 0.3*size
        self.mouthMaxWidth = 0.55*size
        self.mouthAngle = math.pi/10
        
    # Draws the emoticon  (à modifier pour faire correspondre vaec la valeur normalisée du sensor)
    def draw(self):
        self. head(self.sensor.getTransformedValue())
        self.eye(self.eyeLeftPosition)
        self.eye(self.eyeRightPosition)
        self.mouth(self.mouthPosition,self.sensor.getTransformedValue())
        
    # retourne les coordonnées dans le repère (o,x,y) du parametre position
    def headToArea(self,position):
        return [int(self.sensor.generalConfiguration.screen.get_width()/2+position[0]), int((self.sensor.generalConfiguration.getEmoticonSize()/2)+(self.sensor.generalConfiguration.getEmoticonBorder())+(self.sensor.generalConfiguration.getButtonHeight())-position[1])]
    #retourne la couleur associé au parametre x
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
    
    # construit la tete de l'emoticone en dessinant un cercle de centre (0,0) et de rayon la motié emoticoneSize
    def head(self,x):
        screen= pygame.display.get_surface()
        # Draws a circle in red with a center in 100, 100 and a radius equal to 80
        pygame.draw.circle(screen,self.color(x), self.headToArea([0,0]),int(self.sensor.generalConfiguration.getEmoticonSize()/2))
        
    # dessine l'oeil de l'emoticone
    # position étant des coordonnées exprimer dans le repère (o',x',y')
    def eye(self,position):
        # Draws a black ellipse contained in a rectangle whose left upper corner is 50,60,
        # width=15 and height=20
        eyepos=self.headToArea(position)
        screen= pygame.display.get_surface()
        pygame.draw.ellipse(screen, [0,0,0],[eyepos[0]-self.eyeWidth/2 ,eyepos[1]-self.eyeHeight,self.eyeWidth,self.eyeHeight])
    
    # mouth(self,position,x) 
    # dessine la bouche de l'emoticone en prenant en compte le parametre x compris entre -1 et 1 et position étant des coordonnées exprimer dans le repère (o',x',y')
    def mouth(self,position,x) :
        mouthCenter=self.headToArea(position)
        screen= pygame.display.get_surface()
        if (x<0.15 and x>=-0.15) or (x>0.15):
            pygame.draw.arc(screen, [0,0,0], [mouthCenter[0] - self.mouthMaxWidth/2 ,mouthCenter[1]-self.mouthMaxHeight/2, self.mouthMaxWidth,self.mouthMaxHeight*abs(x)],math.pi+self.mouthAngle , -self.mouthAngle)
            
        if x==0:
            pygame.draw.line(screen, [0,0,0], [mouthCenter[0]-self.mouthMaxWidth/2 ,mouthCenter[1]],[mouthCenter[0]+self.mouthMaxWidth/2 ,mouthCenter[1]])
            
        if x<-0.15:
            pygame.draw.arc(screen, [0,0,0], [mouthCenter[0] - self.mouthMaxWidth/2 ,mouthCenter[1]-self.mouthMaxHeight/2, self.mouthMaxWidth,self.mouthMaxHeight*abs(x)],self.mouthAngle,math.pi-self.mouthAngle )
     
        
