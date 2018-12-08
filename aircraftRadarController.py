import json
import queue
from tkinter import *
from radarview import RadarView
from threading import Thread
from time import sleep
import math
from models import *
from radarViewModels import *

class AircraftRadarController(object):

    def __init__(self, aircraftProvider,window):
        self.window = window
        self.q = queue.Queue()
        self.provider = aircraftProvider
        self.workerThread = Thread(target=self.provideAircraftData)
        self.cancel = False
        self.positionCalculator = RelativPositionCalculator(47.5, 9.2417)

    def showAircraftRadar(self):
        RadarView(self.window, self.q, controller=self)
        self.workerThread.start()

    def stop(self):
        self.cancel = True

    def provideAircraftData(self):
        while self.cancel == False:
            aircrafts = self.provider.getAircrafts()
            viewModels = list(map(lambda x: self.aircraftToViewModel(x), aircrafts))
            self.q.put(viewModels)
            sleep(2)

    def aircraftToViewModel(self, aircraft):
        relaticePosition = self.positionCalculator.calculateRelativePosition(aircraft.longitude, aircraft.latitude)
        return AircraftViewModel(relaticePosition.distance, relaticePosition.bearing)              

class RelativPositionCalculator(object):

    def __init__(self, currentLatitude, currentLongitude):
        self.currentLatitude = currentLatitude
        self.currentLongitude = currentLongitude

    def calculateRelativePosition(self, targetLongitude, targetLatitude):
        longitude = self.currentLongitude
        latitude = self.currentLatitude
        dlong = (targetLongitude-longitude) / 180 * math.pi
        lat1rad= latitude / 180 * math.pi
        lat2rad= targetLatitude / 180 * math.pi
      
        targetDistance = 6378.388 *  math.acos(math.sin(latitude / 180 * math.pi) * math.sin(targetLatitude / 180 * math.pi) + math.cos(latitude / 180 * math.pi) * math.cos(targetLatitude / 180 * math.pi) * math.cos(targetLongitude / 180 * math.pi - longitude / 180 * math.pi))
        
        y = math.sin(dlong) * math.cos(lat2rad)
        x = math.cos(lat1rad)* math.sin(lat2rad) - math.sin(lat1rad)* math.cos(lat2rad) * math.cos(dlong)

        targetAngle = math.atan2(y, x) * 180 / math.pi
        
        if targetAngle < 0:
        	targetAngle = (180 + (180 + targetAngle))
        
        bearing= int(targetAngle)
        targetDistanceMeter = int(targetDistance * 1000)

        return RelativePosition(targetDistanceMeter, bearing)