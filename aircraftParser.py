import json
from models import Aircraft

class AircraftParser(object):

        def parseAircraftsFromJson(self,aircraftJson):
                aircrafts = []
                for aircraft in aircraftJson['aircraft']:
                        if all (k in aircraft for k in ("lon", "lat")):
                                aircrafts.append(Aircraft(aircraft["lat"], aircraft["lon"]))
                return aircrafts


