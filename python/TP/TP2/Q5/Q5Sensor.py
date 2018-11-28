# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import http
import urllib

class Sensor:
    # Constructor
    def __init__(self, url, label, thresholds):
        self.url = url
        self.label = label
        self.thresholds = thresholds

    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration

    def setEmoticon(self, emoticon):
        self.emoticon = emoticon

    def setButton(self, button):
        self.button = button

    def setSensorId(self, sensorId):
        self.sensorId = sensorId

    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration

    def getSensorId(self):
        return self.sensorId

    def getLabel(self):
        return self.label

    # Checks if the connection to the sensor is set
    def isConnectedToUrl(self):
        try:
            self.request = urllib.request.urlopen(self.url)
        except OSError:
            return False
        else:
            return self.request.getcode() == http.HTTPStatus.OK

    # Reads the sensor
    def read(self):
        if self.isConnectedToUrl():
            return self.request.read().decode('utf-8')
        else:
            return None

    # Gets the transformed value
    def getTransformedValue(self):
        pass

    # Draws the emoticon for this sensor
    def drawEmoticon(self):
        pass

    # Draws the button for this sensor
    def drawButton(self):
        pass