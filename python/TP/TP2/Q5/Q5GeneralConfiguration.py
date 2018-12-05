# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q5Emoticon import Emoticon
from Q5Button import Button

class GeneralConfiguration:
    # Constructor
    def __init__(self) :
        self.initPygame()
        
        # Parameters for the emoticons        
        self._emoticonSize = 400
        self._emoticonBorder = 20  
        
        # Parameters for the buttons
        self._buttonWidth = 150
        self._buttonHeight = 80
                
        # Sensors list
        self._sensors = []
        self._selectedSensor = 0
        
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
        
    # GETTERS / SETTERS
    # Screen
    def getButtonWidth(self)  :  return self._buttonWidth
    def getButtonHeight(self) :  return self._buttonHeight
    def getButtonBorder(self, sensorID) :  return self.getSensors()[sensorID].button.getBorder()
    def setButtonWidth(self, value)  : self._buttonWidht  = value
    def setButtonHeight(self, value) : self._buttonHeight = value
    def setButtonBorder(self, sensorID, value) : self.getSensors()[sensorID].button.setBorder()
    # Emoticon
    def getEmoticonSize(self)  : return self._emoticonSize
    def getEmoticonBorder(self): return self._emoticonBorder
    def setEmoticonSize(self, value)   : self._emoticonSize   = value 
    def setEmoticonBorder(self, value) : self._emoticonBorder = value
    # Sensor
    def getSensors(self)        : return self._sensors
    def getSelectedSensor(self) : return self._selectedSensor
    def setSelectedSensor(self, value) : self._selectedSensor = value

        
    # Adds a sensor    
    def addSensor(self, sensor):
        sensor.setGeneralConfiguration(self)
        sensor.setSensorId(len(self._sensors))
        # Gestion de l'emoticon
        Semoticon = Emoticon(sensor)
        Semoticon.setEmoticoneParameters(self.getEmoticonSize())
        sensor.setEmoticon(Semoticon)
        # Gestion du boutton
        sensor.setButton(Button(sensor))
        
        self._sensors.append(sensor)
 
    
    # Retrieves the sensor id from a posiiion
    def positionToSensorId(self, position):
        for i in range(len(self.getSensors())):
            # Test en hauteur
            if position[1] <= self.getButtonHeight() :
                # Test en largeur
                if position[0] >= i*self.getButtonWidth()+20 and position[0] <= (i+1)*self.getButtonWidth()+20 :
                    print("Position du curseur :", position)
                    print("ID SENSOR :", i)
                    return i
            else:
                return None
            

    # Checks if the display of a new sensor was requested
    def checkIfSensorChanged(self, eventPosition):
        # ID du sensor courrant
        currentSensor = self.positionToSensorId(eventPosition)
        # Mise a jour du sensor courrant
        if(currentSensor != None):
            self.setSelectedSensor(currentSensor)
            for i in range(len(self.getSensors())):
                self.getSensors()[i].isSelected(currentSensor)
            
    
    # Draws on pygame screen
    def draw(self):
        # Clears the surface
        pygame.display.get_surface().fill([0, 0, 0])
        self.getSensors()[self.getSelectedSensor()].drawEmoticon()      # Draw the emoticon of the current sensor
        # Draw every buttons
        for i in range(len(self.getSensors())):
            self.getSensors()[i].drawButton(i*self.getButtonWidth() + 20, 0, self.getButtonBorder(i))        
            
    # Displays   
    def display(self):
        # Draws on the screen surface
        self.draw()
        
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
               