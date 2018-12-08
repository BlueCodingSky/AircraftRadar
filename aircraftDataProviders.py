import json
from models import Aircraft
from abc import ABC, abstractmethod

class DataProvider(ABC):

    def __init__(self):
        self.parser = AircraftParser()

    def getAircrafts(self):
        data = self.readAircraftJson()
        return self.parser.parseAircraftsFromJson(data)

    @abstractmethod
    def readAircraftJson(self):
        pass


class FileDataProvider(DataProvider):

    def __init__(self, fileName):
        self.fileName = fileName
        self.parser = AircraftParser()

    def readAircraftJson(self):
        with open(self.fileName, 'r') as aircraftFile:
            return json.load(aircraftFile)


class AircraftParser(object):

        def parseAircraftsFromJson(self,aircraftJson):
                aircrafts = []
                for aircraft in aircraftJson['aircraft']:
                        if all (k in aircraft for k in ("lon", "lat")):
                                aircrafts.append(Aircraft(aircraft["lat"], aircraft["lon"]))
                return aircrafts