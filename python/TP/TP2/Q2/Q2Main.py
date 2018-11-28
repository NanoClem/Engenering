# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import pygame
from Q2GeneralConfiguration import GeneralConfiguration
from Q2Emoticon import Emoticon

def main():
 
    # Creates the general configuration and the sensors
    generalConfiguration = GeneralConfiguration()
    
    # Creates an emoticon
    emoticon = Emoticon()
    # Injects the general configuration in the emoticon
    emoticon.setGeneralConfiguration(generalConfiguration)
   # print(emoticon.headToArea([10,10]))   
    #print(emoticon.color(1))
    emoticon.setEmoticoneParameters(emoticon.generalConfiguration.emoticonSize)
    # Infinite loop    
    while True:

        # Waits for an event
        event = pygame.event.wait()
 
        if event.type == pygame.QUIT:
            pygame.quit()
            break 
        
        # Draws the emoticon
        elif event.type == pygame.USEREVENT:
            emoticon.draw()
            generalConfiguration.display()
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Just pass
            pass
                
# Calls the main function
if __name__ == "__main__":
    main()    
