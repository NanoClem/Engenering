# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import http
import urllib

class Sensor:
    """
        Cette classe represente un capteur de differente nature (temperature, puissance, ...)
    """
    
    
    def __init__(self, url, label, thresholds):
        """
            CONSTRUCTEUR
            :param url: url du sensor
            :param label: description du sensor
            :param tresholds: seuils des valeurs du sensor
        """
        self.url = url
        self.label = label
        self.thresholds = thresholds



    def setGeneralConfiguration(self, generalConfiguration):
        """
            Injection de la classe generalConfiguration
            :param generalConfiguration: classe dont le sensor depend
        """
        self.generalConfiguration = generalConfiguration



    def setEmoticon(self, emoticon):
        """
            Ajout d'un emoticone au sensor
            :param emoticon: l'emoticone a ajouter
        """
        self.emoticon = emoticon



    def setButton(self, button):
        """
            Ajout d'un bouton
            :param bouton: le bouton a ajouter
        """
        self.button = button



    def setSensorId(self, sensorId):
        """
            Ajout d'un ID
            :param sensorID: ID du sensor
        """
        self.sensorId = sensorId



    def getGeneralConfiguration(self):
        """
            Recuperation la classe de dependance
            :return: classe dont le sensor depend
        """
        return self.generalConfiguration



    def getSensorId(self):
        """
            Recuperation de l'ID
            :return: ID du sensor
        """
        return self.sensorId
    
    
    
    def getLabel(self):
        """
            Recuperation de la description du sensor
            :return: description du sensor
        """
        return self.label



    def isConnectedToUrl(self):
        """
            Permet de savoir si le sensor est connecte a son url
            :return: True si le sensor est connecte, False sinon
        """
        try:
            self.request = urllib.request.urlopen(self.url)
        except OSError:
            return False
        else:
            return self.request.getcode() == http.HTTPStatus.OK
        
        
    
    def isSelected(self, sensorID) :
        """
            Permet de savoir si le sensor est selectionne dans le menu et regle la bordure de son bouton
            :return: True s'il est selectione, False sinon
        """
        if sensorID == self.getSensorId() :
            self.button.setBorder(3)
            return True
        
        self.button.setBorder(1)
        return False



    def read(self):
        """
            Lis la valeur du sensor envoyee grace a la connection par son url
            :return: valeur du sensor
        """
        if self.isConnectedToUrl():
            return self.request.read().decode('utf-8')
        else:
            return None



    def getTransformedValue(self):
        """
            Calcule une valeur normalisee sur [-1,1] de la valeur lue du sensor
            :return: valeur normalisee du sensor
        """
        sensValue  = float(self.read())      # valeur du sensor
        result     = 0                       # résultat après normalisation
        Smin       = self.thresholds[0]
        Sneutral   = self.thresholds[1]
        Smax       = self.thresholds[2]
        
        # NORMALISATION DE LA VALEUR DU SENSOR
        if(sensValue < Sneutral):
            result = (sensValue - Sneutral) / (Sneutral - Smin)
        else :
            result = (sensValue - Sneutral) / (Smax - Sneutral)
            
        # ECRETAGE
        if(result > 1):
            result = 1
        elif(result < -1):
            result = -1
            
        return result
    


    def drawEmoticon(self):
        """
            Dessine l'emoticone du sensor
        """
        self.emoticon.draw()



    def drawButton(self, width=0, height=0, border=1):
        """
            Dessine le bouton du sensor
            :param width: position en abscisse du bouton
            :param height: position en ordonnee du bouton
            :param border: epaisseur du bouton
        """
        info = ['', self.getLabel(), '', self.read()]
        self.button.drawLines(info, width)
        self.button.draw(width, height, border)