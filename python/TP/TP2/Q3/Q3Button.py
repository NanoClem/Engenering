# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame

class Button:

    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
        
        
    # Getters
    def getPosition(self):
        return [self.generalConfiguration.buttonWidth, self.generalConfiguration.buttonHeight]


    # Draws the button    
    def draw(self):
        buttonPos = self.getPosition()
        screen = pygame.display.get_surface()
        # Draw the button
        pygame.draw.rect(screen, [255,255,255], [buttonPos[0], buttonPos[0], buttonPos[1], buttonPos[1]], 1)
        
    
    # Draw lines text
    def drawLines(self, lines):
        screen = pygame.display.get_surface() 
        
        # Create the font
        font = pygame.font.Font(None, 14)
        
        # Image text
        posLine = [0,0]
        
        for i in range(len(lines)):
            # Center and create new lines
            if(lines[i] == ""):
                textImage = font.render(lines[i+1], 0, [255,255,255])
                posLine[0] += 10
                posLine[1] += 20
                
            
            
                
            # If the line position excess the image's height
#            if(posLine > textImage.get_height()):
#                posLine = textImage.get_height()
            # Print text
            screen.blit(textImage, [posLine[0], posLine[1]])
            
