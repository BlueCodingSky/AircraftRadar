import json

class ConfigStore(object):

    def __init__(self):
        with open('config.json', 'r') as config:
            self.configFile = json.load(config)

    def getAircraftDataSourceType(self):
        return self.configFile['aircraftDataSource']['type']

    def getAircraftDataSourceDestination(self):
        return self.configFile['aircraftDataSource']['destination']