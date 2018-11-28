# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame


# =============================================================================
# CLASSE BOUTON
# =============================================================================
class Button:

    """
    SETTERS
    """
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
        
        
    """
    GETTERS
    """
    def getPosition(self):
        return [self.generalConfiguration.buttonWidth, self.generalConfiguration.buttonHeight]


    """
    DESSINE LE BOUTON A L'ECRAN
    """
    def draw(self):
        buttonPos = self.getPosition()
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, [255,255,255], [0, 0, buttonPos[0], buttonPos[1]], 1)
            
        
    """
    DESSINE LES LIGNES CONTENUES DANS LE BOUTON
    """
    def drawLines(self, lines):
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
                posLine[0] = buttonSize[0]/2 - int(textImage.get_rect()[2]/2)
                posLine[1] = buttonSize[1]/(2+ajust) + i*jump
                
            # Print text
            screen.blit(textImage, [posLine[0], posLine[1]])
            
