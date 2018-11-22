# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
import math

class Emoticon:
<<<<<<< HEAD
    
    #Constructor
    def __init__(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration

=======
    def __init__(self,generalConfiguration):
        # ajout des coordonnées de la tete du centre
        self.headCenter_X=self.generalConfiguration.screen()/2
        self.headCenter_Y=(self.generalConfiguration.emoticonSize/2)+(self.generalConfiguration.emoticonBorder)+(self.generalConfiguration.buttonHeight)
>>>>>>> 6d7a27aa691723e482f3cd7efdb85a4021066160
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration

    # Draws the emoticon    
    def draw(self):   
        pass
# retourne les coordonnées dans le repère (o,x,y) du parametre position
    def headToArea(self,position):
        return [self.headCenter_X+position[0], self.headCenter_Y-position[1]]