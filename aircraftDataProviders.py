import json
from models import Aircraft
from abc import ABC, abstractmethod
import urllib.request

class AircraftProviderFactory(object):

    def getAircraftProvider(self, providerType, aircraftSource):
        if providerType == 'file':
            return FileDataProvider(aircraftSource)

        return WebServerDataProvider(aircraftSource)

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
        super(FileDataProvider, self).__init__()
        self.fileName = fileName

    def readAircraftJson(self):
        with open(self.fileName, 'r') as aircraftFile:
            return json.load(aircraftFile)

class WebServerDataProvider(DataProvider):

    def __init__(self, url):
        super(WebServerDataProvider, self).__init__()
        self.url = url

    def readAircraftJson(self):
        with urllib.request.urlopen(self.url) as url:
            return json.loads(url.read().decode('utf-8'))

class AircraftParser(object):

        def parseAircraftsFromJson(self,aircraftJson):
                aircrafts = []
                for aircraft in aircraftJson['aircraft']:
                        if all (k in aircraft for k in ("lon", "lat")):
                                aircrafts.append(Aircraft(aircraft["lat"], aircraft["lon"]))
                return aircrafts