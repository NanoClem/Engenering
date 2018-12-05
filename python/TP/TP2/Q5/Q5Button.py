# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame     
        
class Button:
    """
        Cette classe est une interface graphique d'un sensor sous forme de bouton
        elle permet d'afficher les differentes informations du sensor
    """
    
    def __init__(self, sensor) :
        """
            CONSTRUCTEUR
            :param sensor: sensor lie au bouton
        """
        self._sensor = sensor
        self._border = 1
        

    def getPosition(self) : 
        """
            Retourne la position du bouton
            :return: position du bouton sous forme de liste
        """
        return [self._sensor.generalConfiguration.getButtonWidth(), self._sensor.generalConfiguration.getButtonHeight()]
    
    
    
    def getBorder(self) : 
        """
            Retourne l'epaisseur du bouton
            :return: epaisseur du bouton
        """
        return self._border 
    


    def setBorder(self, value) :
        """
            Modifie l'epaisseur du bouton
            :param value: nouvelle epaisseur du bouton
        """
        self._border = value

    
    
    def draw(self, width=0, height=0, border=1):
        """
            Dessine le bouton a l'ecran
            :param width: abscisse du bouton
            :param height: ordonnee du bouton
            :param border: epaisseur du bouton
        """
        buttonPos = self.getPosition()
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, [255,255,255], [width, height, buttonPos[0], buttonPos[1]], self.getBorder())
            
        

    def drawLines(self, lines, width=0):
        """
            Dessine les information du sensor dans le cadre du bouton sous forme d'image
            :param lines: liste des informations du sensor
            :param width: posistion en abscisse de l'image
        """
        screen = pygame.display.get_surface()
        
        # Create the font
        font = pygame.font.Font(None, 18)
        
        # Positions
        posLine    = [0,0]                          # position de la ligne
        buttonSize = self.getPosition()             # dimensions du bouton
        jump       = buttonSize[1] / len(lines)     # valeur du saut de ligne
        ajust      = 2                              # valeur de réajustement 
        
        for i in range(len(lines)):
            # Center and create new lines
            if(lines[i] == ""):
                # texte compris dans l'image
                textImage = font.render(lines[i+1], 0, [255,255,255])
                posLine[0] = buttonSize[0]/2 - int(textImage.get_rect()[2]/2) + width
                posLine[1] = buttonSize[1]/(2+ajust) + i*jump
                
            # Print text
            screen.blit(textImage, [posLine[0], posLine[1]]) 

