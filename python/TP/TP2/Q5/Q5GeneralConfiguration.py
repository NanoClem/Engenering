# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import pygame
from Q5Emoticon import Emoticon
from Q5Button import Button

class GeneralConfiguration:
    """
     Cette classe est une interface entre les differents modules du projet
    """


    def __init__(self) :
        """
            CONSTRUCTEUR
        """
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
        
        
        
    def initPygame(self): 
        """
            Initialise pygame
        """
        #Initialization
        pygame.init()
        # Sets the screen size.
        pygame.display.set_mode((800, 600))    
        # Sets the timer to check event every 200 ms
        pygame.time.set_timer(pygame.USEREVENT, 200)         
        # Gets pygame screen
        self.screen = pygame.display.get_surface()         
        


    def getButtonWidth(self) :
        """
            Retourne la largeur du bouton
            :return: largeur du bouton
        """
        return self._buttonWidth
    
    
    
    def getButtonHeight(self) :
         """
            Retourne la hauteur du bouton
            :return: hauteur du bouton
         """
         return self._buttonHeight
    
    
    
    def getButtonBorder(self, sensorID) :
        """
            Retourne l'epaisseur du bouton
            :return: epaisseur du bouton
        """
        return self.getSensors()[sensorID].button.getBorder()
    
    
    
    def setButtonWidth(self, value)  : 
        """
            Modifie la largeur du bouton
            :param value: valeur de la nouvelle largeur
        """
        self._buttonWidht  = value
        
        
        
    def setButtonHeight(self, value) : 
        """
            Modifie la hauteur du bouton
            :param value: valeur de la nouvelle hauteur
        """
        self._buttonHeight = value
        
        
        
    def setButtonBorder(self, sensorID, value) : 
        """
            Modifie l'paisseur du bouton
            :param sensorID: id du sensor
            :param value: valeur de la nouvelle epaisseur
        """
        self.getSensors()[sensorID].button.setBorder()
        
    
    
    def getEmoticonSize(self) : 
        """
            Retourne la taille de l'emoticone
            :return: taille de l'emoticone
        """
        return self._emoticonSize
    
    
    
    def getEmoticonBorder(self) : 
        """
            Retourne l'epaisseur de l'emoticone
            :return: epaisseur de l'emoticone
        """
        return self._emoticonBorder
    
    
    
    def setEmoticonSize(self, value) : 
        """
            Modifie la taille de l'emoticone
            :param value: nouvelle taille de l'emoticone
        """
        self._emoticonSize   = value 
    
    
    
    def setEmoticonBorder(self, value) : 
        """
            Modifie l'epaisseur de l'emoticone
            :param value: nouvelle epaisseur de l'emoticone
        """
        self._emoticonBorder = value
        
        
        
    def getSensors(self) : 
        """
            Retourne la liste des sensors
            :return: liste des sensors
        """
        return self._sensors
    
    
    
    def getSelectedSensor(self) : 
        """
            Retourne le sensor selectionne
            :return: id du sensor selectionne
        """
        return self._selectedSensor
    
    
    
    def setSelectedSensor(self, value) : 
        """
            Modifie l'id sensor courrant
            :param: nouvel id de sensor
        """
        self._selectedSensor = value

        
  
    def addSensor(self, sensor):
        """
            Ajoute un nouveau sensor
            :param: sensor a ajouter
        """
        sensor.setGeneralConfiguration(self)
        sensor.setSensorId(len(self._sensors))
        # Gestion de l'emoticon
        Semoticon = Emoticon(sensor)
        Semoticon.setEmoticoneParameters(self.getEmoticonSize())
        sensor.setEmoticon(Semoticon)
        # Gestion du boutton
        sensor.setButton(Button(sensor))
        
        self._sensors.append(sensor)
 
    

    def positionToSensorId(self, position):
        """
            Retourne l'id du sensor dont la position de la souris est située dans la zone du bouton associe
            :param position: position de la souris sous forme de liste
        """
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
            

    
    def checkIfSensorChanged(self, eventPosition):
        """
            Verifie si l'affichage des sensors doit être change, et le change
            :param eventPosition: position de la souris sous forme de liste
        """
        # ID du sensor courrant
        currentSensor = self.positionToSensorId(eventPosition)
        # Mise a jour du sensor courrant
        if(currentSensor != None):
            self.setSelectedSensor(currentSensor)
            for i in range(len(self.getSensors())):
                self.getSensors()[i].isSelected(currentSensor)
            
    

    def draw(self):
        """
            Dessine tous les elements du projet a l'ecran
        """
        # Clears the surface
        pygame.display.get_surface().fill([0, 0, 0])
        self.getSensors()[self.getSelectedSensor()].drawEmoticon()      # Draw the emoticon of the current sensor
        # Draw every buttons
        for i in range(len(self.getSensors())):
            self.getSensors()[i].drawButton(i*self.getButtonWidth() + 20, 0, self.getButtonBorder(i))        
            
            
  
    def display(self):
        """
            Affiche a l'ecran des evenements en prenant en compte la boucle d'evenement
        """
        # Draws on the screen surface
        self.draw()
        
        # Updates the display and clears new timer events
        pygame.display.flip()
        pygame.event.clear(pygame.USEREVENT)
               