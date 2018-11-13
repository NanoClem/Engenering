# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import httplib
from urlparse import urlparse
import socket

class Sensor:
    # Constructor
    def __init__(self, url, label, thresholds):
        self.url = url
        self.label = label 
        self.thresholds = thresholds
    
    # Setters
    def setGeneralConfiguration(self, generalConfiguration):
        self.generalConfiguration = generalConfiguration
    
    # Getters
    def getGeneralConfiguration(self):
        return self.generalConfiguration       

    def getLabel(self):
        return self.label
                     
    # Checks if the connection to the sensor is set
    def isConnectedToUrl(self):
        self.parsedUrl = urlparse(self.url)
        self.connection = httplib.HTTPConnection(self.parsedUrl.netloc, 80, 1) 
        try:
            self.connection.request('GET', self.url)
        except socket.error:
            return False
        else: 
            self.response = self.connection.getresponse()
        return self.response.status == httplib.OK
        
    # Reads the sensor
    def read(self):
        if self.isConnectedToUrl():
            return self.response.read()
        else:
            return None
            
    # Gets the transformed value
    def getTransformedValue(self):
        pass
                   
        