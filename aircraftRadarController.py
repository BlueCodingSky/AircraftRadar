import json
import queue
from aircraftParser import *
from tkinter import *
from radarview import RadarView
from threading import Thread
from time import sleep

class AircraftRadarController(object):

    def __init__(self, window):
        self.window = window
        self.q = queue.Queue()
        self.parser = AircraftParser()
        self.workerThread = Thread(target=self.provideAircraftData)

    def showAircraftRadar(self):
        RadarView(self.window, self.q, controller=self)
        self.workerThread.start()

    def readAircraftJson(self):
        with open('/Users/Kuppi/Desktop/Raspi/aircraft.json', 'r') as aircraftFile:
            return json.load(aircraftFile)

    def provideAircraftData(self):
        while True:
            data = self.readAircraftJson()
            aircrafts = self.parser.parseAircraftsFromJson(data)
            self.q.put(aircrafts)
            sleep(1)
                