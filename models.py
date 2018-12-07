class Aircraft(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class RelativePosition(object):
    def __init__(self, distance, bearing):
        self.distance = distance
        self.bearing = bearing
